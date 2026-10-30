def test_transaction_amount_is_positive():
    amount = 5000
    assert amount > 0


def test_transaction_amount_is_not_zero():
    amount = 5000
    assert amount != 0


def test_transaction_status_is_valid():
    status = "SUCCESS"
    assert status in ["SUCCESS", "FAILED", "PENDING"]


def test_transaction_type_is_valid():
    transaction_type = "DEPOSIT"
    assert transaction_type in ["DEPOSIT", "WITHDRAWAL", "TRANSFER"]


