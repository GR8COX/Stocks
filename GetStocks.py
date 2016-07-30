import quandl
import CalculateRSI as rsi
import pandas
from datetime import date, timedelta


# API Key
quandl.ApiConfig.api_key = 'G47s_Q43P4LPhJa8QdEb'

# Start and Ending Dates for metrics
startDate = date.today() - timedelta(days=365)
endDate = date.today()

# Stock list
# TODO: Gather List of Stocks
stock = "FB"

# TODO: Iterate through each stock

# Stock Metrics
eodDataFrame = quandl.get("WIKI/" + stock, start_date=str(startDate), end_date=str(endDate), collapse="daily")
stockPrice = eodDataFrame['Close']
stockOpen = eodDataFrame['Open']
stockHigh = eodDataFrame['HIgh']
stockLow = eodDataFrame['Low']
stockAssets = quandl.get("SF1/" + stock + "_ASSETS_ARQ.1", start_date=str(startDate), end_date=str(endDate))
stockLiability = quandl.get("SF1/" + stock + "_LIABILITIES_ARQ.1", start_date=str(startDate), end_date=str(endDate))
stockGrossIncome = quandl.get("SF1/" + stock + "_GP_ARQ.1", start_date=str(startDate), end_date=str(endDate))
stockNetIncome = quandl.get("SF1/" + stock + "_NETINC_ART.1", start_date=str(startDate), end_date=str(endDate))
stockVolume = eodDataFrame['Volume']
    #quandl.get("EOD/" + stock + ".5", start_date=str(startDate), end_date=str(endDate), collapse="daily")
stockVolumeVariance = 1234
stockNetIncomePerEmployee = 1234

# Compare Assets and Liability
print(stockAssets.tail(1))
print(stockLiability.tail(1))




# Graph RSI
#twentyoneRSI = rsi.calculateRSI(stockPrice, 21)
#fourteenRSI = rsi.calculateRSI(stockPrice, 14)
#sevenRSI = rsi.calculateRSI(stockPrice, 7)

#print(stockData)
#print(stockAssets)

