from collections.abc import Callable


def create_user(user_name: str, user_age: int, after_created: Callable) -> None:  # noqa: ARG001
    pass


def send_test_email(user_id: int) -> None:  # noqa: ARG001
    pass


if __name__ == '__main__':
    assert (  # noqa: S101
        create_user(  # type: ignore
            user_name='Ilya',
            user_age=32,
            after_created=send_test_email,
        )
        is None
    )
