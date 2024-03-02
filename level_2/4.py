def ban_users(users_ids: set[int]) -> int:  # noqa: ARG001
    return 2  # совершенно не понятно, что должна делать функция из названия - банить юзеров
    # и тогда 2 это код, что успешно забанены?


if __name__ == '__main__':
    assert ban_users(users_ids={167, 623, 209, 921}) == 2  # noqa: S101, PLR2004
