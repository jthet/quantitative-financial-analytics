# Predicting Federal Interest Rates and Recession Status

## Overview

This project explores macroeconomic trends to analyze the Federal Funds Effective Rate (FEDFUNDS) and predict future interest rate decisions and recession status. The analysis employs a variety of statistical and machine learning techniques to derive meaningful insights from historical economic data.

## Objectives

1. **Data Analysis**:
   - Investigate relationships between key economic indicators (e.g., inflation, unemployment, GDP) and the Federal Funds Rate.
   - Perform descriptive statistics to summarize economic variables.

2. **Visualization**:
   - Create time-series plots and histograms to examine patterns in interest rate changes.
   - Cross-correlation plots to identify lead-lag relationships between economic indicators and FEDFUNDS.

3. **Modeling**:
   - Build linear and nonlinear regression models to predict the size of rate hikes/cuts.
   - Create classification models to determine recession status and predict future economic conditions (1, 3, and 6 months).

4. **Economic Insights**:
   - Assess the current state of the U.S. economy and argue for specific policy actions at the next Federal Reserve meeting.

## Data Sources

1. **Federal Reserve Economic Data (FRED)**:
   - Inflation Rate (`CORESTICKM159SFRBATL`)
   - GDP (`GDP`)
   - Unemployment Rate (`UNRATE`)
   - Federal Funds Effective Rate (`FEDFUNDS`)
   - Consumer Sentiment (`UMCSENT`)
   - Composite Leading Indicator (`USALOLITONOSTSAM`)
   - Yield Curve: 10-Year Treasury Minus 3-Month Treasury (`T10Y3MM`)
   - Coincident Indicators (`BBKMCOIX`)
   - Lagging Indicators (`M16005USM358SNBR`)
   - Recession Indicator (`USREC`)

2. **The Conference Board**:
   - Leading, lagging, and coincident indices.

3. **National Bureau of Economic Research (NBER)**:
   - Recession dates.

## Methodology

### Data Preparation
- Consolidated multiple datasets using `fredapi` and ensured consistent time alignment.
- Calculated percentage changes for key indicators to analyze trends over time.
- Merged data using inner joins to eliminate missing values and ensure clean data.

### Analysis and Visualization
- Applied descriptive statistics and cross-correlation analysis to study indicator relationships.
- Created visualizations to compare trends during rate hike and cut events.

### Predictive Modeling
1. **Regression Models**:
   - Linear and nonlinear regression models trained to predict rate hikes/cuts.
   - Metrics: R-squared and Mean Squared Error (MSE) to evaluate model performance.

2. **Classification Models**:
   - Models include Random Forest, Naive Bayes, and K-Nearest Neighbors.
   - Predicted recession status for current and future timeframes (1, 3, and 6 months).

### Key Insights
- Inflation and unemployment show lead-lag relationships with FEDFUNDS.
- Yield curve inversions strongly correlate with economic slowdowns.
- Machine learning models suggest a high likelihood of maintaining or lowering interest rates in the next meeting.

## Results

1. **Regression Models**:
   - Linear Model: R-squared of 0.903.
   - Nonlinear Model: R-squared of 0.953.
   - Predictions: Significant rate cuts expected in a slowing economy.

2. **Classification Models**:
   - Current recession prediction: Economy is not in recession.
   - Future predictions: Increasing uncertainty for 3- and 6-month forecasts.

## Conclusion

This project demonstrates the application of statistical and machine learning techniques to analyze complex economic phenomena. The results provide actionable insights for monetary policy decisions and forecasting economic conditions. While models perform well in controlled scenarios, external shocks and data limitations remain challenges for accurate predictions.
