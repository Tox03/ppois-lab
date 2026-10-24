"""Базовое исходное сырье для металлообработки и литья."""

from __future__ import annotations

class RawMaterial:
    """Описывает свойства базового сырья (сталь, алюминиевый сплав, полимер)."""

    def __init__(self, material_id: str, name: str, density_g_cm3: float, base_cost_per_kg: float) -> None:
        # Уникальный артикул материала в номенклатуре
        self.material_id = material_id
        # Название марки материала (например, Сталь 40Х, АК7ч)
        self.name = name
        # Плотность сырья в г/см³
        self.density_g_cm3 = density_g_cm3
        # Базовая закупочная стоимость за килограмм (в у.е.)
        self.base_cost_per_kg = base_cost_per_kg

    def calculate_volume_cost(self, volume_cm3: float) -> float:
        """Рассчитывает стоимость заданного объема сырья с учетом плотности."""
        mass_kg = self.estimate_mass_kg(volume_cm3)
        return round(mass_kg * self.base_cost_per_kg, 2)

    def estimate_mass_kg(self, volume_cm3: float) -> float:
        """Оценивает массу заготовки в килограммах по ее объему."""
        if volume_cm3 < 0:
            raise ValueError("Объем не может быть отрицательным")
        mass_grams = volume_cm3 * self.density_g_cm3
        return round(mass_grams / 1000.0, 3)
