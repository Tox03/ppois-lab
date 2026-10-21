"""Тесты для точки входа main.py."""

import sys
import os
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from main import main

class TestMainSuite(unittest.TestCase):
    """Тестирует запуск основного приложения через main()."""

    @patch("builtins.input", return_value="0")
    def test_main_execution(self, mock_input):
        """Проверяет запуск CLI и выход по команде 0."""
        main()
        self.assertTrue(mock_input.called)

if __name__ == "__main__":
    unittest.main()
