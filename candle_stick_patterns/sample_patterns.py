import talib
import yfinance as yf
datafiles=os.listdir('candle_stick_patterns/datasets/daily')
with open('candle_stick_patterns/datasets/symbols.csv') as f:
        companies = f.read().splitlines()
        for company in companies:
            symbol = company.split(',')[0]
            print(symbol)
            data = yf.download(symbol, start="2023-01-01", end="2023-01-20")
            data.to_csv('candle_stick_patterns/datasets/daily/{}.csv'.format(symbol))
#print(data)

# morningstar=talib.CDLMORNINGSTAR(data['Open'],data['High'],data['Low'],data['Close'])
# engulfing = talib.CDLENGULFING(data['Open'],data['High'],data['Low'],data['Close'])
# hammer = talib.CDLHAMMER(data['Open'],data['High'],data['Low'],data['Close'])
# data['Morning Star'] = morningstar
# data['Engulfing'] = engulfing
# data['Hammer'] = hammer

# # morning_star=data[data['Morning Star'] !=0]
# engulfing_days=data[data['Engulfing'] !=0]
# # hammer_days=data[data['Hammer'] !=0]

# print(engulfing_days)




#print(morning_star)

#print(hammer_days)


        print("*****Working*****")
        for filename in datafiles:
            df = pd.read_csv("candle_stick_patterns/datasets/daily/{}".format(filename))
            #print(df)
            pattern_function=getattr(talib,pattern)
            symbol = filename.split('.')[0]
