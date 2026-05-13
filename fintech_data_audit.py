from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


OUTPUT_DIR = Path("week2_outputs")


def build_synthetic_dataset(size=5000, seed=42):
    rng = np.random.default_rng(seed)

    amounts = rng.lognormal(mean=3.7, sigma=1.0, size=size)
    hours = rng.integers(0, 24, size=size)
    account_age_days = rng.integers(5, 3650, size=size)
    txn_count_24h = rng.poisson(lam=3.5, size=size)
    merchant_types = rng.choice(
        ["grocery", "travel", "electronics", "transfer", "health", "education"],
        size=size,
        p=[0.28, 0.1, 0.14, 0.16, 0.18, 0.14],
    )

    dataframe = pd.DataFrame(
        {
            "transaction_id": [f"tx_{index:05d}" for index in range(size)],
            "amount": amounts.round(2),
            "hour": hours,
            "account_age_days": account_age_days,
            "txn_count_24h": txn_count_24h,
            "merchant_type": merchant_types,
        }
    )

    anomaly_count = max(8, size // 100)
    anomaly_rows = rng.choice(dataframe.index, size=anomaly_count, replace=False)
    dataframe.loc[anomaly_rows[: anomaly_count // 3], "amount"] *= 80
    dataframe.loc[anomaly_rows[anomaly_count // 3 : 2 * anomaly_count // 3], "amount"] = -25
    dataframe.loc[anomaly_rows[2 * anomaly_count // 3 :], "amount"] = np.nan

    return dataframe


def audit_dataset(dataframe):
    missing_counts = dataframe.isna().sum()
    numeric_frame = dataframe.select_dtypes(include=[np.number])

    negative_amounts = int((dataframe["amount"] < 0).fillna(False).sum())
    missing_amounts = int(dataframe["amount"].isna().sum())
    late_night = int(((dataframe["hour"] < 4) | (dataframe["hour"] > 22)).sum())

    q1 = dataframe["amount"].quantile(0.25)
    q3 = dataframe["amount"].quantile(0.75)
    iqr = q3 - q1
    outlier_mask = (dataframe["amount"] < (q1 - 1.5 * iqr)) | (dataframe["amount"] > (q3 + 1.5 * iqr))
    outlier_count = int(outlier_mask.fillna(False).sum())

    health_score = 100
    health_score -= min(missing_amounts * 2, 25)
    health_score -= min(negative_amounts * 3, 30)
    health_score -= min(outlier_count // 20, 20)
    health_score = max(0, health_score)

    return {
        "rows": len(dataframe),
        "missing_counts": missing_counts,
        "negative_amounts": negative_amounts,
        "missing_amounts": missing_amounts,
        "late_night_transactions": late_night,
        "outlier_count": outlier_count,
        "health_score": health_score,
        "correlations": numeric_frame.corr(numeric_only=True),
    }


def save_visuals(dataframe):
    OUTPUT_DIR.mkdir(exist_ok=True)

    plt.figure(figsize=(9, 5))
    dataframe["amount"].dropna().clip(upper=dataframe["amount"].dropna().quantile(0.99)).hist(bins=40)
    plt.title("Transaction Amount Distribution (Capped at 99th Percentile)")
    plt.xlabel("Amount")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "amount_distribution.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    dataframe["hour"].value_counts().sort_index().plot(kind="bar")
    plt.title("Transaction Volume by Hour")
    plt.xlabel("Hour")
    plt.ylabel("Transactions")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "transactions_by_hour.png")
    plt.close()


def write_report(results):
    lines = [
        "# Week 2 Data Audit Report",
        "",
        f"- Rows audited: {results['rows']}",
        f"- Data health score: {results['health_score']}/100",
        f"- Missing amount values: {results['missing_amounts']}",
        f"- Negative amounts detected: {results['negative_amounts']}",
        f"- IQR-based amount outliers: {results['outlier_count']}",
        f"- Late-night transactions: {results['late_night_transactions']}",
        "",
        "## Missing Values by Column",
        results["missing_counts"].to_string(),
        "",
        "## Numeric Correlations",
        results["correlations"].round(3).to_string(),
        "",
        "## Takeaways",
        "- Real-world data fails before models fail. Missing values, invalid amounts, and long-tail distributions distort learning.",
        "- Pandas is the fastest way to inspect tabular failure modes before spending time on modeling.",
        "- This audit creates the baseline for Week 3 feature engineering and fraud modeling.",
    ]

    report_path = OUTPUT_DIR / "WEEK2_DATA_AUDIT_REPORT.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def main():
    print("\n--- Week 2: FinTech Data Audit ---")
    dataset = build_synthetic_dataset()
    results = audit_dataset(dataset)
    save_visuals(dataset)
    report_path = write_report(results)

    print(f"Rows audited: {results['rows']}")
    print(f"Health score: {results['health_score']}/100")
    print(f"Missing amount values: {results['missing_amounts']}")
    print(f"Negative amounts: {results['negative_amounts']}")
    print(f"Outlier count: {results['outlier_count']}")
    print(f"Late-night transactions: {results['late_night_transactions']}")
    print(f"Report written to: {report_path}")
    print(f"Charts saved to: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
