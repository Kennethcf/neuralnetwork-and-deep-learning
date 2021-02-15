#fix all the bugs use DNA for source code 
import DNA 



#this this the main funcition of DNA(find it on github.com/kennethcf)
#this is a demonstration for nuralnetwork and deeplearning
#it takes 7 steps before a decision is made on two conditions condition variable m stands for market saying it goes on "p" or "n"these variables are set in getticker funtion line 12

if __name__ == "__main__":
    global k 
    records = {}
    gettickers()
    k = kite.instruments(exchange="NSE")

    w = 0
    new = {}
    p = pandas.DataFrame(new)
    l = 0
    for i in tickers:
        getdata(ticker =i,frame = "15minute", dates=0)
        day = data
        getdata(ticker=i,frame="5minute",dates=10)

        EMA("close",200)
        macd()
        EMA("close",50)
        TRIX()
        RSI()
        today = kite.ohlc(256265)
        intra = ((today[str(256265)]["last_price"]-today[str(256265)]["ohlc"]["open"] )/today[str(256265)]["ohlc"]["open"])*100
        data.drop(range(200))
        print(m)
        if m == "p":
            if data["macd"][len(data)-1] > 0 and data["macd"][len(data)-1] < 25 and data["ml"][len(data)-1] > data["macd"][len(data)-1]  :
                print(1)
                if data["close"][len(data)-1] > data["EMA200"][len(data)-1]:
                    print(2)
                    if data["close"][len(data)-1] > data["EMA50"][len(data)-1]:
                        print(3)
                        if data["TRIX"][len(data)-1] > 0 and data["TRIX"][len(data)-2] < data["TRIX"][len(data)-1] :
                            print(5)
                            if data["RSI20"][len(data)-1] > 56 :
                                print(6)
                                if day["high"][0] < 300:
                                    buy(shortlist[w],day["high"][0] + 0.05)
                                else:
                                    buy(shortlist[w],day["high"][0] + 0.1)
        if m == "n":
            if data["macd"][len(data)-1] < 0 and data["macd"][len(data)-1] > -25 and data["ml"][len(data)-1] < data["macd"][len(data)-1]  :
                print(1)
                if data["close"][len(data)-1] < data["EMA200"][len(data)-1]:
                    print(2)
                    if data["close"][len(data)-1] < data["EMA50"][len(data)-1]:
                        print(3)
                        if data["TRIX"][len(data)-1] < 0 and data["TRIX"][len(data)-2] > data["TRIX"][len(data)-1] :
                            print(5)
                            if data["RSI20"][len(data)-1] < 56 :
                                print(6)
                                if day["high"][0] < 300:
                                    buy(shortlist[w],day["low"][0] + 0.05)
                                else:
                                    buy(shortlist[w],day["low"][0] + 0.1)
        w  =  w + 1 



#all neuralnetworks are sum of loops and condition <<pro tip>>

