from email_validate import validate  # mypy error: Skipping analyzing "email_validate": module is installed, but missing


def is_correct_email(raw_email: str) -> bool:
    return bool(validate(raw_email))


if __name__ == '__main__':
    assert is_correct_email(raw_email='test@gmail.co') is False  # noqa: S101
