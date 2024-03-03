from typing import TypedDict


class User(TypedDict):
    name: str
    age: int
    transactions_sums: list[int]


def calculate_total_spent_for_user(user: User) -> int:
    return sum(user.get('transactions_sums', []))


if __name__ == '__main__':
    assert (  # noqa: S101
        calculate_total_spent_for_user(
            user={
                'name': 'Ilya',
                'age': 32,
                'transactions_sums': [102, 15, 63, 12],
            },
        )
        == 192  # noqa: PLR2004
    )
