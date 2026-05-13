# Personalized AI/ML Learning Roadmap 🚀

This repository tracks my journey from **Senior iOS Engineer** to **AI Product Engineer**. Leveraging my background in Physics and FinTech, I am following a 6-8 month intensive roadmap focused on the **Five Laws of Learning** and the **Offer Framework**.

## 🎯 Target Role
**AI Product Engineer** (Full-stack + ML Integration)

## 🏗 Week 1: Foundations & The ML Bridge
In my first week, I focused on porting my mathematical foundations into high-performance Python code, specifically optimized for **Apple Silicon (M1 Pro)**.

### Key Technical Achievements:
- **Hardware Benchmarking:** Verified a **122.7x speedup** by transitioning from iterative loops to **NumPy Vectorization**.
- **Normal Equation:** Implemented the analytical solution for Linear Regression ($\theta = (X^T X)^{-1} X^T y$) from scratch.
- **NumPy Core:** Mastered Broadcasting, Memory Views, and SIMD operations.

### Performance Audit (M1 Pro):
| Operation (1M Points) | Time (s) |
| :--- | :--- |
| Iterative Loop | 0.6017s |
| **Vectorized (NumPy)** | **0.0049s** |

## 📂 Repository Structure
- `WeekOne/`: Week 1 scripts and report for vectorization, NumPy, and linear regression foundations.
- `WeekTwo/`: Week 2 scripts, report, and audit outputs for Pandas and data triage.
- `ROADMAP_PROGRESS.md`: Live tracking of the roadmap and weekly milestones.
- `README.md`: Overview of the roadmap, structure, and execution commands.

### WeekOne Contents
- `WeekOne/vectorization_test.py`
- `WeekOne/linear_regression_scratch.py`
- `WeekOne/numpy_bridge.py`
- `WeekOne/WEEK1_TECHNICAL_REPORT.md`

### WeekTwo Contents
- `WeekTwo/pandas_bridge.py`
- `WeekTwo/fintech_data_audit.py`
- `WeekTwo/WEEK2_TECHNICAL_REPORT.md`
- `WeekTwo/week2_outputs/WEEK2_DATA_AUDIT_REPORT.md`
- `WeekTwo/week2_outputs/amount_distribution.png`
- `WeekTwo/week2_outputs/transactions_by_hour.png`

## 🧭 Week 2: Data Triage & Statistical Audit
Week 2 moves from clean mathematical examples to messy tabular data.

### Week 2 Goals:
- Learn the 20% of Pandas needed for ML work: filtering, null handling, grouping, and feature creation.
- Audit a realistic FinTech-style dataset for missing values, negative amounts, outliers, and late-night activity.
- Generate a repeatable report and charts before moving into modeling.

### Week 2 Commands:
```bash
python WeekTwo/pandas_bridge.py
python WeekTwo/fintech_data_audit.py
```

### Week 1 Commands:
```bash
python WeekOne/vectorization_test.py
python WeekOne/linear_regression_scratch.py
python WeekOne/numpy_bridge.py
```

## 🛠 Tech Stack
- **Languages:** Python 3.11+, Swift
- **Environment:** Miniforge (Conda), Apple Silicon (MPS)
- **Libraries:** NumPy, Pandas, Matplotlib

---
*Follow my journey as I build production-grade AI systems at age 46, proving that architectural maturity is the ultimate differentiator in ML.*
