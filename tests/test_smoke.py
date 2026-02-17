"""
PiTrac Tower Build - Smoke Tests
These are quick sanity checks that verify the project structure
and basic assumptions are correct. Think of these like a "hello world"
for the project - if these fail, something fundamental is wrong.
"""

import os
import pathlib


# Where is the project root? One level up from the tests/ folder.
projectRoot = pathlib.Path(__file__).parent.parent


class TestProjectStructure:
    """Verify the basic directory structure exists.
    Like checking that all the rooms in your house are still there
    before you start redecorating."""

    def test_claudeMdExists(self):
        """The .claude.md file must exist - it's our rulebook."""
        claudeMdPath = projectRoot / ".claude.md"
        assert claudeMdPath.exists(), (
            f"Missing .claude.md at {claudeMdPath}. "
            "This file contains all our mandatory development rules."
        )

    def test_handoffMdExists(self):
        """The handoff.md file must exist - it's our memory between sessions."""
        handoffPath = projectRoot / "handoff.md"
        assert handoffPath.exists(), (
            f"Missing handoff.md at {handoffPath}. "
            "This file tracks what happened and what's next."
        )

    def test_testDirectoryExists(self):
        """The tests/ directory must exist - no tests means no confidence."""
        testsDir = projectRoot / "tests"
        assert testsDir.is_dir(), (
            f"Missing tests/ directory at {testsDir}. "
            "We need this for our Ralph Loop test suites."
        )

    def test_requiredDirectoriesExist(self):
        """All standard project directories should be present."""
        requiredDirs = ["tests", "scripts", "config", "src"]
        for dirName in requiredDirs:
            dirPath = projectRoot / dirName
            assert dirPath.is_dir(), (
                f"Missing required directory: {dirPath}. "
                f"Run: mkdir -p {dirPath}"
            )


class TestClaudeMdContent:
    """Verify .claude.md contains all mandatory rules.
    Like checking that your recipe has all the ingredients listed
    before you start cooking."""

    def test_claudeMdHasRalphLoop(self):
        """Ralph Loop rule must be documented."""
        claudeMdPath = projectRoot / ".claude.md"
        contentText = claudeMdPath.read_text()
        assert "Ralph Loop" in contentText, (
            ".claude.md must document the Ralph Loop (3-cycle TDD process)"
        )

    def test_claudeMdHasBarneyStyle(self):
        """Barney-style explanation rule must be documented."""
        claudeMdPath = projectRoot / ".claude.md"
        contentText = claudeMdPath.read_text()
        assert "Barney" in contentText, (
            ".claude.md must document the Barney-style explanation requirement"
        )

    def test_claudeMdHasCamelCase(self):
        """camelCase naming rule must be documented."""
        claudeMdPath = projectRoot / ".claude.md"
        contentText = claudeMdPath.read_text()
        assert "camelCase" in contentText, (
            ".claude.md must document the Smalltalk camelCase naming convention"
        )

    def test_claudeMdHasHandoffRule(self):
        """Handoff.md maintenance rule must be documented."""
        claudeMdPath = projectRoot / ".claude.md"
        contentText = claudeMdPath.read_text()
        assert "handoff" in contentText.lower(), (
            ".claude.md must document the handoff.md maintenance rule"
        )

    def test_claudeMdHasTestSuiteRule(self):
        """Test suite rule must be documented."""
        claudeMdPath = projectRoot / ".claude.md"
        contentText = claudeMdPath.read_text()
        assert "test suite" in contentText.lower() or "Test Suite" in contentText, (
            ".claude.md must document the complete test suite requirement"
        )
