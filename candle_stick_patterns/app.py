from ast import YieldFrom
from flask import Flask, render_template, request
from patterns import patterns
import yfinance as yf
import os, csv
import pandas as pd
import talib



app = Flask(__name__)

@app.route('/')
def index():
    pattern = request.args.get('pattern',None)
    stocks = {}
    with open('candle_stick_patterns/datasets/symbols.csv') as f:
        for row in csv.reader(f):
            stocks[row[0]] = {'company':row[1]}
            #print(stocks)
    if pattern:
        datafiles=os.listdir('candle_stick_patterns/datasets/daily')
        print("*****Working*****")
        for filename in datafiles:
            df = pd.read_csv("candle_stick_patterns/datasets/daily/{}".format(filename))
            #print(df)
            pattern_function=getattr(talib,pattern)
            symbol = filename.split('.')[0]
            print(symbol)
            
            try:
                result=pattern_function(df['Open'],df['High'],df['Low'],df['Close'])
                
                print(result)
                last = result.tail(1).values[0]
               
                print("{} triggered {}".format(filename, pattern))
                if last > 0:
                    stocks[symbol][pattern] = 'bullish'

                elif last < 0:
                    stocks[symbol][pattern] = 'bearish'

                else:
                    stocks[symbol][pattern] = None
        
                #print(last)
                #print("{} triggered {}".format(filename, pattern))
            except:
                pass

    return render_template('index.html', patterns=patterns, stocks=stocks, current_pattern=pattern)


@app.route('/snapshot')

def snapshot():
    with open('candle_stick_patterns/datasets/symbols.csv') as f:
        companies = f.read().splitlines()
        for company in companies:
            symbol = company.split(',')[0]
            print(symbol)
            # df=yf.download(symbol, start="2023-01-18", end="2023-01-19")
            # df.to_csv('candle_stick_patterns/datasets/daily/{}.csv'.format(symbol))

        
    return {


        'code': 'success'
    }