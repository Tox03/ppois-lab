"""Геометрические размеры и допуски деталей."""

from __future__ import annotations

class Dimension:
    """Описывает габаритные размеры автомобильной детали и конструкторские допуски."""

    def __init__(self, length_mm: float, width_mm: float, height_mm: float, tolerance_mm: float = 0.05) -> None:
        # Длина детали в миллиметрах
        self.length_mm = length_mm
        # Ширина детали в миллиметрах
        self.width_mm = width_mm
        # Высота (или толщина) детали в миллиметрах
        self.height_mm = height_mm
        # Допустимое отклонение от номинала в миллиметрах
        self.tolerance_mm = tolerance_mm

    def calculate_volume_cm3(self) -> float:
        """Вычисляет расчетный объем параллелепипеда детали в кубических сантиметрах."""
        volume_mm3 = self.length_mm * self.width_mm * self.height_mm
        return volume_mm3 / 1000.0

    def is_within_tolerance(self, actual: Dimension) -> bool:
        """
        Проверяет, укладываются ли фактические измеренные размеры в поле допуска чертежа.
        Ассоциация: параметр actual другого экземпляра Dimension.
        """
        diff_l = abs(self.length_mm - actual.length_mm)
        diff_w = abs(self.width_mm - actual.width_mm)
        diff_h = abs(self.height_mm - actual.height_mm)
        return (diff_l <= self.tolerance_mm and
                diff_w <= self.tolerance_mm and
                diff_h <= self.tolerance_mm)

    def scale(self, factor: float) -> Dimension:
        """
        Масштабирует габаритные размеры с учетом коэффициента усадки металла при остывании.
        Возвращает новый экземпляр Dimension.
        """
        if factor <= 0.0:
            raise ValueError("Масштабный коэффициент должен быть положительным")
        return Dimension(
            length_mm=round(self.length_mm * factor, 3),
            width_mm=round(self.width_mm * factor, 3),
            height_mm=round(self.height_mm * factor, 3),
            tolerance_mm=self.tolerance_mm
        )
