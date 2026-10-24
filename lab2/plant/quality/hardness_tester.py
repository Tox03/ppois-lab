"""Стационарный твердомер (шкалы Роквелла HRC, Бринелля HB, Виккерса HV)."""

from __future__ import annotations
from typing import Optional
from plant.parts.gearbox_shaft import GearboxShaft
from plant.quality.calibration_tool import CalibrationTool
from plant.exceptions.calibration_expired_exception import CalibrationExpiredException

class HardnessTester:
    """Измеряет поверхностную твердость деталей после термообработки индентором."""

    def __init__(
        self,
        tester_id: str,
        method_type: str = "HRC_Роквелл",
        calibration_tool: Optional[CalibrationTool] = None,
        measurements_count: int = 0
    ) -> None:
        # Инвентарный номер прибора
        self.tester_id = tester_id
        # Метод испытания (HRC, HB, HV)
        self.method_type = method_type
        # Эталонная мера твердости (Ассоциация: CalibrationTool)
        self.calibration_tool = calibration_tool
        # Число выполненных уколов индентора
        self.measurements_count = measurements_count

    def calibrate(self, tool: CalibrationTool) -> None:
        """Проводит сверку показаний твердомера по эталонным плиткам твердости."""
        self.calibration_tool = tool

    def measure_hardness(self, shaft: GearboxShaft, measured_hrc: float) -> bool:
        """
        Выполняет измерение твердости зубьев вала коробки передач.
        Ассоциация: GearboxShaft.
        """
        if self.calibration_tool is not None and not self.calibration_tool.is_calibrated:
            raise CalibrationExpiredException(self.tester_id, 1)
        self.measurements_count += 1
        shaft.surface_hardness_hrc = measured_hrc
        return shaft.validate_hardness()

    def is_rockwell_method(self) -> bool:
        """Проверяет соответствие методики шкале вдавливания алмазного конуса HRC."""
        return "hrc" in self.method_type.lower() or "роквелл" in self.method_type.lower()
