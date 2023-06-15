"""Greetings module."""


def greeting() -> None:
    print("Welcome!")


def personalized_greeting(name: str) -> None:
    """
    Personalized greeting printer.

    Args:
        name: Name of the person/entity to greet.
    """
    print(f"Welcome, {name}!")
