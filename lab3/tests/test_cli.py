# -*- coding: utf-8 -*-
"""Модульные тесты для консольного интерфейса NetworkCli."""

import unittest
from unittest.mock import patch
from lab3.cli.network_cli import NetworkCli


class TestNetworkCli(unittest.TestCase):
    """Тестирование функциональности CLI без интерактивного ввода."""

    def setUp(self):
        self.cli = NetworkCli()

    def test_cli_methods(self):
        """Проверка выполнения всех демонстрационных методов интерфейса."""
        self.cli.show_system_report()
        self.cli.manage_users()
        self.cli.manage_posts()
        self.cli.manage_polls()
        self.cli.manage_chats()
        self.cli.manage_friendship()
        self.cli.manage_blocking()
        self.cli.manage_finances()
        self.cli.manage_moderation()
        self.cli.show_analytics_and_search()

    @patch("builtins.input", side_effect=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "unknown", "0"])
    def test_cli_run_menu_flow(self, mock_input):
        """Проверка цикла run по всем пунктам меню и выход."""
        self.cli.run()

    @patch("builtins.input", side_effect=EOFError)
    def test_cli_run_eof(self, mock_input):
        """Проверка реакции на сигнал завершения ввода EOF."""
        self.cli.run()


if __name__ == "__main__":
    unittest.main()
