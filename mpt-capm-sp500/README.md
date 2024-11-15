# README: Modern Portfolio Theory & CAPM (and Fama French) Analysis

## Overview

This homework investigates the relationships between asset returns, market factors, and portfolio optimization using the Capital Asset Pricing Model (CAPM), Fama-French (FF) models, and Modern Portfolio Theory (MPT). The assignment applies both traditional and advanced statistical techniques to analyze stock behavior and portfolio efficiency.

## Objectives

1. **CAPM and Fama-French Models**:
   - Compute CAPM and FF 3-Factor model coefficients for 10 selected S&P 500 companies.
   - Examine the significance and relevance of Beta for each stock.

2. **Time-Varying Beta Analysis**:
   - Compute and plot rolling one-year betas for a selected stock from 2000 to the present.

3. **Factor Derivations and Maintenance**:
   - Summarize the derivations and periodic updates of the Fama-French factors.

4. **Model Enhancements**:
   - Propose and implement a methodology to modernize the FF model.

5. **Portfolio Optimization**:
   - Calculate the efficient frontier and identify the tangent portfolio using the top 10 S&P 500 companies.
   - Compute and report optimal portfolio weights.

6. **Advanced Regression Techniques**:
   - Use lasso, ridge, and elastic net regression to analyze CAPM and FF models.
   - Compare and discuss the appropriateness of these approaches.

## Data Sources

1. **Fama-French Data**:
   - *F-F_Research_Data_Factors_daily.CSV*: Daily factors for market excess returns, SMB, HML, RMW, and CMA.
   - Fama-French Data Library: [Fama-French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp).

2. **Stock Price Data**:
   - Homework 2 data.xlsx containing daily stock prices for selected companies.

3. **Risk-Free Rate**:
   - Daily returns derived from Treasury bill data in the Fama-French dataset.

## Methodology

### CAPM and Fama-French Models
- Calculated percent returns for the selected stocks.
- Conducted linear regressions to estimate Alpha and Beta coefficients under CAPM and FF models.
- Reported results with t-statistics to assess coefficient significance.

### Rolling Beta Analysis
- Computed one-year rolling betas using 252 trading-day windows.
- Plotted the evolution of beta coefficients over time for a selected stock.

### Efficient Frontier
- Used Monte Carlo simulations (100,000 portfolios) to compute the efficient frontier.
- Optimized weights for the tangent portfolio by maximizing the Sharpe ratio.
- The risk-free rate was calculated as the average daily T-Bill return over the past two years.

### Advanced Regression
- Implemented lasso, ridge, and elastic net regressions to explore factor significance.
- Evaluated the performance and dimensionality reduction capabilities of each regression technique.

## Results

1. **CAPM and FF Coefficients**:
   - Highlighted market sensitivities (Mkt-RF) and factor contributions (SMB, HML).
   - Beta relevance: Growth-oriented stocks (e.g., NVDA) exhibited higher volatility and significant negative HML coefficients.

2. **Rolling Beta Trends**:
   - Time-varying beta patterns reveal shifts in market, size, and value sensitivities over decades.

3. **Portfolio Optimization**:
   - Optimal portfolio weights emphasize high-growth and stable-value stocks.
   - Tangent portfolio achieved maximum Sharpe ratio with a 0.0187% risk-free rate.

4. **Regression Insights**:
   - Lasso and elastic net highlighted the insignificance of SMB for large-cap stocks.
   - Ridge regression reduced coefficients proportionally without nullifying factors.

## Conclusion

This analysis provided insights into the dynamics of market factors and their implications for asset returns and portfolio construction. The application of advanced regression methods and portfolio theory demonstrates practical approaches to optimizing investment strategies while addressing theoretical considerations.