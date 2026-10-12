"""Тесты для консольного интерфейса завода."""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cli.plant_cli import PlantCli

class TestCliSuite(unittest.TestCase):
    """Тестирует сценарии работы интерактивного меню завода."""

    def test_cli_all_actions(self):
        cli = PlantCli()
        # Запуск сценариев меню по очереди и завершение
        commands = ["1", "2", "3", "4", "5", "6", "7", "99", "0"]
        cli.run(auto_input=commands)
        self.assertEqual(cli.plant.total_parts_produced, 10)
        self.assertEqual(len(cli.plant.active_orders), 1)

if __name__ == "__main__":
    unittest.main()
