import decimal
import uuid


def get_user_balance(user_id: uuid.UUID) -> decimal.Decimal:  # noqa: ARG001
    return decimal.Decimal('265.2')


if __name__ == "__main__":
    assert get_user_balance(user_id=uuid.uuid4()) == decimal.Decimal("265.2")  # noqa: S101
