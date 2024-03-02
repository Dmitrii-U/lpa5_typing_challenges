def compose_full_name(first_name: str, last_name: str, middle_name: str | None) -> str:
    middle_name = f' {middle_name}' if middle_name else ''
    return f'{last_name} {first_name}{middle_name}'


if __name__ == '__main__':
    assert compose_full_name(first_name='John', last_name='Doe', middle_name=None) == 'Doe John'  # noqa: S101
    assert (  # noqa: S101
        compose_full_name(first_name='Ilya', last_name='Lebedev', middle_name='Alexeyevich')
        == 'Lebedev Ilya Alexeyevich'
    )
