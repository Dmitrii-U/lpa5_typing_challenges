def is_loan_amount_too_big(loan_amount_usd: int, max_loan_amount_for_user_usd: int | None) -> bool:
    if max_loan_amount_for_user_usd:
        return loan_amount_usd > max_loan_amount_for_user_usd
    return False


if __name__ == '__main__':
    assert is_loan_amount_too_big(loan_amount_usd=1000, max_loan_amount_for_user_usd=4000) is False  # noqa: S101
    assert is_loan_amount_too_big(loan_amount_usd=1000, max_loan_amount_for_user_usd=None) is False  # noqa: S101
