# Pre-commit hooks

This repo is intended to include a collection of simple, mostly Python-related [pre-commit](https://pre-commit.com/) hooks.

## Usage

Add this to your .pre-commit-config.yaml

```yaml
- repo: https://github.com/martinstefanik/pre-commit-hooks
    rev: v1.0.0  # Use the ref you want to point at
    hooks:
    - id: check-multiline-docstrings
```

## Available hooks

`check-multiline-docstrings`

Check that all multiline docstrings in Python files start and end with a _single_ newline character. This checks whether the docstrings are formatted like this

```python
def personalized_greeting(name: str) -> None:
    """
    Personalized greeting printer.

    Args:
        name: Name of the person/entity to greet.
    """
    print(f"Welcome, {name}!")
```

as opposed for instance to this

```python
def personalized_greeting(name: str) -> None:
    """Personalized greeting printer.

    Args:
        name: Name of the person/entity to greet.
    """
    print(f"Welcome, {name}!")
```

This might be slightly less common but still conforms to the [PEP 257](https://peps.python.org/pep-0257/#multi-line-docstrings) and some people might prefer docstrings formatted this way.
