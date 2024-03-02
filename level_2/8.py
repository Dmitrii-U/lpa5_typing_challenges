UserDataTuple = tuple[str, int, list[int]]


def calculate_total_spent_for_users(
    users_ids: set[int], users_ids_to_users_map: dict[int, UserDataTuple]
) -> int | None:
    for user_id in users_ids:
        if user_spent := users_ids_to_users_map.get(user_id):
            return sum(user_spent[2])
    return None  # RET503 Missing explicit `return` at the end of function able to return non-`None` value


if __name__ == '__main__':
    assert (  # noqa: S101
        calculate_total_spent_for_users(
            users_ids={3, 6, 12, 15},
            users_ids_to_users_map={
                3: ('Ilya', 32, [102, 15, 63, 12]),
            },
        )
        == 192  # noqa: PLR2004
    )
