"""Тесты для собственных классов исключений завода автодеталей."""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plant.exceptions.plant_base_exception import PlantBaseException
from plant.exceptions.material_defect_exception import MaterialDefectException
from plant.exceptions.raw_material_shortage_exception import RawMaterialShortageException
from plant.exceptions.equipment_overheat_exception import EquipmentOverheatException
from plant.exceptions.machine_malfunction_exception import MachineMalfunctionException
from plant.exceptions.quality_check_failed_exception import QualityCheckFailedException
from plant.exceptions.tool_wear_exceeded_exception import ToolWearExceededException
from plant.exceptions.production_line_halt_exception import ProductionLineHaltException
from plant.exceptions.safety_violation_exception import SafetyViolationException
from plant.exceptions.order_capacity_exceeded_exception import OrderCapacityExceededException
from plant.exceptions.calibration_expired_exception import CalibrationExpiredException
from plant.exceptions.invalid_specification_exception import InvalidSpecificationException
from plant.exceptions.storage_exhausted_exception import StorageExhaustedException
from plant.exceptions.defect_threshold_exceeded_exception import DefectThresholdExceededException

class TestExceptionsSuite(unittest.TestCase):
    """Набор тестов для проверки всех 14 специализированных исключений предметной области."""

    def test_plant_base_exception(self):
        exc = PlantBaseException("Общий сбой", "ERR_CODE_01")
        self.assertIn("ERR_CODE_01", exc.get_details())
        self.assertIn("Общий сбой", exc.get_details())

    def test_material_defect_exception(self):
        exc = MaterialDefectException("Сталь 45", "Неметаллические включения")
        self.assertIn("Сталь 45", exc.log_defect())
        self.assertIn("Неметаллические включения", exc.log_defect())

    def test_raw_material_shortage_exception(self):
        exc = RawMaterialShortageException("Алюминий", 100.0, 40.0)
        self.assertEqual(exc.calculate_deficit(), 60.0)

    def test_equipment_overheat_exception(self):
        exc = EquipmentOverheatException("СТАНОК-01", 95.0, 80.0)
        self.assertEqual(exc.get_excess_temp(), 15.0)

    def test_machine_malfunction_exception(self):
        exc = MachineMalfunctionException("ПРЕСС-01", "Клин ползуна", is_critical=True)
        self.assertTrue(exc.is_critical_failure())

    def test_quality_check_failed_exception(self):
        exc = QualityCheckFailedException("PST-001", "Диаметр", 82.55, 82.50)
        self.assertAlmostEqual(exc.get_deviation(), 0.05, places=4)

    def test_tool_wear_exceeded_exception(self):
        exc = ToolWearExceededException("ФРЕЗА-10", 0.35, 0.30)
        self.assertGreater(exc.get_wear_percentage(), 100.0)

    def test_production_line_halt_exception(self):
        exc = ProductionLineHaltException("ЛИНИЯ-1", "Разрыв конвейера", requires_evacuation=True)
        self.assertTrue(exc.requires_emergency_evacuation())

    def test_safety_violation_exception(self):
        exc1 = SafetyViolationException("РАБ-101", "Без каски", penalty_points=1)
        self.assertEqual(exc1.get_penalty_level(), "ПРЕДУПРЕЖДЕНИЕ")
        exc2 = SafetyViolationException("РАБ-102", "Вход в опасную зону", penalty_points=3)
        self.assertEqual(exc2.get_penalty_level(), "КРИТИЧЕСКИЙ_ОТСТРАНЕНИЕ")

    def test_order_capacity_exceeded_exception(self):
        exc = OrderCapacityExceededException("ЗАКАЗ-99", 70000, 50000)
        self.assertEqual(exc.get_overflow_amount(), 20000)

    def test_calibration_expired_exception(self):
        exc = CalibrationExpiredException("ШЦ-150", 10)
        self.assertTrue(exc.is_grace_period_exceeded())

    def test_invalid_specification_exception(self):
        exc = InvalidSpecificationException("ТУ-99", "Отрицательный предел прочности")
        self.assertIn("ТУ-99", exc.get_validation_report())

    def test_storage_exhausted_exception(self):
        exc = StorageExhaustedException("ЯЧ-01", 500.0, 620.0)
        self.assertEqual(exc.get_excess_weight(), 120.0)

    def test_defect_threshold_exceeded_exception(self):
        exc = DefectThresholdExceededException("ЛИНИЯ-2", 4.5, 2.0)
        self.assertAlmostEqual(exc.get_scrap_excess(), 2.5, places=2)

if __name__ == "__main__":
    unittest.main()
