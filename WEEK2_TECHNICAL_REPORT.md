# Week 2 Technical Report: Data Triage Before Modeling
**Date:** May 2026
**Engineer:** [Your Name]
**Focus:** Pandas foundations, failure-mode detection, and FinTech data integrity

## 1. Executive Summary
Week 2 shifted the roadmap from clean mathematical examples to tabular production data. The primary objective was to learn the minimum useful Pandas needed for ML work and to validate a FinTech-style dataset before any modeling work begins.

This phase reinforced a core engineering truth: **models usually fail after the data has already failed**. Before optimizing algorithms, I need reliable habits for auditing nulls, invalid values, long-tail distributions, and suspicious slices of activity.

## 2. Pandas as the Bridge from Arrays to Tables
NumPy gave me performance and matrix thinking. Pandas adds labels, grouping, and filtering so the same discipline can be applied to real business records.

Key concepts covered:
- **Column selection:** isolating high-signal variables such as `amount`, `hour`, and `merchant_type`
- **Boolean filtering:** extracting suspicious rows like late-night or unusually large transactions
- **Missing value inspection:** checking null density before downstream modeling
- **Grouping:** aggregating customer-level behavior from raw transaction rows
- **Simple feature engineering:** turning raw columns into useful signals such as `is_late_night`

## 3. FinTech Audit Findings
I generated and audited a realistic synthetic FinTech dataset with **5,000 transactions**.

### Audit Summary
- **Rows audited:** 5,000
- **Data health score:** 25/100
- **Missing amount values:** 17
- **Negative amounts detected:** 17
- **IQR-based amount outliers:** 418
- **Late-night transactions:** 1,094

### Interpretation
- The low health score is intentional. It simulates the kind of noisy, failure-prone data common in production systems.
- The long-tail amount distribution shows why averages alone are misleading in financial datasets.
- The late-night transaction volume demonstrates why time-based features will likely matter in future fraud modeling.
- Negative and missing amounts are data-quality failures that should be handled before training any model.

## 4. Senior Engineering Takeaway
The value of Week 2 is not “knowing Pandas.” The value is learning to inspect data like a production engineer.

In a FinTech environment, a model can appear correct while still being built on invalid assumptions:
- missing values silently bias feature distributions
- extreme outliers dominate gradients and thresholds
- schema mistakes distort downstream analytics
- poor data hygiene wastes compute and reduces trust in the system

This is where product engineering matters. Before asking whether a model is accurate, I need to ask whether the input stream is trustworthy.

## 5. Output Assets
Week 2 produced the following proof assets:
- `pandas_bridge.py`
- `fintech_data_audit.py`
- `week2_outputs/WEEK2_DATA_AUDIT_REPORT.md`
- `week2_outputs/amount_distribution.png`
- `week2_outputs/transactions_by_hour.png`

## 6. Conclusion
Week 2 established the practical data-triage habits required before moving into feature engineering and classification. This closes the gap between mathematical readiness and production readiness.

---
**Status:** WEEK 2 COMPLETE ✅
**Next Milestone:** Feature Engineering and baseline fraud classification
