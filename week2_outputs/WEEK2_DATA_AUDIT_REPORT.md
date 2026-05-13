# Week 2 Data Audit Report

- Rows audited: 5000
- Data health score: 25/100
- Missing amount values: 17
- Negative amounts detected: 17
- IQR-based amount outliers: 418
- Late-night transactions: 1094

## Missing Values by Column
transaction_id       0
amount              17
hour                 0
account_age_days     0
txn_count_24h        0
merchant_type        0

## Numeric Correlations
                  amount   hour  account_age_days  txn_count_24h
amount             1.000  0.009            -0.028         -0.009
hour               0.009  1.000             0.000          0.010
account_age_days  -0.028  0.000             1.000         -0.008
txn_count_24h     -0.009  0.010            -0.008          1.000

## Takeaways
- Real-world data fails before models fail. Missing values, invalid amounts, and long-tail distributions distort learning.
- Pandas is the fastest way to inspect tabular failure modes before spending time on modeling.
- This audit creates the baseline for Week 3 feature engineering and fraud modeling.