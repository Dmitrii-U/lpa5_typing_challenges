UserDataTuple = tuple[str, int, list[int]]


def calculate_total_spent_for_user(user: UserDataTuple) -> int:
    return sum(user[2])


if __name__ == '__main__':
    assert calculate_total_spent_for_user(user=('Ilya', 32, [102, 15, 63, 12])) == 192  # noqa: S101, PLR2004
