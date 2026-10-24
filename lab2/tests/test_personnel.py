"""Тесты для персонала завода: операторы, инженеры, мастера, руководство."""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plant.core.contact_info import ContactInfo
from plant.equipment.machine import Machine
from plant.equipment.cutting_tool import CuttingTool
from plant.equipment.tooling_fixture import ToolingFixture
from plant.personnel.employee import Employee
from plant.personnel.machine_operator import MachineOperator
from plant.personnel.quality_inspector import QualityInspector
from plant.personnel.maintenance_engineer import MaintenanceEngineer
from plant.personnel.toolmaker import Toolmaker
from plant.personnel.safety_officer import SafetyOfficer
from plant.personnel.shift_supervisor import ShiftSupervisor
from plant.personnel.plant_director import PlantDirector
from plant.exceptions.safety_violation_exception import SafetyViolationException

class TestPersonnelSuite(unittest.TestCase):
    """Тестирует классы персонала завода и трудовую логику."""

    def setUp(self):
        self.ci = ContactInfo("worker@plant.by", "+375-29-333-44-55", "Цех №1")
        self.emp = Employee("ТН-01", "Иванов Иван", "Оператор ЧПУ", 2000.0, self.ci)

    def test_employee_bonus_and_promotion(self):
        bonus = self.emp.calculate_annual_bonus(1.5)
        self.assertEqual(bonus, 3000.0)
        self.emp.promote("Старший оператор ЧПУ", 10.0)
        self.assertEqual(self.emp.salary, 2200.0)
        self.assertFalse(self.emp.is_management())

    def test_machine_operator(self):
        operator = MachineOperator(self.emp, 4)
        m = Machine("СТК-10", "СТАНОК", 10.0, 30.0)
        with self.assertRaises(SafetyViolationException):
            operator.assign_machine(m)
        operator.pass_safety_exam()
        operator.assign_machine(m)
        self.assertEqual(operator.produce_units(50), 50)

    def test_quality_inspector(self):
        insp_emp = Employee("ТН-02", "Петров П.П.", "Контролер ОТК", 2100.0, self.ci)
        inspector = QualityInspector(insp_emp, "ОТК-09")
        mark_good = inspector.inspect_part(True)
        mark_bad = inspector.inspect_part(False)
        self.assertIn("ПРИНЯТО", mark_good)
        self.assertIn("БРАК", mark_bad)
        inspector.add_certification("IATF 16949")
        self.assertEqual(inspector.get_rejection_rate(1), 50.0)
        insp_empty = QualityInspector(self.emp, "ОТК-00")
        self.assertEqual(insp_empty.get_rejection_rate(0), 0.0)

    def test_maintenance_engineer_and_toolmaker(self):
        maint_emp = Employee("ТН-03", "Сидоров С.С.", "Инженер-механик", 2500.0, self.ci)
        engineer = MaintenanceEngineer(maint_emp, "Эксперт")
        m = Machine("СТК-11", "СТАНОК", 50.0, 85.0, is_operational=False)
        self.assertTrue(engineer.perform_preventive_maintenance(m))
        self.assertTrue(m.is_operational)
        self.assertTrue(engineer.is_expert())
        engineer.repair_breakdown(m, "Аварийная замена муфты")
        self.assertEqual(m.current_temperature, 25.0)

        tool_emp = Employee("ТН-04", "Кузнецов К.К.", "Слесарь-инструментальщик", 2300.0, self.ci)
        toolmaker = Toolmaker(tool_emp, "Штампы")
        tool = CuttingTool("ФР-01", "ВК8", 0.25)
        toolmaker.regrind_cutting_tool(tool)
        self.assertEqual(tool.flank_wear_mm, 0.0)

        fixture = ToolingFixture("ШТ-09", "Литье", 500, 1000)
        self.assertTrue(toolmaker.verify_die_precision(fixture))
        toolmaker.refurbish_die(fixture)
        self.assertEqual(toolmaker.refurbished_tools_count, 2)

    def test_safety_officer_and_supervisor(self):
        safe_emp = Employee("ТН-05", "Васильев В.В.", "Инженер по ОТ", 2400.0, self.ci)
        officer = SafetyOfficer(safe_emp)
        with self.assertRaises(SafetyViolationException):
            officer.conduct_line_audit(False, "ТН-01")
        officer.conduct_line_audit(True, "ТН-01")
        officer.update_policy("ISO-45001-v3")
        self.assertEqual(officer.safety_policy_version, "ISO-45001-v3")
        self.assertIn("ПРЕДПИСАНИЕ", officer.issue_violation("ТН-01", "Работа без очков"))

        super_emp = Employee("ТН-06", "Смирнов С.С.", "Мастер смены", 2600.0, self.ci)
        supervisor = ShiftSupervisor(super_emp, "СМЕНА-1", 12)
        supervisor.start_shift()
        self.assertTrue(supervisor.active_shift_running)
        report = supervisor.end_shift(120)
        self.assertIn("120", report)
        m_extra = Machine("СТК-99", "РЕЗЕРВ", 10.0, 25.0)
        op_emp = Employee("ТН-01", "Иванов И.И.", "Оператор", 2000.0, self.ci)
        op = MachineOperator(op_emp, 4, safety_certified=True)
        self.assertEqual(op.produce_units(10), 0)
        supervisor.reassign_operator(op, m_extra)
        self.assertEqual(op.produce_units(0), 0)
        self.assertEqual(op.produce_units(-5), 0)
        self.assertEqual(op.produce_units(15), 15)

    def test_plant_director(self):
        dir_emp = Employee("ТН-00", "Федоров Ф.Ф.", "Генеральный директор", 6000.0, self.ci)
        director = PlantDirector(dir_emp, annual_budget=500000.0, strategic_plan_name="Модернизация 2026")
        self.assertTrue(director.authorize_line_expansion("Новая линия поршней", 150000.0))
        self.assertEqual(director.annual_budget, 350000.0)
        self.assertFalse(director.authorize_line_expansion("Сверхдорогой проект", 9999999.0))
        with self.assertRaises(ValueError):
            director.approve_budget_expense(-100.0, "Ошибка")
        self.assertIn("Федоров", director.sign_annual_report())

    def test_employee_edge_cases(self):
        with self.assertRaises(ValueError):
            self.emp.promote("Инженер", -10.0)
        self.emp.promote("Главный директор цеха", 5.0)
        self.assertTrue(self.emp.is_management())

if __name__ == "__main__":
    unittest.main()
