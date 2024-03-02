<<<<<<< HEAD
||||||| parent of b572976 (level_1)
from constants import ___
=======
# from constants import ___
>>>>>>> b572976 (level_1)
from email_validate import validate  # mypy error: Skipping analyzing "email_validate": module is installed, but missing
# library stubs or py.typed marker  [import-untyped] хотя в настройках указано ignore_missing_imports = true


def is_correct_email(raw_email: str) -> bool:
<<<<<<< HEAD
    return bool(validate(raw_email))
||||||| parent of b572976 (level_1)
def is_correct_email(raw_email: ___) -> ___:
    pass
=======
    return validate(raw_email)
>>>>>>> b572976 (level_1)


if __name__ == '__main__':
    assert is_correct_email(raw_email='test@gmail.co') is False  # noqa: S101
