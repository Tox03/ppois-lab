"""Тесты для контроля качества, калибровки и испытательных приборов."""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plant.core.dimension import Dimension
from plant.core.technical_specification import TechnicalSpecification
from plant.core.serial_number import SerialNumber
from plant.core.contact_info import ContactInfo
from plant.parts.auto_part import AutoPart
from plant.parts.gearbox_shaft import GearboxShaft
from plant.personnel.employee import Employee
from plant.personnel.quality_inspector import QualityInspector
from plant.quality.quality_standard import QualityStandard
from plant.quality.calibration_tool import CalibrationTool
from plant.quality.cmm_scanner import CmmScanner
from plant.quality.tensile_tester import TensileTester
from plant.quality.hardness_tester import HardnessTester
from plant.quality.defect_report import DefectReport
from plant.quality.inspection_report import InspectionReport
from plant.exceptions.calibration_expired_exception import CalibrationExpiredException

class TestQualitySuite(unittest.TestCase):
    """Тестирует классы ОТК, метрологии и отчетов качества."""

    def setUp(self):
        self.ci = ContactInfo("qc@plant.by", "+375-17-555-55-55", "ОТК")
        self.emp = Employee("ТН-50", "Орлов О.О.", "Инспектор", 2300.0, self.ci)
        self.inspector = QualityInspector(self.emp, "КЛЕЙМО-01")
        self.dim = Dimension(50.0, 50.0, 50.0)
        self.spec = TechnicalSpecification("СПЕЦ-01", "ISO-9001", 500.0, 1.2)
        self.sn = SerialNumber("TST", 2026, 99)
        self.part = AutoPart("АРТ-99", self.sn, "Тестовая деталь", self.dim, self.spec)

    def test_quality_standard(self):
        std = QualityStandard("IATF 16949", "2016", max_tolerance_deviation=0.03, min_tensile_threshold=450.0)
        self.assertTrue(std.audit_dimension(0.02))
        self.assertFalse(std.audit_dimension(0.05))
        self.assertTrue(std.audit_strength(500.0))
        self.assertTrue(std.is_automotive_certified())

    def test_calibration_tool_and_expiration(self):
        calib = CalibrationTool("ЭТАЛОН-01", "Набор мер длины", "2026-01-10", calibration_interval_days=180)
        self.assertTrue(calib.check_calibration_validity(100))
        with self.assertRaises(CalibrationExpiredException):
            calib.check_calibration_validity(200)
        calib.recalibrate("2026-10-12")
        self.assertTrue(calib.is_calibrated)
        self.assertIn("ГОДЕН", calib.format_calibration_tag())

    def test_cmm_scanner(self):
        calib_bad = CalibrationTool("ЭТАЛОН-ПЛОХОЙ", "Мера", "2020-01-01", 10, is_calibrated=False)
        scanner = CmmScanner("КИМ-01", precision_microns=1.5, calibration_tool=calib_bad)
        self.assertTrue(scanner.is_high_accuracy())
        with self.assertRaises(CalibrationExpiredException):
            scanner.scan_part_cloud(self.part, points_count=1000)
        calib_ok = CalibrationTool("ЭТАЛОН-ХОР", "Мера", "2026-01-01", 365)
        scanner.calibrate(calib_ok)
        self.assertTrue(scanner.scan_part_cloud(self.part, points_count=1000))
        self.assertEqual(scanner.points_scanned, 1000)

    def test_tensile_and_hardness_testers(self):
        calib_bad = CalibrationTool("МЕРА-ПРОСРОЧЕНА", "Датчик", "2020-01-01", 10, is_calibrated=False)
        tensile = TensileTester("РМ-100", max_force_kn=100.0, calibration_tool=calib_bad)
        with self.assertRaises(CalibrationExpiredException):
            tensile.execute_pull_test(self.spec, 550.0)
        calib_ok = CalibrationTool("ЭТАЛОН-СИЛЫ", "Датчик", "2026-01-01", 365)
        tensile.calibrate(calib_ok)
        self.assertTrue(tensile.execute_pull_test(self.spec, 550.0))
        self.assertEqual(tensile.tests_executed, 1)
        self.assertGreater(tensile.get_utilization(500), 0)
        self.assertEqual(tensile.get_utilization(0), 100.0)
        from plant.exceptions.invalid_specification_exception import InvalidSpecificationException
        with self.assertRaises(InvalidSpecificationException):
            tensile.execute_pull_test(self.spec, -10.0)

        hardness = HardnessTester("ТР-01", "HRC_Роквелл", calibration_tool=calib_bad)
        shaft = GearboxShaft(self.part, 25, 50.0, 16)
        with self.assertRaises(CalibrationExpiredException):
            hardness.measure_hardness(shaft, 60.0)
        calib_good = CalibrationTool("МЕРА-HRC", "Эталон Роквелла", "2026-01-01", 365)
        hardness.calibrate(calib_good)
        self.assertTrue(hardness.is_rockwell_method())
        self.assertTrue(hardness.measure_hardness(shaft, 60.0))

    def test_defect_and_inspection_reports(self):
        defect = DefectReport("БРАК-01", self.part, self.inspector, "Глубокая раковина", severity_level="КРИТИЧЕСКИЙ")
        self.assertEqual(defect.classify_disposition(), "УТИЛИЗАЦИЯ_В_БРАК")
        self.assertTrue(defect.is_scrap())
        self.assertFalse(self.part.is_defect_free)
        self.assertIn("БРАК-01", defect.format_ticket())

        defect2 = DefectReport("БРАК-02", self.part, self.inspector, "Заусенец", severity_level="УСТРАНИМЫЙ")
        self.assertEqual(defect2.classify_disposition(), "ВОЗВРАТ_НА_ДОРАБОТКУ")
        self.assertFalse(defect2.is_scrap())

        defect3 = DefectReport("БРАК-03", self.part, self.inspector, "Отклонение цвета", severity_level="НЕЗНАЧИТЕЛЬНЫЙ")
        self.assertEqual(defect3.classify_disposition(), "РАЗРЕШЕНО_С_ОТКЛОНЕНИЕМ")

        act = InspectionReport("АКТ-100", "ПАРТИЯ-50", self.inspector, passed_items=98, rejected_items=2)
        self.assertEqual(act.calculate_yield_rate(), 98.0)
        self.assertTrue(act.is_batch_acceptable(min_yield_rate=95.0))
        self.assertIn("АКТ-100", act.sign_report())

if __name__ == "__main__":
    unittest.main()
