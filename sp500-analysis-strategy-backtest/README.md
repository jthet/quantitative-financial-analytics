# Financial Analysis of S&P 500 and Top Constituents

## Overview

This assignment involves a comprehensive analysis of the S&P 500 index and its top constituents to explore various statistical properties, correlations, and trading strategies. The object is a deep dive in financial data analysis through descriptive statistics, visualizations, and strategy backtesting.

For a the detailed analysis read the [write up](sp500-analysis-strategy-backtest-writeUp.pdf).
For the code and analysis look at the [jupyter notebook](sp500-analysis-strategy-backtest.ipynb)

## Objectives

1. **Data Analysis**:
   - Distribution analysis for daily price (close), daily volume, and net returns (daily, monthly, yearly).
   - Normality tests, including Shapiro-Wilk, Jarque-Bera, and Anderson-Darling.
   - Descriptive statistics: volatility, kurtosis, skewness.

2. **Volatility Analysis**:
   - Graphical exploration of volatility across different time scales (e.g., population, rolling 1-year, rolling 90-day).

3. **Risk/Reward Profile**:
   - Scatter plot of average daily return vs. standard deviation of daily returns for the S&P 500 and its top constituents.

4. **Correlation Analysis**:
   - Rolling monthly correlation between a selected constituent and the S&P 500.

5. **Kernel Density Estimation (KDE)**:
   - Analyze daily, monthly, and yearly return distributions for the S&P 500.

6. **Autocorrelation**:
   - Test for autocorrelation in net returns for selected constituents and the S&P 500.

7. **Trading Strategy Backtesting**:
   - Compare a Moving Average Crossover strategy to a Buy & Hold strategy.
   - Explore optimization techniques for strategy improvement.

## Deliverables

1. **Visualizations**:
   - Histograms, box plots, QQ plots for distributions.
   - Rolling volatility plots for multiple time scales.
   - Risk/reward scatter plot for top constituents.
   - Rolling correlation and autocorrelation plots.

2. **Metrics and Insights**:
   - Descriptive statistics for returns and volumes.
   - Correlation and volatility insights over time.
   - Comparative analysis of trading strategies.

3. **Code and Analysis**:
   - Python code for all computations and visualizations.
   - Comments and interpretations for each analysis section.

## Usage

The project includes Python scripts for replicating the analysis. Key libraries used include:
- `pandas` for data manipulation.
- `matplotlib` and `seaborn` for visualizations.
- `scipy.stats` and `statsmodels` for statistical tests.

## Notable Insights

- Distribution characteristics show significant skewness and kurtosis, deviating from normality.
- Rolling volatility smooths noise and reveals trends over different time scales.
- Buy & Hold consistently outperforms Moving Average Crossover in this analysis.
- Correlation and autocorrelation tests provide valuable insights into return dynamics.

## Conclusion

This analysis bridges statistical and financial perspectives, fostering skills in quantitative finance and data-driven decision-making.