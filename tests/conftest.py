"""
PiTrac Tower Build - Pytest Configuration
This file is automatically loaded by pytest before running any tests.
Think of it as the "setup the room before the meeting" file.
"""

import pathlib
import pytest


@pytest.fixture
def projectRoot():
    """Returns the project root directory path.
    Useful when tests need to find project files."""
    return pathlib.Path(__file__).parent.parent


@pytest.fixture
def testsDir():
    """Returns the tests directory path."""
    return pathlib.Path(__file__).parent
