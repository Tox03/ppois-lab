"""Тесты для интерактивного консольного интерфейса завода."""

from __future__ import annotations
import sys
import os
import unittest
import tempfile
import unittest.mock as mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from cli.plant_cli import PlantCli
from plant.production.production_line import ProductionLine
from plant.production.production_plan import ProductionPlan
from plant.production.production_order import ProductionOrder


class TestCliSuite(unittest.TestCase):
    """Тестирует сценарии работы интерактивного меню завода, сдачи заказов, линий, персонала и JSON."""

    def test_cli_full_interactive_lifecycle(self):
        """Проверяет полный цикл: производство, линии, создание/сдача заказов, ТО, найм персонала, JSON."""
        cli = PlantCli()
        commands = [
            # 1. Запуск суточного производства (2 смены)
            "1", "2",
            # 2. Управление линиями: плановый останов линии 1, затем ее успешный перезапуск
            "2", "2", "1",
            "2", "1", "1",
            # 2. Добавление технологического поста на линию
            "2", "3",
            # 3. Создание нового наряда-заказа
            "3", "НАРЯД-002", "Поршень Спорт 16V", "600", "2026-11-05",
            # 4. Сдача (завершение) первого наряда-заказа
            "4", "1",
            # 5. Пополнение склада сырьем (обновление данных)
            "5", "1", "200.0",
            # 5. Списание сырья со склада
            "5", "2", "50.0",
            # 5. Добавление новой складской ячейки
            "5", "3", "B-01", "3000.0",
            # 6. Оформление и отгрузка коммерческого заказа
            "6", "ДОГОВОР-002", "Поршень Спорт в сборе", "300", "60.0",
            # 7. Сдача коммерческого заказа клиенту (подтверждение доставки)
            "7", "1",
            # 8. Обновление параметров станка ЧПУ (обороты шпинделя)
            "8", "1", "8500",
            # 8. Плановое ТО станка (охлаждение)
            "8", "2",
            # 8. Заточка инструмента
            "8", "3",
            # 8. Регистрация нового станка
            "8", "4", "СТАНОК-03", "DMG-50",
            # 9. Пополнение годового бюджета завода
            "9", "1", "250000.0",
            # 9. Найм нового оператора станков с ЧПУ
            "9", "2", "Петров Иван Сидорович", "1", "Оператор ЧПУ 4 разряда", "2800.0", "+375-29-333-44-55", "petrov@autoplant.by",
            # 9. Просмотр штатного расписания
            "9", "3",
            # 9. Повышение сотрудника и индексация оклада
            "9", "4", "2", "Ведущий наладчик ЧПУ", "20.0",
            # 9. Изменение квалификационного разряда оператора
            "9", "5", "6",
            # 10. Контроль качества ОТК
            "10", "82.46",
            # 11. Симуляция аварии (перегрев станка ЧПУ)
            "11",
            # 2. Восстановление и перезапуск линии после аварии
            "2", "1", "1",
            # 12. Сводный отчет предприятия
            "12",
            # 13. Сохранение состояния в JSON
            "13", "1",
            # 13. Загрузка состояния из JSON
            "13", "2",
            # 13. Сброс к исходным настройкам
            "13", "3",
            # Некорректный пункт меню
            "99",
            # 0. Выход (отказ от сохранения)
            "0", "нет"
        ]

        cli.run(auto_input=commands)

        # Проверка создания заказов
        self.assertGreaterEqual(len(cli.plant.active_orders), 1)
        # Проверка директора и бюджета
        self.assertGreaterEqual(cli.director.annual_budget, 5000000.0)

    def test_cli_zero_and_negative_shifts(self):
        """Проверяет обработку 0 и отрицательного числа рабочих смен."""
        cli = PlantCli()
        init_prod = cli.plant.total_parts_produced
        commands = ["1", "0", "1", "-5", "0", "нет"]
        cli.run(auto_input=commands)
        self.assertEqual(cli.plant.total_parts_produced, init_prod)

    def test_cli_line_halt_and_recovery(self):
        """Проверяет останов линии, невозможность выпуска и ее последующий перезапуск."""
        cli = PlantCli()
        commands = [
            # Плановый останов линии
            "2", "2", "1",
            # Попытка запуска суточного производства на остановленной линии
            "1", "1",
            # Перезапуск линии
            "2", "1", "1",
            # Запуск производства после перезапуска
            "1", "1",
            "0", "нет"
        ]
        init_parts = cli.plant.total_parts_produced
        cli.run(auto_input=commands)
        self.assertGreater(cli.plant.total_parts_produced, init_parts)

    def test_cli_order_completion_and_recomplete(self):
        """Проверяет обработку попытки повторной сдачи уже выполненного заказа."""
        cli = PlantCli()
        commands = ["4", "1", "4", "1", "0", "нет"]
        cli.run(auto_input=commands)
        self.assertEqual(cli.plant.active_orders[0].status, "ВЫПОЛНЕН")

    def test_cli_delivery_confirmation_and_reconfirm(self):
        """Проверяет подтверждение доставки и повторную попытку подтверждения."""
        cli = PlantCli()
        commands = ["7", "1", "7", "1", "0", "нет"]
        cli.run(auto_input=commands)
        self.assertTrue(cli.active_dispatches[0].is_delivered)

    def test_cli_invalid_input_handling(self):
        """Проверяет устойчивость к некорректным числовым и текстовым значениям."""
        cli = PlantCli()
        commands = [
            "4", "999",
            "4", "not_a_num",
            "7", "999",
            "7", "invalid_num",
            "2", "1", "999",
            "2", "2", "999",
            "2", "99",
            "8", "1", "not_a_number",
            "8", "1", "200",
            "8", "1", "30000",
            "8", "99",
            "5", "1", "-100",
            "5", "2", "-50",
            "5", "99",
            "6", "ДОГ-ERR", "Поршень", "0", "0",
            "3", "НАРЯД-ERR", "Поршень", "-10", "2026-10-30",
            "9", "1", "-500",
            "9", "4", "999",
            "9", "5", "10",
            "9", "99",
            "13", "99",
            "0", "нет"
        ]
        cli.run(auto_input=commands)
        self.assertEqual(cli.plant.active_orders[0].status, "В_ПРОИЗВОДСТВЕ")

    def test_cli_empty_collections_and_subchoices(self):
        """Проверяет вызовы операций при пустых списках нарядов/ТТН и неизвестных подоперациях."""
        cli = PlantCli()
        cli.plant.active_orders.clear()
        cli.active_dispatches.clear()
        cli.plant.production_lines.clear()
        commands = [
            "2", "4", "7", "0", "нет"
        ]
        cli.run(auto_input=commands)

    def test_cli_hire_all_role_types(self):
        """Проверяет найм всех поддерживаемых типов должностей персонала."""
        cli = PlantCli()
        commands = [
            # 1: Контролер ОТК (роль 2)
            "9", "2", "Соколова Анна Михайловна", "2", "Контролер ОТК 1 кат", "2400", "+375-29-111-00-11", "sokolova@plant.by",
            # 2: Инженер ТО (роль 3)
            "9", "2", "Григорьев Семен Ильич", "3", "Инженер по ремонту станков", "3100", "+375-29-222-00-22", "grig@plant.by",
            # 3: Инспектор ТБ (роль 4)
            "9", "2", "Павлов Виктор Олегович", "4", "Инженер охраны труда", "2500", "+375-29-333-00-33", "pavlov@plant.by",
            # 4: Инструментальщик (роль 5)
            "9", "2", "Кузнецов Дмитрий Романович", "5", "Слесарь 6 разряда", "2700", "+375-29-444-00-44", "kuznetsov@plant.by",
            # 5: Произвольная должность (роль 99)
            "9", "2", "Алексеев Петр Сергеевич", "99", "Начальник склада", "2900", "+375-29-555-00-55", "alekseev@plant.by",
            "0", "нет"
        ]
        cli.run(auto_input=commands)
        self.assertGreaterEqual(len(cli.employees), 8)

    def test_cli_json_save_load_and_reset(self):
        """Проверяет сохранение, загрузку и сброс состояния завода через временный файл."""
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
            tmp_path = tmp.name

        try:
            cli = PlantCli()
            cli.plant.total_parts_produced = 999
            cli.director.annual_budget = 7770000.0

            # Сохранение в файл
            self.assertTrue(cli.save_to_json(tmp_path))

            # Создание нового экземпляра и загрузка
            cli2 = PlantCli()
            self.assertTrue(cli2.load_from_json(tmp_path))
            self.assertEqual(cli2.plant.total_parts_produced, 999)
            self.assertEqual(cli2.director.annual_budget, 7770000.0)

            # Проверка загрузки несуществующего файла
            self.assertFalse(cli2.load_from_json("non_existent_file_12345.json"))

            # Проверка загрузки поврежденного файла
            with open(tmp_path, "w", encoding="utf-8") as f:
                f.write("{invalid_json: true,")
            self.assertFalse(cli2.load_from_json(tmp_path))
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_cli_save_on_exit(self):
        """Проверяет сохранение данных при выходе с ответом 'да'."""
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
            tmp_path = tmp.name

        try:
            cli = PlantCli()
            cli.STATE_FILE_PATH = tmp_path
            commands = ["0", "да"]
            cli.run(auto_input=commands)
            self.assertTrue(os.path.exists(tmp_path))
            self.assertGreater(os.path.getsize(tmp_path), 0)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_cli_defective_part_inspection(self):
        """Проверяет сценарий ОТК при обнаружении брака детали."""
        cli = PlantCli()
        commands = ["10", "90.0", "0", "нет"]
        cli.run(auto_input=commands)

    def test_cli_prompt_fallback_on_eof(self):
        """Проверяет корректное возвращение дефолтного значения при EOFError в консоли."""
        cli = PlantCli()
        cli._input_gen = None
        with mock.patch("builtins.input", side_effect=EOFError):
            result = cli._prompt("Введите значение", "дефолт")
            self.assertEqual(result, "дефолт")
        with mock.patch("builtins.input", side_effect=KeyboardInterrupt):
            result2 = cli._prompt("Введите значение", "дефолт2")
            self.assertEqual(result2, "дефолт2")

    def test_cli_corrupted_json_handling(self):
        """Проверяет корректную обработку поврежденного JSON-файла при загрузке."""
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w", encoding="utf-8") as tmp:
            tmp.write("{ invalid json file content }")
            tmp_path = tmp.name

        try:
            cli = PlantCli()
            cli.STATE_FILE_PATH = tmp_path
            # Меню 13, операция 2 (Загрузить из JSON), затем 0 (Выход) без сохранения
            commands = ["13", "2", "0", "нет"]
            cli.run(auto_input=commands)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_cli_boundary_menu_choices(self):
        """Проверяет поведение при вводе некорректных команд в главном меню."""
        cli = PlantCli()
        commands = ["99", "-1", "abc", "", "0", "нет"]
        cli.run(auto_input=commands)

    def test_cli_personnel_promotion_and_rank_change(self):
        """Проверяет сценарии повышения сотрудника и изменения разряда."""
        cli = PlantCli()
        commands = ["9", "4", "2", "Старший оператор станков с ЧПУ", "20.0", "9", "5", "6", "0", "нет"]
        cli.run(auto_input=commands)
        self.assertEqual(cli.operator.qualification_rank, 6)

    def test_cli_personnel_promotion_invalid_index(self):
        """Проверяет сценарий ввода неверного номера сотрудника при повышении."""
        cli = PlantCli()
        commands = ["9", "4", "999", "9", "99", "0", "нет"]
        cli.run(auto_input=commands)

    def test_cli_line_halt_and_resume_interactive(self):
        """Проверяет останов и возобновление линий через меню управления линиями."""
        cli = PlantCli()
        commands = ["2", "1", "2", "2", "2", "3", "0", "нет"]
        cli.run(auto_input=commands)

    def test_cli_warehouse_and_supplies(self):
        """Проверяет сценарии работы с сырьем и складами предприятия."""
        cli = PlantCli()
        commands = ["6", "1", "6", "2", "100.0", "0", "нет"]
        cli.run(auto_input=commands)

    def test_cli_prompt_validations_and_generator_exhaustion(self):
        """Проверяет валидацию ввода чисел (границы, ошибки типа) и исчерпание генератора."""
        cli = PlantCli()
        cli._input_gen = iter(["val1"])
        self.assertEqual(cli._prompt("msg", "def"), "val1")
        self.assertEqual(cli._prompt("msg", "def"), "def")

        cli._input_gen = iter(["-5", "105", "not_int", "42"])
        self.assertEqual(cli._prompt_int("m", 10, min_val=0), 10)
        self.assertEqual(cli._prompt_int("m", 10, max_val=100), 10)
        self.assertEqual(cli._prompt_int("m", 10), 10)
        self.assertEqual(cli._prompt_int("m", 10), 42)

        cli._input_gen = iter(["-1.5", "150.0", "bad_flt", "3.14"])
        self.assertEqual(cli._prompt_float("m", 5.0, min_val=0.0), 5.0)
        self.assertEqual(cli._prompt_float("m", 5.0, max_val=100.0), 5.0)
        self.assertEqual(cli._prompt_float("m", 5.0), 5.0)
        self.assertEqual(cli._prompt_float("m", 5.0), 3.14)

    def test_cli_daily_production_with_halted_lines(self):
        """Проверяет запуск смены при остановленной линии."""
        cli = PlantCli()
        cli.prod_line.is_running = False
        cli.work_station.is_active = False
        commands = ["1", "1", "0", "нет"]
        cli.run(auto_input=commands)

    def test_cli_manage_lines_extended_edge_cases(self):
        """Проверяет обработку ошибок управления линиями (нечисловой ввод, неактивные посты)."""
        cli = PlantCli()
        empty_line = ProductionLine("ЛИНИЯ-ТЕСТ", "Тестовая пустая линия")
        cli.plant.add_production_line(empty_line)
        commands = ["2", "1", "2", "abc", "2", "2", "2", "1", "abc", "2", "1", "2", "0", "нет"]
        cli.run(auto_input=commands)

    def test_cli_order_creation_edge_cases(self):
        """Проверяет создание наряда с 0 деталей и наряда с ошибкой."""
        cli = PlantCli()
        commands = ["3", "НАРЯД-000", "Деталь", "0", "3", "НАРЯД-999", "Сверхзаказ", "90000", "0", "нет"]
        cli.run(auto_input=commands)

    def test_cli_order_completion_not_in_production(self):
        """Проверяет сдачу наряда, статус которого еще не переведен в производство."""
        cli = PlantCli()
        plan = ProductionPlan("ПЛАН-NEW", planned_quantity=100, deadline_date="2026-10-30")
        new_order = ProductionOrder("НАРЯД-NEW", "Шестерня", 100, plan)
        new_order.status = "СОЗДАН"
        cli.plant.receive_production_order(new_order)
        commands = ["4", str(len(cli.plant.active_orders)), "0", "нет"]
        cli.run(auto_input=commands)
        self.assertEqual(new_order.status, "ВЫПОЛНЕН")

    def test_cli_warehouse_edge_cases(self):
        """Проверяет граничные условия склада (нулевая масса, переполнение ячейки)."""
        cli = PlantCli()
        commands = ["5", "1", "0", "5", "1", "999999.0", "5", "2", "0", "5", "2", "999999.0", "0", "нет"]
        cli.run(auto_input=commands)

    def test_cli_commercial_dispatch_zero_and_errors(self):
        """Проверяет нулевой объем, нулевую цену и ошибку отгрузки."""
        cli = PlantCli()
        commands = [
            "6", "КЛ-01", "Деталь", "0",
            "6", "КЛ-02", "Деталь", "100", "0.0",
            "6", "КЛ-03", "Деталь", "999999", "10.0",
            "0", "нет"
        ]
        cli.run(auto_input=commands)

    def test_cli_equipment_and_budget_zero_and_errors(self):
        """Проверяет ошибку оборотов ЧПУ и пополнение бюджета на 0 у.е."""
        cli = PlantCli()
        commands = ["8", "1", "-100", "9", "1", "0.0", "0", "нет"]
        cli.run(auto_input=commands)

    def test_cli_json_save_load_failures(self):
        """Проверяет обработку ошибок сохранения и загрузки JSON."""
        cli = PlantCli()
        cli.STATE_FILE_PATH = "Z:\\non_existent_drive_12345\\state.json"
        commands = ["13", "1", "13", "2", "0", "нет"]
        cli.run(auto_input=commands)


if __name__ == "__main__":
    unittest.main()
