def is_correct_int(raw_int: str | None) -> bool:
    if not raw_int:
        return False
    return raw_int.isalnum()


if __name__ == '__main__':
    assert is_correct_int(raw_int='12') is True  # noqa: S101
    assert is_correct_int(raw_int='12&') is False  # noqa: S101
    assert is_correct_int(raw_int=None) is False  # noqa: S101
