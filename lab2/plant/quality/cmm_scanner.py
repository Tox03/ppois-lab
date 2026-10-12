"""Координатно-измерительная машина (КИМ) 3D-контроля геометрии."""

from __future__ import annotations
from typing import Optional
from plant.parts.auto_part import AutoPart
from plant.quality.calibration_tool import CalibrationTool
from plant.exceptions.calibration_expired_exception import CalibrationExpiredException

class CmmScanner:
    """Осуществляет оптическое и контактное 3D-сканирование готовых автокомпонентов."""

    def __init__(
        self,
        scanner_id: str,
        precision_microns: float,
        calibration_tool: Optional[CalibrationTool] = None,
        points_scanned: int = 0
    ) -> None:
        # Серийный номер КИМ
        self.scanner_id = scanner_id
        # Паспортная точность измерений в микрометрах (мкм)
        self.precision_microns = precision_microns
        # Эталон поверки машины (Ассоциация: CalibrationTool)
        self.calibration_tool = calibration_tool
        # Суммарное количество снятых координатных точек
        self.points_scanned = points_scanned

    def calibrate(self, tool: CalibrationTool) -> None:
        """Привязывает поверочный эталон к измерительной системе КИМ."""
        self.calibration_tool = tool

    def scan_part_cloud(self, part: AutoPart, points_count: int) -> bool:
        """Выполняет трехмерное сканирование облака точек автодетали."""
        if self.calibration_tool is not None and not self.calibration_tool.is_calibrated:
            raise CalibrationExpiredException(self.scanner_id, 1)
        self.points_scanned += points_count
        # Проверяем деталь на отсутствие брака
        return part.is_defect_free

    def is_high_accuracy(self) -> bool:
        """Определяет, относится ли КИМ к прецизионному классу метрологии (<2 мкм)."""
        return self.precision_microns <= 2.0
