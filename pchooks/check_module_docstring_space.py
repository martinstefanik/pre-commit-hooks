"""
CLI for checking whether module docstring are followed by a given number of
empty lines.
"""

import argparse
import re
from typing import Sequence, Union


def main(argv: Union[Sequence[str], None] = None) -> int:
    """
    Entry point for the 'check-module-docstring-space' pre-commit hook.

    Args:
        argv: Command-line arguments.

    Returns:
        0 if checks for all files pass, 1 otherwise.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Pre-commit hook to check whether module docstrings are followed "
            "by a given number of empty line."
        )
    )
    parser.add_argument(
        "-n",
        "--n-lines",
        type=int,
        default=1,
        help="The number of lines that should follow a module docstring.",
    )
    parser.add_argument("file_paths", nargs="*", help="Python files to check.")
    args = parser.parse_args(argv)

    return_code = 0
    for file_path in args.file_paths:
        return_code |= check_module_docstring_space(
            file_path, n_lines=args.n_lines
        )

    return return_code


def check_module_docstring_space(file_path: str, n_lines: int) -> int:
    """
    Check that the module docstring in a given file is followed by a given
    number of empty lines.

    Args:
        file_path: Path to the Python file to check.
        n_lines: The number of lines that should follow a module docstring.

    Returns:
        0 if the check passes, 1 otherwise.
    """
    return_code = 0
    with open(file_path, "r") as f:
        file_contents = f.read()
        pattern = re.compile(r'^""".*?"""(\n*)', flags=re.DOTALL)
        match = pattern.match(file_contents)
        if match is not None:
            if match.group(1) != "\n" * (n_lines + 1):
                return_code = 1
                print(
                    f"Module docstring should be followed by {n_lines} empty "
                    f"{'line' if n_lines == 1 else 'lines'}: {file_path}"
                )
    return return_code


if __name__ == "__main__":
    SystemExit(main())  # pragma: no cover
