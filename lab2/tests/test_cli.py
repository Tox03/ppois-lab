"""Тесты для интерактивного консольного интерфейса завода."""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cli.plant_cli import PlantCli

class TestCliSuite(unittest.TestCase):
    """Тестирует сценарии работы интерактивного меню завода, сдачи заказов и обновления данных."""

    def test_cli_full_interactive_lifecycle(self):
        """Проверяет полный цикл: производство, создание/сдача заказов, обновление оборудования, склада и персонала."""
        cli = PlantCli()
        commands = [
            # 1. Запуск суточного производства (2 смены)
            "1", "2",
            # 2. Создание нового наряда-заказа
            "2", "НАРЯД-002", "Поршень Спорт 16V", "600", "2026-11-05",
            # 3. Сдача (завершение) первого наряда-заказа
            "3", "1",
            # 4. Пополнение склада сырьем (обновление данных)
            "4", "1", "200.0",
            # 4. Списание сырья со склада
            "4", "2", "50.0",
            # 5. Оформление и отгрузка коммерческого заказа
            "5", "ДОГОВОР-002", "Поршень Спорт в сборе", "300", "60.0",
            # 6. Сдача коммерческого заказа клиенту (подтверждение доставки)
            "6", "1",
            # 7. Обновление параметров станка ЧПУ (обороты шпинделя)
            "7", "1", "8500",
            # 7. Плановое ТО станка (охлаждение)
            "7", "2",
            # 7. Заточка инструмента
            "7", "3",
            # 8. Пополнение годового бюджета завода
            "8", "1", "250000.0",
            # 8. Повышение сотрудника и индексация оклада
            "8", "2", "Ведущий наладчик ЧПУ", "20.0",
            # 8. Изменение квалификационного разряда
            "8", "3", "6",
            # 9. Контроль качества ОТК
            "9", "82.46",
            # 10. Симуляция аварии
            "10",
            # 7. Плановое ТО и устранение последствий перегрева
            "7", "2",
            # 11. Сводный отчет предприятия
            "11",
            # Некорректный пункт меню
            "99",
            # 0. Выход
            "0"
        ]

        cli.run(auto_input=commands)

        # Проверка выпуска продукции
        self.assertEqual(cli.plant.total_parts_produced, 20)
        # Проверка создания заказов
        self.assertEqual(len(cli.plant.active_orders), 2)
        # Проверка СДАЧИ заказа
        self.assertEqual(cli.plant.active_orders[0].status, "ВЫПОЛНЕН")
        # Проверка СДАЧИ заказа клиенту
        self.assertTrue(cli.active_dispatches[0].is_delivered)
        # Проверка ОБНОВЛЕНИЯ данных оборудования
        self.assertEqual(cli.cnc_station.spindle_rpm, 8500)
        self.assertEqual(cli.machine_cnc.current_temperature, 25.0)
        self.assertEqual(cli.cutter.flank_wear_mm, 0.0)
        # Проверка ОБНОВЛЕНИЯ данных бюджета и персонала
        self.assertEqual(cli.director.annual_budget, 5250000.0)
        self.assertEqual(cli.operator.employee.position, "Ведущий наладчик ЧПУ")
        self.assertEqual(cli.operator.qualification_rank, 6)
        # Проверка ОБНОВЛЕНИЯ складских остатков (1500 + 200 - 50 = 1650)
        self.assertEqual(cli.bin_a1.current_weight_kg, 1650.0)

    def test_cli_order_completion_and_recomplete(self):
        """Проверяет обработку попытки повторной сдачи уже выполненного заказа."""
        cli = PlantCli()
        # Сдаем заказ 1, затем пытаемся сдать его снова, затем выход
        commands = ["3", "1", "3", "1", "0"]
        cli.run(auto_input=commands)
        self.assertEqual(cli.plant.active_orders[0].status, "ВЫПОЛНЕН")

    def test_cli_delivery_confirmation_and_reconfirm(self):
        """Проверяет подтверждение доставки и повторную попытку подтверждения."""
        cli = PlantCli()
        commands = ["6", "1", "6", "1", "0"]
        cli.run(auto_input=commands)
        self.assertTrue(cli.active_dispatches[0].is_delivered)

    def test_cli_invalid_input_handling(self):
        """Проверяет устойчивость к некорректным числовым и текстовым значениям."""
        cli = PlantCli()
        # Некорректный выбор наряда (индекс 999), некорректное число для оборотов ЧПУ
        commands = ["3", "999", "7", "1", "not_a_number", "0"]
        cli.run(auto_input=commands)
        self.assertEqual(cli.plant.active_orders[0].status, "В_ПРОИЗВОДСТВЕ")

    def test_cli_empty_collections_and_subchoices(self):
        """Проверяет вызовы операций при пустых списках нарядов/ТТН и неизвестных подоперациях."""
        cli = PlantCli()
        cli.plant.active_orders.clear()
        cli.active_dispatches.clear()
        # 3 (нет нарядов), 6 (нет ТТН), 4 -> 99 (неизвестно), 7 -> 99, 8 -> 99, 0
        commands = ["3", "6", "4", "99", "7", "99", "8", "99", "0"]
        cli.run(auto_input=commands)

    def test_cli_defective_part_inspection(self):
        """Проверяет сценарий ОТК при обнаружении брака детали."""
        cli = PlantCli()
        # 9 (ОТК) с бракованным размером 90.0 мм, 0
        commands = ["9", "90.0", "0"]
        cli.run(auto_input=commands)

    def test_cli_prompt_fallback_on_eof(self):
        """Проверяет корректное возвращение дефолтного значения при EOFError в консоли."""
        cli = PlantCli()
        cli._input_gen = None
        import unittest.mock as mock
        with mock.patch("builtins.input", side_effect=EOFError):
            result = cli._prompt("Введите значение", "дефолт")
            self.assertEqual(result, "дефолт")
        with mock.patch("builtins.input", side_effect=KeyboardInterrupt):
            result2 = cli._prompt("Введите значение", "дефолт2")
            self.assertEqual(result2, "дефолт2")

if __name__ == "__main__":
    unittest.main()
