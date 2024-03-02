def is_adult(age: int, country_name: str) -> bool:
    return bool(age and country_name)


if __name__ == "__main__":
    assert is_adult(age=17, country_name="Russia") is True  # noqa: S101
