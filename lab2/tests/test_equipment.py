"""Тесты для оборудования, станков, оснастки и датчиков."""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plant.equipment.machine import Machine
from plant.equipment.tooling_fixture import ToolingFixture
from plant.equipment.cutting_tool import CuttingTool
from plant.equipment.stamping_press import StampingPress
from plant.equipment.cnc_milling_machine import CncMillingMachine
from plant.equipment.welding_robot import WeldingRobot
from plant.equipment.painting_booth import PaintingBooth
from plant.equipment.heat_treatment_furnace import HeatTreatmentFurnace
from plant.equipment.laser_cutter import LaserCutter
from plant.equipment.equipment_sensor import EquipmentSensor
from plant.equipment.maintenance_log import MaintenanceLog
from plant.exceptions.equipment_overheat_exception import EquipmentOverheatException
from plant.exceptions.tool_wear_exceeded_exception import ToolWearExceededException
from plant.exceptions.machine_malfunction_exception import MachineMalfunctionException

class TestEquipmentSuite(unittest.TestCase):
    """Тестирует классы станков, ЧПУ, роботов, оснастки и мониторинга."""

    def test_machine_lifecycle(self):
        m = Machine("СТК-01", "HAAS-VF3", operating_hours=120.5, current_temperature=45.0, max_allowed_temp=80.0)
        m.start()
        m.record_hours(8.0)
        self.assertEqual(m.operating_hours, 128.5)
        m.stop()
        self.assertLess(m.current_temperature, 45.0)

        m.current_temperature = 85.0
        with self.assertRaises(EquipmentOverheatException):
            m.start()
        with self.assertRaises(ValueError):
            m.record_hours(-5.0)
        m_broken = Machine("СТК-СЛОМАН", "HAAS", 10.0, 20.0, is_operational=False)
        with self.assertRaises(MachineMalfunctionException):
            m_broken.start()

    def test_tooling_fixture_and_cutting_tool(self):
        fixture = ToolingFixture("ШТАМП-01", "Вырубной", 999, 1000)
        self.assertAlmostEqual(fixture.get_wear_ratio(), 0.999, places=3)
        with self.assertRaises(ToolWearExceededException):
            fixture.increment_cycles(2)
        self.assertTrue(fixture.is_worn_out)
        fixture.refurbish()
        self.assertEqual(fixture.cycles_used, 0)
        self.assertFalse(fixture.is_worn_out)

        tool = CuttingTool("ФРЕЗА-Ф12", "ВК8", 0.1, max_wear_limit_mm=0.3)
        self.assertTrue(tool.is_usable())
        tool.apply_cut_wear(0.1)
        self.assertEqual(tool.flank_wear_mm, 0.2)
        with self.assertRaises(ValueError):
            tool.apply_cut_wear(-0.1)
        with self.assertRaises(ToolWearExceededException):
            tool.apply_cut_wear(0.15)
        tool.regrind()
        self.assertTrue(tool.is_usable())

    def test_stamping_press_and_cnc(self):
        m1 = Machine("ПРЕСС-БАЗА", "AIDA-500", 10.0, 30.0)
        press = StampingPress(500.0, 200.0, m1)
        fixture = ToolingFixture("ШТ-02", "Вытяжной", 0, 5000)
        press.install_die(fixture)
        self.assertTrue(press.execute_stroke())
        self.assertEqual(press.parts_stamped, 1)

        m2 = Machine("ЧПУ-БАЗА", "DMG-MORI", 50.0, 30.0)
        cnc = CncMillingMachine(5, 8000, m2)
        tool = CuttingTool("ТОРЕЦ-D50", "Твердосплав", 0.05)
        cnc.mount_tool(tool)
        self.assertTrue(cnc.mill_contour(1200.0, 5.0))
        cnc.set_spindle_speed(12000)
        self.assertEqual(cnc.spindle_rpm, 12000)

        with self.assertRaises(ValueError):
            cnc.set_spindle_speed(50)
        with self.assertRaises(ValueError):
            cnc.set_spindle_speed(50000)

        bad_tool = CuttingTool("ФРЕЗА-ИЗНОС", "ВК8", 0.5, 0.3, is_sharp=False)
        with self.assertRaises(MachineMalfunctionException):
            cnc.mount_tool(bad_tool)

        m2.is_operational = False
        with self.assertRaises(MachineMalfunctionException):
            cnc.mill_contour(500.0, 2.0)

        cnc_no_tool = CncMillingMachine(3, 3000, m1, active_tool=None)
        with self.assertRaises(MachineMalfunctionException):
            cnc_no_tool.mill_contour(500.0, 2.0)

    def test_welding_and_painting(self):
        m_weld = Machine("РОБОТ-СВАРКА", "KUKA-KR16", 100.0, 30.0)
        robot = WeldingRobot(220.0, 15.0, m_weld, "Св-08Г2С")
        robot.ignite_arc()
        self.assertTrue(robot.arc_ignited)
        robot.extinguish_arc()
        self.assertFalse(robot.arc_ignited)
        duration = robot.perform_seam_weld(30.0)
        self.assertGreater(duration, 0)
        m_weld.is_operational = False
        with self.assertRaises(MachineMalfunctionException):
            robot.ignite_arc()

        m_weld_ok = Machine("РОБОТ-2", "KUKA", 10.0, 20.0)
        low_gas_robot = WeldingRobot(220.0, 5.0, m_weld_ok, "Св-08Г2С")
        with self.assertRaises(MachineMalfunctionException):
            low_gas_robot.ignite_arc()

        m_paint = Machine("ПОКРАСКА-БАЗА", "WAGNER-PXE", 20.0, 25.0)
        booth = PaintingBooth(0.4, "RAL 9005", 45.0, m_paint)
        self.assertTrue(booth.apply_powder_coat(65.0))
        self.assertTrue(booth.bake_paint(200.0, 15.0))
        booth.ventilate()
        with self.assertRaises(ValueError):
            booth.bake_paint(150.0, 10.0)
        with self.assertRaises(ValueError):
            booth.bake_paint(300.0, 10.0)
        m_paint.is_operational = False
        with self.assertRaises(MachineMalfunctionException):
            booth.apply_powder_coat(50.0)
        m_booth_ok = Machine("ПОКРАСКА-ОК", "WAGNER", 10.0, 20.0, is_operational=True)
        humid_booth = PaintingBooth(0.4, "RAL 9005", 85.0, m_booth_ok)
        with self.assertRaises(MachineMalfunctionException):
            humid_booth.apply_powder_coat(50.0)

    def test_furnace_and_laser(self):
        m_furnace = Machine("ПЕЧЬ-01", "NABERTHERM", 300.0, 20.0)
        furnace = HeatTreatmentFurnace(860.0, "Закалочное масло", 45.0, m_furnace)
        self.assertIn("холодная", furnace.quench())
        furnace.heat_to_target(900.0)
        self.assertIn("Закалка выполнена", furnace.quench())
        self.assertTrue(furnace.perform_hardening_cycle(60.0))
        with self.assertRaises(EquipmentOverheatException):
            furnace.heat_to_target(1300.0)

        m_laser = Machine("ЛАЗЕР-01", "TRUMPF-TruLaser", 50.0, 25.0)
        laser = LaserCutter(6000.0, 15.0, m_laser)
        cut_time = laser.cut_sheet_profile(30.0)
        self.assertGreater(cut_time, 0)
        laser.set_power(8000.0)
        self.assertEqual(laser.laser_power_watts, 8000.0)
        with self.assertRaises(ValueError):
            laser.set_power(100.0)
        laser.beam_focused = False
        with self.assertRaises(MachineMalfunctionException):
            laser.cut_sheet_profile(10.0)
        laser.focus_beam()
        m_laser.is_operational = False
        with self.assertRaises(MachineMalfunctionException):
            laser.cut_sheet_profile(10.0)

    def test_stamping_press_edge_cases(self):
        m = Machine("ПРЕСС-02", "AIDA", 10.0, 20.0, is_operational=True)
        press = StampingPress(300.0, 150.0, m)
        self.assertTrue(press.calibrate_pressure(250.0))
        with self.assertRaises(ValueError):
            press.calibrate_pressure(400.0)
        with self.assertRaises(MachineMalfunctionException):
            press.execute_stroke()
        worn_die = ToolingFixture("ШТ-ВЫР", "Вырубка", 100, 100, is_worn_out=True)
        with self.assertRaises(MachineMalfunctionException):
            press.install_die(worn_die)

    def test_sensor_and_maintenance_log(self):
        m = Machine("СТ-10", "СТАНОК", 10.0, 30.0)
        sensor = EquipmentSensor("ДАТЧИК-ВИБР", "Вибрация RMS", 1.2, 4.5, m)
        sensor.read_value(2.8)
        self.assertFalse(sensor.is_threshold_exceeded())
        sensor.read_value(5.0)
        self.assertTrue(sensor.is_threshold_exceeded())
        sensor.calibrate_offset(1.0)
        self.assertEqual(sensor.last_reading, 4.0)

        log = MaintenanceLog("ТО-001", m, "2026-05-10", "Иванов И.И.", "Замена масла")
        log.log_service_event("Проверка зазоров шпинделя")
        self.assertTrue(log.is_recent_service("2026"))
        self.assertIn("Замена масла", log.format_entry())

if __name__ == "__main__":
    unittest.main()
