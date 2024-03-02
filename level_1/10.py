def stringify(value: object) -> str:
    return str(value)


if __name__ == '__main__':
    assert stringify(value='12') == '12'  # noqa: S101
    assert stringify(value=15) == '15'  # noqa: S101
    assert stringify(value=0.5) == '0.5'  # noqa: S101
    assert stringify(value=None) == 'None'  # noqa: S101
