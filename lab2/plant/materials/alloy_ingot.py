"""Слиток литейного сплава для фасонного литья компонентов ДВС."""

from __future__ import annotations
from plant.materials.raw_material import RawMaterial

class AlloyIngot:
    """Описывает чушку цветного или черного сплава для плавильной печи цеха литья."""

    def __init__(
        self,
        ingot_id: str,
        alloy_composition: str,
        melting_temperature_c: float,
        weight_kg: float,
        raw_material: RawMaterial
    ) -> None:
        # Номер плавки слитка
        self.ingot_id = ingot_id
        # Химический состав сплава (например, Al-Si9-Cu3)
        self.alloy_composition = alloy_composition
        # Температура плавления в градусах Цельсия
        self.melting_temperature_c = melting_temperature_c
        # Масса слитка в кг
        self.weight_kg = weight_kg
        # Ссылка на базовый тип сырья (Ассоциация)
        self.raw_material = raw_material

    def check_furnace_compatibility(self, furnace_max_temp_c: float) -> bool:
        """Проверяет, способна ли заводская печь расплавить данный сплав с запасом 50°C."""
        return furnace_max_temp_c >= (self.melting_temperature_c + 50.0)

    def calculate_casting_yield(self, scrap_ratio: float = 0.08) -> float:
        """Рассчитывает полезный вес годного литья с учетом технологического угара и литников."""
        if scrap_ratio < 0 or scrap_ratio >= 1.0:
            raise ValueError("Доля угара должна находиться в диапазоне [0, 1)")
        return round(self.weight_kg * (1.0 - scrap_ratio), 2)

    def is_high_temp_alloy(self) -> bool:
        """Определяет, относится ли сплав к жаропрочным/высокотемпературным (>1100°C)."""
        return self.melting_temperature_c > 1100.0
