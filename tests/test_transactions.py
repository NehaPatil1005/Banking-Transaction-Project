
import pandas as pd
from src.etl_pipeline import validate_transactions


def test_valid_transaction_is_accepted():
    df = pd.DataFrame({
        "transaction_id": ["T1001"],
        "customer_id": ["C101"],
        "transaction_type": ["DEPOSIT"],
        "amount": [5000],
        "transaction_date": ["2026-10-28"],
        "status": ["SUCCESS"]
    })

    valid_df, rejected_df = validate_transactions(df)

    assert len(valid_df) == 1
    assert len(rejected_df) == 0


def test_negative_amount_is_rejected():
    df = pd.DataFrame({
        "transaction_id": ["T1002"],
        "customer_id": ["C102"],
        "transaction_type": ["WITHDRAWAL"],
        "amount": [-200],
        "transaction_date": ["2026-10-28"],
        "status": ["SUCCESS"]
    })

    valid_df, rejected_df = validate_transactions(df)

    assert len(valid_df) == 0
    assert len(rejected_df) == 1


def test_duplicate_transaction_is_rejected():
    df = pd.DataFrame({
        "transaction_id": ["T1003", "T1003"],
        "customer_id": ["C101", "C101"],
        "transaction_type": ["DEPOSIT", "DEPOSIT"],
        "amount": [1000, 2000],
        "transaction_date": ["2026-10-28", "2026-10-28"],
        "status": ["SUCCESS", "SUCCESS"]
    })

    valid_df, rejected_df = validate_transactions(df)

    assert len(valid_df) == 1
    assert len(rejected_df) == 1
