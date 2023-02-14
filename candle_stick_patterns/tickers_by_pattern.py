import talib
import yfinance as yf
import os
from patterns import patterns
import pandas as pd
import csv
import datetime

def getchildfoldernames(path):
    childfolretlst=[]
    root, dirs, files = os.walk(path).__next__()
    return dirs

def getchildfolderfilenames(path):
    symblst=[]
    datafiles=os.listdir(path)
        
    for filename in datafiles:
        symbol = filename.split('.')[0]
        symblst.append(symbol)
    return symblst

def readdatafromcsvfiles(path,filenamewithextension):
    
    df = pd.read_csv(path+"{}".format(filenamewithextension))
    return df


def addunderscoreindictvalues(mydict):
    myunderscoredict={}
    for key,value in mydict.items():
        values=value.replace(" ","_")
        value_updated=values.replace("/","_")
        value_changed_brackets=value_updated.replace("(","")
        value_changed=value_changed_brackets.replace(")","")
        myunderscoredict[key]=value_changed
    return myunderscoredict
      


    # print(value)


#patchfolder=getchildfoldernames("candle_stick_patterns/patterns_analysis/")
#tckchfolder=getchildfolderfilenames("candle_stick_patterns/datasets/daily/")

startdates="2022-04-01"
enddates="2022-06-15"
daystogobackfordates=243

previous_Date = datetime.datetime.today() - datetime.timedelta(days=daystogobackfordates)
previous_Date_Formatted = previous_Date.strftime ('%m-%d-%Y')

datafiles=os.listdir('candle_stick_patterns/datasets/daily_allstocks/')
count=0
for filename in datafiles:
    count+=1
    #print(str(count))
    # cpath=('candle_stick_patterns/pattern_analysis/consolidated_tickers_by_pattern/tickers_in_consolidated_error_{}.csv').format(previous_Date_Formatted)
    # cle=open(cpath,'a')
    #     #writer = csv.writer(fle)
    # writerc = csv.writer(cle)
  
    df_stocks_by_date_scan = readdatafromcsvfiles("candle_stick_patterns/datasets/daily_allstocks/",filename)
    #df=df_stocks_by_date_scan[df_stocks_by_date_scan['Date']>'2023-01-05']
    mask = (df_stocks_by_date_scan['Date'] > startdates) & (df_stocks_by_date_scan['Date'] <= enddates)
    df = df_stocks_by_date_scan.loc[mask]
    symbol = filename.split('.')[0]
    #print(symbol)
    #print(df[df["Date"]=="2023-01-05"])

    #print(df)
    dictvalueswithunderscore=addunderscoreindictvalues(patterns)
    for pattern,value in dictvalueswithunderscore.items():
        
        #print(symbol+"********"+pattern+"********")
        pattern_function=getattr(talib,pattern)
        #ppath=('candle_stick_patterns/pattern_analysis/{}/').format(value)
        
        path=('candle_stick_patterns/pattern_analysis/tickers_by_candlesticks_pattern/tickers_in_{}').format(value)
        cpath=('candle_stick_patterns/pattern_analysis/consolidated_tickers_by_pattern/tickers_in_consolidated_{}.csv').format(previous_Date_Formatted)
        #fle = open(path, 'a')
        cle=open(cpath,'a')
        #writer = csv.writer(fle)
        writerc = csv.writer(cle)
       
        try:
            result=pattern_function(df['Open'],df['High'],df['Low'],df['Close'])
            # print(symbol)
            # print(pattern)
            # print(result)
            last = result.tail(1).values[0]
            #print("Symbol"+symbol+" "+last)
            #print("{} triggered {}".format(filename, pattern))
            #if df["Date"]=="2023-01-19":
            
            if last > 0:
                print("*****Bullish******--->"+symbol+" "+pattern)
                print(symbol)
                
                #writer.writerow([previous_Date_Formatted, pattern, symbol, value, "Bullish"])
                writerc.writerow([previous_Date_Formatted, pattern, symbol, value, "Bullish"])

            elif last < 0:
                print("*****Bearish******--->"+symbol+" "+pattern)
                print(symbol)
                
                #writer.writerow([previous_Date_Formatted, pattern, symbol, value, "Bearish"])
                writerc.writerow([previous_Date_Formatted, pattern, symbol, value, "Bearish"])

            
            else:
                #stocks[symbol][pattern] = None
                #print("*****None******--->"+symbol+" "+pattern)
                pass
    
            #print(last)
            # print("{} triggered {}".format(filename, pattern))
        except:
            pass




