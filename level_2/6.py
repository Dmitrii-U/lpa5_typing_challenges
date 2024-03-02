def is_name_male(name: str, name_gender_map: dict[str, bool]) -> bool | None:
    return name_gender_map.get(name)


if __name__ == '__main__':
    name_gender_map = {
        'John': True,
        'Jane': False,
    }
    assert is_name_male('John', name_gender_map) is True  # noqa: S101
    assert is_name_male('Unknown', name_gender_map) is None  # noqa: S101
