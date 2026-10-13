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
        self.cli.list_users()
        self.cli.create_post_demo()
        self.cli.run_poll_demo()
        self.cli.send_message_demo()
        self.cli.friendship_demo()
        self.cli.moderation_demo()
        self.cli.monetization_demo()
        self.cli.analytics_search_demo()

    @patch("builtins.input", side_effect=["1", "0"])
    def test_cli_run_exit(self, mock_input):
        """Проверка цикла run с последующим выходом (пункт 0)."""
        self.cli.run()


if __name__ == "__main__":
    unittest.main()
