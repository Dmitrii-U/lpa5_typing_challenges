def is_recovery_code_correct(code: str, user_codes: list[str]) -> bool:
    return code in user_codes


if __name__ == '__main__':
    assert is_recovery_code_correct(code='5212', user_codes=['1862', '8172', '7212']) is False  # noqa: S101
