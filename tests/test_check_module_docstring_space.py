import os

import pytest

from pchooks.check_module_docstring_space import main

RESOURCES_DIR = os.path.join(os.path.dirname(__file__), "resources")


@pytest.mark.parametrize(
    "file_path, n_lines, expected",
    [
        (os.path.join(RESOURCES_DIR, "module_ds_no_line.py"), 0, 0),
        (os.path.join(RESOURCES_DIR, "module_ds_no_line.py"), 1, 1),
        (os.path.join(RESOURCES_DIR, "module_ds_no_line.py"), 2, 1),
        (os.path.join(RESOURCES_DIR, "module_ds_one_line.py"), 0, 1),
        (os.path.join(RESOURCES_DIR, "module_ds_one_line.py"), 1, 0),
        (os.path.join(RESOURCES_DIR, "module_ds_one_line.py"), 2, 1),
        (os.path.join(RESOURCES_DIR, "module_ds_two_lines.py"), 0, 1),
        (os.path.join(RESOURCES_DIR, "module_ds_two_lines.py"), 1, 1),
        (os.path.join(RESOURCES_DIR, "module_ds_two_lines.py"), 2, 0),
        (os.path.join(RESOURCES_DIR, "module_ds_just_ds.py"), 0, 0),
        (os.path.join(RESOURCES_DIR, "module_ds_just_ds.py"), 1, 0),
        (os.path.join(RESOURCES_DIR, "module_ds_just_ds.py"), 2, 0),
        (os.path.join(RESOURCES_DIR, "empty.py"), 0, 0),
        (os.path.join(RESOURCES_DIR, "empty.py"), 1, 0),
        (os.path.join(RESOURCES_DIR, "empty.py"), 2, 0),
    ],
)
def test_correct_validity_marking(file_path: str, n_lines: int, expected: int):
    """Test that the correct output code is returned for a given file."""
    assert main([f"-n {n_lines}", file_path]) == expected
