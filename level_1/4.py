import datetime
import time


def calculate_age(date_of_birth: datetime.date) -> int:
    today = time.localtime()
    return (today.tm_year - datetime.date(1965, 6, 2).year -
            ((today.tm_mon, today.tm_wday) < (date_of_birth.month, date_of_birth.day)))


if __name__ == "__main__":
    assert calculate_age(date_of_birth=datetime.date(1965, 6, 2)) == 58  # noqa: S101, PLR2004
