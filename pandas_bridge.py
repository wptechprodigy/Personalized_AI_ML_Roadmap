import pandas as pd


def run_pandas_bridge():
    print("\n--- Pandas Bridge: From Tables to Features ---")

    transactions = pd.DataFrame(
        {
            "transaction_id": ["tx_001", "tx_002", "tx_003", "tx_004", "tx_005"],
            "customer_id": ["c_01", "c_01", "c_02", "c_03", "c_02"],
            "amount": [25.0, 2500.0, 78.5, None, 420.0],
            "hour": [9, 2, 14, 23, 3],
            "merchant_type": ["grocery", "transfer", "restaurant", "electronics", "travel"],
        }
    )

    print("\n1. Raw DataFrame")
    print(transactions)

    print("\n2. Columns and shape")
    print(f"columns: {list(transactions.columns)}")
    print(f"shape: {transactions.shape}")

    print("\n3. Selecting columns")
    print(transactions[["transaction_id", "amount"]])

    print("\n4. Boolean filtering: high-value or late-night transactions")
    suspicious = transactions[(transactions["amount"].fillna(0) > 1000) | (transactions["hour"] < 4)]
    print(suspicious)

    print("\n5. Missing values")
    print(transactions.isna().sum())

    print("\n6. Simple feature engineering")
    enriched = transactions.copy()
    enriched["is_late_night"] = enriched["hour"] < 4
    enriched["amount_bucket"] = pd.cut(
        enriched["amount"],
        bins=[0, 100, 1000, float("inf")],
        labels=["small", "medium", "large"],
    )
    print(enriched[["transaction_id", "amount", "is_late_night", "amount_bucket"]])

    print("\n7. Grouping: customer spend")
    customer_spend = enriched.groupby("customer_id", dropna=False)["amount"].mean()
    print(customer_spend)

    print("\nINSIGHT: NumPy treats data as arrays. Pandas adds labels, tabular structure,")
    print("and filtering/grouping operations so you can audit real-world datasets quickly.")


if __name__ == "__main__":
    run_pandas_bridge()
