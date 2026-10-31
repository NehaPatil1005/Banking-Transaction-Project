
import pandas as pd


def validate_transactions(df):
    # Identify duplicate transaction IDs
    duplicate_ids = df["transaction_id"].duplicated(keep="first")

    # Check positive transaction amounts
    valid_amounts = df["amount"] > 0

    # Separate valid and rejected records
    valid_df = df[~duplicate_ids & valid_amounts].copy()
    rejected_df = df[duplicate_ids | ~valid_amounts].copy()

    return valid_df, rejected_df


def run_pipeline():
    # Extract
    df = pd.read_csv("data/raw/transactions.csv")
    print("Raw records:", len(df))

    # Transform
    valid_df, rejected_df = validate_transactions(df)

    # Load
    valid_df.to_csv("data/processed/valid_transactions.csv", index=False)
    rejected_df.to_csv("data/rejected/rejected_transactions.csv", index=False)

    print("Valid records:", len(valid_df))
    print("Rejected records:", len(rejected_df))
    print("ETL pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()
