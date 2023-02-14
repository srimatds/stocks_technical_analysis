import talib
import yfinance as yf
import os
import pandas as pd
#from tickers_by_pattern import readdatafromcsvfiles

# datafiles=os.listdir('candle_stick_patterns/datasets/daily')
# with open('candle_stick_patterns/datasets/symbols.csv') as f:
#         companies = f.read().splitlines()
#         for company in companies:
#             symbol = company.split(',')[0]
#             print(symbol)
#             data = yf.download(symbol, start="2023-01-01", end="2023-01-20")
            #data.to_csv('candle_stick_patterns/datasets/daily/{}.csv'.format(symbol))
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


        # print("*****Working*****")
        # for filename in datafiles:
        #     df = pd.read_csv("candle_stick_patterns/datasets/daily/{}".format(filename))
        #     #print(df)
        #     pattern_function=getattr(talib,pattern)
        #     symbol = filename.split('.')[0]


# data = yf.download("TMCI", start="2023-01-17", end="2023-01-20")
# print(data)


#*************Needed for read data and looping as string*******************
# df=pd.read_csv("candle_stick_patterns/pattern_analysis/consolidated_tickers_by_pattern/tickers_in_consolidated.csv",header=None)
# df.columns = ['date', 'pattern', 'ticker','pattern_descr','Trend']

# for index, row in df.iterrows():
#     print(row['ticker'],row['pattern_descr'])
#*************Needed for read data and looping as string*******************

def readdatafromcsvfiles(path,filenamewithextension):
    
    df = pd.read_csv(path+"{}".format(filenamewithextension))
    return df



# df=yf.download("symbol", start="2023-01-18", end="2023-01-19")
# df.to_csv('candle_stick_patterns/datasets/daily/{}.csv'.format(symbol))
import pandas as pd
datafiles=os.listdir('candle_stick_patterns/datasets/daily/')
df=pd.read_csv("candle_stick_patterns/pattern_analysis/consolidated_tickers_by_pattern/tickers_in_consolidated_copy.csv",header=None)
df.columns = ['date', 'pattern', 'ticker','pattern_descr','Trend']

# ****** Use when we read from csv file from local folder ********* #
# for l in chfolder:
    
#     # print("*******"+l+"*******")
#     # path=('candle_stick_patterns/patterns_analysis/{}/symbol.csv').format(l)
count=0
rslst=[]
for index, row in df.iterrows():
    symbol=row['ticker']
    ticker=symbol+'.csv'
    if symbol not in rslst: 
        rslst.append(symbol)

#print(rslst)


for filename in rslst:
    ticker=filename+'.csv'
    try:
      df = readdatafromcsvfiles("candle_stick_patterns/datasets/daily/",ticker)
      df2=df[df['Date']=='2023-01-19']
      print(filename)
      print(df2['Close'].iloc[0])

    except:
        pass


#print(datafiles)
#count=0
# for filename in datafiles:
#     df = readdatafromcsvfiles("candle_stick_patterns/datasets/daily/",filename)

#     symbol = filename.split('.')[0]