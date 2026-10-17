from PIL.ImageCms import profileToProfile
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import datetime as dt 
import yfinance as yf


# Simulation Settings
initialInvestment = 10_000
numDays = 252
numSimulations = 1_000

# import data
def get_data(stocks, start, end):
    stockData = yf.download(stocks, start=start, end=end, auto_adjust=True)
    stockData = stockData['Close']
    returns = stockData.pct_change().dropna()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix

stockList = ['AAPL', 'MSFT', 'NVDA', 'AMZN', 'JPM', 'KO']
stocks = [stock for stock in stockList]
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=300)

meanReturns, covMatrix = get_data(stocks, startDate, endDate)

weights = np.full(len(meanReturns), 1 / len(meanReturns))

covMatrix = covMatrix.loc[meanReturns.index, meanReturns.index]

rng = np.random.default_rng(42)

portfolioPaths = np.zeros((numDays + 1, numSimulations))
portfolioPaths[0, :] = initialInvestment

for simulation in range(numSimulations):
    dailyStockReturns = rng.multivariate_normal(
        mean=meanReturns.to_numpy(),
        cov=covMatrix.to_numpy(),
        size=numDays
    )
    dailyPortfolioReturns = dailyStockReturns @ weights
    portfolioPaths[1:, simulation] = (
        initialInvestment * np.cumprod(1 + dailyPortfolioReturns)
    )

plt.figure(figsize=(12, 6))
plt.plot(portfolioPaths, alpha=0.1, linewidth=0.7)
plt.axhline(
    initialInvestment,
    color="black",
    linestyle="--",
    label="Initial Investment"
)

plt.title("Monte Carlo Portfolio Simulator")
plt.xlabel("Trading Days")
plt.ylabel("Portfolio Value ($)")
plt.legend()
plt.show()

finalValues = portfolioPaths[-1, :]

print(f"Mean final value: ${np.mean(finalValues):,.2f}")
print(f"Median final value: ${np.median(finalValues):,.2f}")
print(f"5th percentile: ${np.percentile(finalValues, 5):,.2f}")
print(f"95th percentile: ${np.percentile(finalValues, 95):,.2f}")
print(
    f"Simulated probability of a loss: "
    f"{np.mean(finalValues < initialInvestment):.1%}"
)