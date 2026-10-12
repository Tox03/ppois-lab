"""Отраслевой стандарт системы менеджмента качества автомобильной промышленности."""

from __future__ import annotations

class QualityStandard:
    """Описывает требования IATF 16949 / ISO 9001 к допускам и прочности автодеталей."""

    def __init__(
        self,
        standard_name: str,
        version: str,
        max_tolerance_deviation: float = 0.05,
        min_tensile_threshold: float = 400.0
    ) -> None:
        # Название стандарта (например, IATF 16949, VDA 6.3)
        self.standard_name = standard_name
        # Редакция стандарта
        self.version = version
        # Максимально допустимое поле погрешности в миллиметрах
        self.max_tolerance_deviation = max_tolerance_deviation
        # Минимальный базовый порог предела прочности металла (МПа)
        self.min_tensile_threshold = min_tensile_threshold

    def audit_dimension(self, deviation_mm: float) -> bool:
        """Проверяет соответствие геометрического отклонения нормам стандарта."""
        return abs(deviation_mm) <= self.max_tolerance_deviation

    def audit_strength(self, measured_strength_mpa: float) -> bool:
        """Проверяет соблюдение прочностного норматива для несущих элементов шасси."""
        return measured_strength_mpa >= self.min_tensile_threshold

    def is_automotive_certified(self) -> bool:
        """Определяет, относится ли стандарт к профильным автомобильным (IATF или VDA)."""
        name_lower = self.standard_name.lower()
        return "iatf" in name_lower or "vda" in name_lower
