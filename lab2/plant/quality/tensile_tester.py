"""Универсальная разрывная испытательная машина прочности металлов."""

from __future__ import annotations
from typing import Optional
from plant.core.technical_specification import TechnicalSpecification
from plant.quality.calibration_tool import CalibrationTool
from plant.exceptions.calibration_expired_exception import CalibrationExpiredException

class TensileTester:
    """Проводит механические испытания образцов на предел прочности и текучести."""

    def __init__(
        self,
        tester_id: str,
        max_force_kn: float,
        calibration_tool: Optional[CalibrationTool] = None,
        tests_executed: int = 0
    ) -> None:
        # Инвентарный номер испытательного стенда
        self.tester_id = tester_id
        # Максимальное развиваемое усилие растяжения в кН (например, 100 кН)
        self.max_force_kn = max_force_kn
        # Поверочный датчик силы (Ассоциация: CalibrationTool)
        self.calibration_tool = calibration_tool
        # Количество проведенных разрушающих испытаний
        self.tests_executed = tests_executed

    def calibrate(self, tool: CalibrationTool) -> None:
        """Регистрирует калибровку датчика силы стенда."""
        self.calibration_tool = tool

    def execute_pull_test(self, spec: TechnicalSpecification, measured_strength_mpa: float) -> bool:
        """
        Проводит испытание на разрыв и сопоставляет прочность со спецификацией детали.
        Ассоциация: TechnicalSpecification
        """
        if self.calibration_tool is not None and not self.calibration_tool.is_calibrated:
            raise CalibrationExpiredException(self.tester_id, 1)
        self.tests_executed += 1
        return spec.verify_strength(measured_strength_mpa)

    def get_utilization(self, max_monthly_tests: int = 500) -> float:
        """Возвращает процент загрузки испытательного стенда за текущий месяц."""
        if max_monthly_tests <= 0:
            return 100.0
        return round((self.tests_executed / max_monthly_tests) * 100.0, 2)
