# Pre-commit hooks

This repo includes a collection of simple [pre-commit](https://pre-commit.com/) hooks for Python.

## Usage

Add the following to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/martinstefanik/pre-commit-hooks
    rev: v1.1.0  # Use the ref you want to point at
    hooks:
    - id: check-multiline-docstrings
    - id: check-module-docstring-space
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

`check-module-docstring-space`

Check that the module docstring is separated from the rest of the code by a pre-defined number of empty lines. This is mostly intended to avoid having no space between the module docstring and the imports. This is something the commonly used code formatter [Black](https://black.readthedocs.io/en/stable/) allows for as of version 2023.9.0.
