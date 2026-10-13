"""Тесты для производственных линий, постов, смен и заказов."""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plant.core.contact_info import ContactInfo
from plant.equipment.machine import Machine
from plant.personnel.employee import Employee
from plant.personnel.machine_operator import MachineOperator
from plant.personnel.shift_supervisor import ShiftSupervisor
from plant.production.work_station import WorkStation
from plant.production.manufacturing_process import ManufacturingProcess
from plant.production.production_line import ProductionLine
from plant.production.work_shift import WorkShift
from plant.production.production_plan import ProductionPlan
from plant.production.production_order import ProductionOrder
from plant.production.energy_meter import EnergyMeter
from plant.production.scrap_record import ScrapRecord
from plant.exceptions.production_line_halt_exception import ProductionLineHaltException
from plant.exceptions.defect_threshold_exceeded_exception import DefectThresholdExceededException
from plant.exceptions.order_capacity_exceeded_exception import OrderCapacityExceededException

class TestProductionSuite(unittest.TestCase):
    """Тестирует классы производственного цикла цеха."""

    def setUp(self):
        self.ci = ContactInfo("dept@plant.by", "+375-17-100-20-30", "Цех 1")
        self.emp = Employee("ТН-10", "Алексеев А.", "Оператор", 2000.0, self.ci)
        self.operator = MachineOperator(self.emp, 4, safety_certified=True)
        self.machine = Machine("СТ-55", "ПРЕСС", 10.0, 25.0)

    def test_work_station(self):
        ws = WorkStation("ПОСТ-01", self.machine)
        self.assertFalse(ws.is_active)
        self.assertFalse(ws.process_part_cycle())
        ws.assign_operator(self.operator)
        self.assertTrue(ws.is_active)
        self.assertTrue(ws.process_part_cycle())
        self.machine.is_operational = False
        self.assertFalse(ws.process_part_cycle())
        self.machine.is_operational = True
        ws.release_station()
        self.assertFalse(ws.is_active)

    def test_manufacturing_process(self):
        proc = ManufacturingProcess("Штамповка днища", duration_minutes=1.5, energy_consumption_kwh=2.4)
        cost = proc.calculate_power_cost(0.15)
        self.assertAlmostEqual(cost, 0.36, places=2)
        proc.optimize_duration(0.1)
        self.assertEqual(proc.duration_minutes, 1.35)
        self.assertFalse(proc.is_thermal_process())
        with self.assertRaises(ValueError):
            proc.calculate_power_cost(-1.0)
        with self.assertRaises(ValueError):
            proc.optimize_duration(2.0)

    def test_production_line_and_exceptions(self):
        line = ProductionLine("ЛИНИЯ-1", "Линия штамповки", max_allowed_scrap_pct=2.5)
        ws = WorkStation("ПОСТ-01", self.machine)
        ws.assign_operator(self.operator)
        line.add_station(ws)
        self.assertTrue(line.start_line())
        
        with self.assertRaises(ProductionLineHaltException):
            line.emergency_halt("Заклинивание податчика")

        with self.assertRaises(DefectThresholdExceededException):
            line.record_scrap(total_produced=100, total_defective=5)
        self.assertEqual(line.record_scrap(0, 0), 0.0)

    def test_work_shift(self):
        s_emp = Employee("ТН-20", "Сергеев С.", "Мастер", 2800.0, self.ci)
        supervisor = ShiftSupervisor(s_emp, "СМЕНА-ДЕНЬ", 10)
        shift = WorkShift("СМ-01", "ДНЕВНАЯ", supervisor, hours_duration=8.0)
        self.assertFalse(shift.is_night_shift())
        shift.hours_duration = 0.0
        self.assertEqual(shift.calculate_hourly_productivity(100), 0.0)
        self.assertIn("100", shift.record_shift_output(100))

    def test_production_plan_and_order(self):
        plan = ProductionPlan("ПЛАН-2026-10", planned_quantity=1000, deadline_date="2026-10-31")
        plan.register_output(400)
        self.assertEqual(plan.calculate_fulfillment_percentage(), 40.0)
        self.assertFalse(plan.is_plan_fulfilled())
        with self.assertRaises(ValueError):
            plan.register_output(-50)
        empty_plan = ProductionPlan("ПЛАН-0", planned_quantity=0, deadline_date="2026-10-31")
        self.assertEqual(empty_plan.calculate_fulfillment_percentage(), 100.0)

        order = ProductionOrder("НАРЯД-01", "Поршень ДВС", 500)
        order.link_plan(plan)
        with self.assertRaises(RuntimeError):
            order.complete_order()

        order.start_production(max_capacity=1000)
        self.assertEqual(order.status, "В_ПРОИЗВОДСТВЕ")
        order.complete_order()
        self.assertEqual(order.status, "ВЫПОЛНЕН")
        self.assertEqual(plan.completed_quantity, 900)

        bad_order = ProductionOrder("НАРЯД-99", "Вал КПП", 60000)
        with self.assertRaises(OrderCapacityExceededException):
            bad_order.start_production(max_capacity=50000)

    def test_energy_meter_and_scrap_record(self):
        meter = EnergyMeter("СЧЕТЧИК-ЦЕХ1", 100.0, 0.10)
        meter.record_consumption(50.0)
        self.assertEqual(meter.total_kwh, 150.0)
        self.assertEqual(meter.calculate_energy_bill(), 15.0)
        meter.reset_monthly_counter()
        self.assertEqual(meter.total_kwh, 0.0)
        with self.assertRaises(ValueError):
            meter.record_consumption(-10.0)

        scrap = ScrapRecord("АКТ-01", "Трещина после закалки", 12, "2026-10-12")
        self.assertEqual(scrap.calculate_financial_loss(50.0), 600.0)
        self.assertFalse(scrap.is_critical_scrap(50))
        with self.assertRaises(ValueError):
            scrap.calculate_financial_loss(-10.0)
        self.assertIn("АКТ-01", scrap.format_summary())

if __name__ == "__main__":
    unittest.main()
