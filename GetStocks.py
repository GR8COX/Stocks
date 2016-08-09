import quandl
import CalculateRSI as rsi
import pandas
import csv
from datetime import date, timedelta

# API Key
quandl.ApiConfig.api_key = 'G47s_Q43P4LPhJa8QdEb'

# Start and Ending Dates for metrics
startDate = date.today() - timedelta(days=365)
endDate = date.today()

print("Gathering Stocks...")
# Stock list
# Import Stock List from CSV file
stockCodesCsv = pandas.read_csv('WIKI/WIKI-datasets-codes.csv')
stockList = stockCodesCsv['Code']

# TODO: Gather List of Stock Symbols
columns = "Stock, SevenRSI, FourteenRSI, TwentyOneRsi"
stockSellList = []
stockBuyList = []

print("Starting stock iteration...")
for x in stockList:
    stock = x
    # TODO: Iterate through each stock
    # Stock Metrics
    eodDataFrame = quandl.get(stock, start_date=str(startDate), end_date=str(endDate), collapse="daily")
    if not eodDataFrame.empty:
        stockPrice = eodDataFrame['Close']
        stockOpen = eodDataFrame['Open']
        stockHigh = eodDataFrame['High']
        stockLow = eodDataFrame['Low']
        # stockAssets = quandl.get("SF1/" + stock + "_ASSETS_ARQ.1", start_date=str(startDate), end_date=str(endDate))
        # stockLiability = quandl.get("SF1/" + stock + "_LIABILITIES_ARQ.1", start_date=str(startDate), end_date=str(endDate))
        # stockGrossIncome = quandl.get("SF1/" + stock + "_GP_ARQ.1", start_date=str(startDate), end_date=str(endDate))
        # stockNetIncome = quandl.get("SF1/" + stock + "_NETINC_ART.1", start_date=str(startDate), end_date=str(endDate))
        stockVolume = eodDataFrame['Volume']
        stockVolumeVariance = stockVolume.diff
        stockNetIncomePerEmployee = 1234

        # Compare Assets and Liability
        # latestAssetValue = stockAssets['Value'][-1]
        # latestLiabilityValue = stockLiability['Value'][-1]
        # asset_I = False
        # assetMargin = latestAssetValue - latestLiabilityValue

        # if assetMargin > 0:
        #    asset_I = True

        # Compare Gross and Net Income
        # latestGrossIncome = stockGrossIncome['Value'][-1]
        # latestNetIncome = stockNetIncome['Value'][-1]
        # netIncome_I = False
        # netIncomeMark = (latestNetIncome/latestGrossIncome)*100

        # if netIncomeMark > 10:
        #   netIncome_I = True

        # Retrieve RSI series

        twentyOneRSI = rsi.calculateRSI(eodDataFrame, 21)
        fourteenRSI = rsi.calculateRSI(eodDataFrame, 14)
        sevenRSI = rsi.calculateRSI(eodDataFrame, 7)

        # Change RSI sets into integers
        twentyOneRSI = tuple(twentyOneRSI)[0]
        fourteenRSI = tuple(fourteenRSI)[0]
        sevenRSI = tuple(sevenRSI)[0]

        # RSI Indicators
        twentyOneRSI_I = "Hold"
        fourteenRSI_I = "Hold"
        sevenRSI_I = "Hold"

        # RSI Checks
        if twentyOneRSI > 70:
            twentyOneRSI_I = "Sell"
        if twentyOneRSI < 30:
            twentyOneRSI_I = "Buy"

        if fourteenRSI > 70:
            fourteenRSI_I = "Sell"
        if twentyOneRSI < 30:
            fourteenRSI = "Buy"

        if sevenRSI > 70:
            sevenRSI_I = "Sell"
        if sevenRSI < 30:
            sevenRSI_I = "Buy"

        # Price Comparison
        yearlyChange = 1234
        monthlyChange = 1234
        averageMonthlyChange = 1234

        # Sell List
        if twentyOneRSI_I == "Sell" or fourteenRSI_I == "Sell" or sevenRSI_I == "Sell":
            stockSellSeries = pandas.Series([stock, sevenRSI, fourteenRSI, twentyOneRSI])
            stockSellList.append(stockSellSeries)

        # Buy List
        if twentyOneRSI_I == "Buy" or fourteenRSI_I == "Buy" or sevenRSI_I == "Buy":
            stockBuySeries = pandas.Series([stock, sevenRSI, fourteenRSI, twentyOneRSI])
            stockBuyList.append(stockBuySeries)


# TODO: write out buy and sell list
print("Building Dataframes...")
stockSellDataframe = pandas.DataFrame(stockSellList, index=date.today(), columns=columns)
stockBuyDataframe = pandas.DataFrame(stockBuyList, index=date.today(), columns=columns)
print("Saving Stock lists...")
stockSellDataframe.to_csv("StockSellList.csv", sep='\t', encoding='utf-8')
stockBuyDataframe.to_csv("StockBuyList.csv", sep='\t', encoding='utf-8')
print("Complete!")
