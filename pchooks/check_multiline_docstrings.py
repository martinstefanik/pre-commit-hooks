"""
Script for checking whether multi-line docstrings start and end with a single
newline character so that they are formatted like this very docstring.
"""

import argparse
import ast
import re
from dataclasses import dataclass
from typing import Sequence, Union


def main(argv: Union[Sequence[str], None] = None) -> int:
    """
    Entry point for the pre-commit hook.

    Args:
        argv: Command-line arguments.

    Returns:
        0 if checks for all files pass, 1 otherwise.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Pre-commit hook to check whether multi-line docstrings start and "
            "end with a single newline."
        )
    )
    parser.add_argument("file_paths", nargs="*", help="Python files to check.")
    args = parser.parse_args(argv)

    return_code = 0
    for file_path in args.file_paths:
        return_code |= check_file_docstrings(file_path)
    return return_code


@dataclass
class Docstring:
    """Representation of a docstring."""

    file_path: str
    line_number: int
    docstring: str


def check_file_docstrings(file_path: str) -> int:
    """
    Check that the multi-line docstrings in a given file start and end with a
    single newline character.

    Args:
        file_path: Path to the Python file to check.

    Returns:
        0 if the check passes, 1 otherwise.
    """
    return_code = 0
    docstrings = extract_docstrings(file_path)
    for ds in docstrings:
        if not is_docstring_valid(ds):
            return_code = 1
            print(f"Misformatted docstring: {ds.file_path}:{ds.line_number}")
    return return_code


def extract_docstrings(file_path: str) -> list[Docstring]:
    """
    Extract docstrings together with their starting lines from a given Python
    file (without the opening and closing triple quotes).

    Args:
        file_path: Path to the Python file to extract docstrings from.

    Returns:
        List of docstrings together with their starting lines.
    """
    with open(file_path, "r") as f:
        code = f.read()
    tree = ast.parse(code)
    docstrings = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Str):
            docstring = Docstring(
                file_path=file_path,
                line_number=node.lineno,
                docstring=node.value.s,
            )
            docstrings.append(docstring)
    return docstrings


def is_docstring_valid(docstring: Docstring) -> bool:
    """Check whether a given docstring is valid.

    Args:
        docstring: Docstring to check.

    Returns:
        Indication of whether the docstring is valid.
    """
    stripped_docstring = docstring.docstring.strip(" \t")
    if stripped_docstring.count("\n") > 0:
        start_match = re.search(r"^\n(?!\n)", stripped_docstring)
        if start_match is None:
            return False
        end_match = re.search(r"\n+$", stripped_docstring)
        if end_match is None or len(end_match.group()) > 1:
            return False
    return True


if __name__ == "__main__":
    SystemExit(main())  # pragma: no cover
