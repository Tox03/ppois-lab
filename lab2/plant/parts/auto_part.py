"""Базовая готовая деталь или автокомпонент."""

from __future__ import annotations
from plant.core.dimension import Dimension
from plant.core.technical_specification import TechnicalSpecification
from plant.core.serial_number import SerialNumber
from plant.exceptions.quality_check_failed_exception import QualityCheckFailedException

class AutoPart:
    """Описывает базовые свойства автомобильной запчасти (геометрия, паспорт, ТУ)."""

    def __init__(
        self,
        part_number: str,
        serial_number: SerialNumber,
        part_name: str,
        dimension: Dimension,
        spec: TechnicalSpecification,
        is_defect_free: bool = True
    ) -> None:
        # Каталожный артикул детали
        self.part_number = part_number
        # Уникальный серийный номер изделия (Ассоциация: SerialNumber)
        self.serial_number = serial_number
        # Наименование узла/детали
        self.part_name = part_name
        # Номинальные габариты (Ассоциация: Dimension)
        self.dimension = dimension
        # Техническая спецификация чертежа (Ассоциация: TechnicalSpecification)
        self.spec = spec
        # Признак годности изделия (отсутствие брака)
        self.is_defect_free = is_defect_free

    def verify_dimensions(self, actual_dim: Dimension) -> bool:
        """
        Сверяет фактические измеренные размеры с полями допуска.
        Выбрасывает QualityCheckFailedException при выходе за поле допуска.
        """
        if not self.dimension.is_within_tolerance(actual_dim):
            self.is_defect_free = False
            raise QualityCheckFailedException(
                self.part_number,
                "Геометрические размеры",
                actual_dim.length_mm,
                self.dimension.length_mm
            )
        return True

    def mark_as_defective(self) -> None:
        """Переводит деталь в статус неисправимого брака и аннулирует серийный номер."""
        self.is_defect_free = False
        self.serial_number.deactivate()

    def get_part_label(self) -> str:
        """Формирует паспортную строку для штрихкода складской этикетки."""
        return f"{self.part_name} [{self.part_number}] SN:{self.serial_number.generate_code()}"
