import os

import pytest

from pchooks.check_multiline_docstrings import main

RESOURCES_DIR = os.path.join(os.path.dirname(__file__), "resources")


@pytest.mark.parametrize(
    "file_path, expected",
    [
        (os.path.join(RESOURCES_DIR, "module_start_invalid_1.py"), 1),
        (os.path.join(RESOURCES_DIR, "module_start_invalid_2.py"), 1),
        (os.path.join(RESOURCES_DIR, "module_start_invalid_3.py"), 1),
        (os.path.join(RESOURCES_DIR, "module_end_invalid_1.py"), 1),
        (os.path.join(RESOURCES_DIR, "module_end_invalid_2.py"), 1),
        (os.path.join(RESOURCES_DIR, "module_end_invalid_3.py"), 1),
        (os.path.join(RESOURCES_DIR, "module_valid.py"), 0),
        (os.path.join(RESOURCES_DIR, "function_start_invalid_1.py"), 1),
        (os.path.join(RESOURCES_DIR, "function_start_invalid_2.py"), 1),
        (os.path.join(RESOURCES_DIR, "function_start_invalid_3.py"), 1),
        (os.path.join(RESOURCES_DIR, "function_end_invalid_1.py"), 1),
        (os.path.join(RESOURCES_DIR, "function_end_invalid_2.py"), 1),
        (os.path.join(RESOURCES_DIR, "function_end_invalid_3.py"), 1),
        (os.path.join(RESOURCES_DIR, "function_end_invalid_3.py"), 1),
        (os.path.join(RESOURCES_DIR, "function_valid.py"), 0),
        (os.path.join(RESOURCES_DIR, "empty.py"), 0),
    ],
)
def test_correct_validity_marking(file_path: str, expected: int):
    """Test that the correct output code is returned for a given file."""
    assert main([file_path]) == expected
