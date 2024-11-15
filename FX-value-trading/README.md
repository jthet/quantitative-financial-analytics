# Systematic FX Trading Using PPP and Trend Analysis

## Project Overview

This project involves building a systematic FX trading strategy using Purchasing Power Parity (PPP) and trend-based indicators. The analysis focuses on G10 currency pairs and explores value-based and trend-following methodologies. The project spans data processing, backtesting, advanced modeling, and strategy evaluation.

## Objectives

1. **Data Analysis and Cleaning**:
   - Utilize IMF WEO, FRED, and Bloomberg data to construct a dataset of PPP values and economic indicators.
   - Address missing data issues and align data frequencies for consistency.

2. **Systematic Trading Rules**:
   - Create a PPP-based trading signal using deviations from theoretical exchange rates.
   - Develop advanced trading rules incorporating risk management techniques (e.g., volatility targeting, codified leverage).

3. **Trend-Based Indicators**:
   - Formulate a composite Trend-Value Indicator (TVI) using momentum, trend persistence, and price positioning.
   - Implement advanced trading rules based on TVI for enhanced performance.

4. **G10 Currency Universe**:
   - Expand the strategy to all G10 currency pairs, accounting for base currency variations.
   - Compare performance across currencies using equity curves.

5. **Logistic Regression Modeling**:
   - Transition from absolute thresholds to relative signals using logistic regression.
   - Generate long-short signals ranked by the strength of PPP deviations.

6. **New Metric Development**:
   - Design a composite value metric (NEO-XXXUSD) integrating PPP, real interest rates (RIR), and current account balances (CAB).
   - Evaluate robustness, cost, and capacity of the new metric.

## Methodology

1. **Data Sources**:
   - **IMF WEO**: PPP values and macroeconomic indicators.
   - **FRED**: Interest rates for G10 currencies.
   - **Bloomberg**: Spot exchange rates and additional economic data.

2. **Trading Strategies**:
   - Base PPP Strategy: Signals based on deviations from PPP.
   - Advanced Risk-Controlled Strategy: Incorporates volatility targeting and dynamic position sizing.

3. **Trend Analysis**:
   - Metrics: Momentum (14-day), trend persistence (30-day R-squared), and price positioning (200-day SMA).
   - Formula: \( TVI = w_1 \times Momentum + w_2 \times TrendPersistence + w_3 \times PricePosition \).

4. **G10 Currency Backtesting**:
   - Evaluate strategies across USD and non-USD base currencies.
   - Highlight Swiss Franc anomalies (e.g., 2015 shock).

5. **Logistic Regression**:
   - Model PPP deviations to rank signal strength.
   - Apply thresholds for top/bottom 20% of buy/sell signals.

6. **Composite Metric (NEO)**:
   - Formula: \( NEO = 0.33 \times PPP + 0.33 \times RIR + 0.34 \times CAB \).
   - Incorporates trade flows and investment attractiveness for robust currency valuation.

## Results and Insights

- **PPP Strategy**:
  - Stable but moderate performance over 24 years, outperforming buy-and-hold strategies.
  - Limited by annual data updates and single-factor reliance.

- **Trend-Based Strategy**:
  - Effective in capturing trends, particularly in volatile markets (e.g., USDNOK, EURUSD).
  - Less robust in range-bound markets or during economic shocks (e.g., USDCHF in 2015).

- **Advanced Metrics**:
  - NEO-XXXUSD demonstrates improved predictive power but varies by currency pair stability.
  - Highlights the importance of data quality and timely updates for metric effectiveness.

## Future Work

- Integrate additional indicators (e.g., inflation-adjusted indexes, forward-looking measures).
- Apply machine learning for dynamic weighting of composite metrics.
- Optimize strategies for cost efficiency and broader applicability.

## Conclusion

This Project demonstrates the value of systematic FX trading strategies using PPP and trend indicators. The project provides a foundation for further exploration of multi-factor models and adaptive methodologies in financial markets.