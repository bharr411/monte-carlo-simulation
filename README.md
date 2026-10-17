# Monte Carlo Portfolio simulation
A python project used for simulating possible future values of a stock portfolio using historical daily returns and covariance.
I built this project to learn about vectorisation, numpy & pandas syntax, portfolio risk and utilising financial data in python.

## What it does
The program: 
  - Downloads historical prices using finance.
  - Calculates average daily returns and the covariance matrix.
  - Generates correlated random daily returns using seed 42 for reproducibility.
  - Simulates 1,000 Portfolio paths over the span of 252 trading days.
  - plots the paths and reports summary statistics.
  The provided project uses 6 example tickers ['AAPL', 'MSFT', 'NVDA', 'AMZN', 'JPM', 'KO'] with an equal weighting of 16.667% share allocation.

## Defaults 
|  Setting  |  Value  |
|  -------  | ------  |
| Initial Investment | $10,000 USD |
| Number of Simulations | 1,000 |
| Simulation Horizons | 252 Trading days |
| Historical Data window | Previous 300 Calendar days |
| Portfolio Allocation | Equal Weights |
| Random Seed | 42 |

## How it works
Historical prices are converted into daily percentage returns. Their average returns and covariance matrix are used to generate simulated returns from a multivariate normal distribution.
For each simulated day, stock returns are combined using portfolio weights. Portfolio values are then calculated by compounding these daily returns:
Portfolio value today = portfolio value yesterday * (1 + daily portfolio return)
For example with a portfolio with $10,000 of capital at a 2% daily RR,
$10,000 * 1.02 = $10,200.

This process is repeated to produce a range of possible portfolio paths.

## Installation and Usage

You need python3 and an internet connection to download market data.

Install the required packages:

```bash
python3 -m pip install pandas numpy matplotlib finance
```

```bash
python3 "Monte Carlo.py"
```

The program displays a chart. After you close the chart the summary stats are shown in terminal.

## Results

The program reports:
  - Mean final portfolio value
  - Median final portfolio value
  - 5th percentile final portfolio value
  - 95th percentile final portfolio value
  - Proportion of simulations ending below the initial investment.

For example a simulated loss probability of 6% means that approximately 6% of the generated paths finished below initial investment.

## Assumptions and limitations
  - Historical average returns and covariance are assumed to remain constant over the simulation horizon
  - Daily return vectors are drawn independently from a multivariate normal distribution
  - Portfolio weights remain constant, implying daily rebalancing.
  - Trading costs, taxes and inflation are excluded.
  - Results are sensitive to the historical period used to estimate the inputs.
  - Normally distributed simple returns can theoretically fall below -100%, making this a simplified model.
  - The simulation does not account for uncertainty in the estimated means and covariance.

The results describe outcomes under these assumptions, therefore not a reliable estimate of true probability of future investments.

## Planned improvements
- Compare results across different historical data windows.
- Add a histogram of final portfolio values.
- Measure maximum drawdown along each path.
- Compare daily rebalancing with buy-and-hold.
- Explore log-return models and historical bootstrapping.
- Process simulations in batches for larger experiments.
