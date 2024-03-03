import decimal
from collections.abc import Mapping


def get_transaction_amount(
    transaction_id: int, transactions_amounts_map: Mapping[int, decimal.Decimal]
) -> decimal.Decimal | None:
    # попробуйте использовать typing.Mapping: transactions_amounts_map по смыслу не должен меняться внутри функции
    return transactions_amounts_map.get(transaction_id)


if __name__ == '__main__':
    transactions_amounts_map = {
        156: decimal.Decimal('30.6'),
        514: decimal.Decimal('164.1'),
        372: decimal.Decimal('92'),
    }
    assert get_transaction_amount(  # noqa: S101
        transaction_id=156, transactions_amounts_map=transactions_amounts_map
    ) == decimal.Decimal('30.6')
    assert (  # noqa: S101
        get_transaction_amount(transaction_id=1000, transactions_amounts_map=transactions_amounts_map) is None
    )
