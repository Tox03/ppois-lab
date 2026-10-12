"""Поршень автомобильного двигателя внутреннего сгорания."""

from __future__ import annotations
from plant.parts.auto_part import AutoPart

class EnginePiston:
    """Описывает поршень цилиндропоршневой группы ДВС с юбкой и канавками колец."""

    def __init__(
        self,
        auto_part: AutoPart,
        piston_diameter_mm: float,
        compression_height_mm: float,
        coating_type: str = "Молибден-графит",
        ring_groove_count: int = 3
    ) -> None:
        # Базовый паспорт автодетали (Ассоциация: AutoPart)
        self.auto_part = auto_part
        # Номинальный диаметр юбки поршня в мм
        self.piston_diameter_mm = piston_diameter_mm
        # Компрессионная высота от оси пальца до днища в мм
        self.compression_height_mm = compression_height_mm
        # Антифрикционное покрытие юбки
        self.coating_type = coating_type
        # Количество канавок под поршневые кольца (компрессионные + маслосъемные)
        self.ring_groove_count = ring_groove_count

    def check_bore_clearance(self, cylinder_bore_mm: float) -> float:
        """Рассчитывает монтажный тепловой зазор между юбкой поршня и гильзой блока."""
        clearance = cylinder_bore_mm - self.piston_diameter_mm
        if clearance < 0.02 or clearance > 0.08:
            # Зазор вне допуска (20-80 мкм)
            self.auto_part.is_defect_free = False
        return round(clearance, 4)

    def calculate_thermal_expansion(self, temp_rise_c: float, expansion_coef: float = 0.000022) -> float:
        """Рассчитывает температурное увеличение диаметра поршня при нагреве в камере сгорания."""
        delta = self.piston_diameter_mm * expansion_coef * temp_rise_c
        return round(delta, 4)

    def is_forged(self) -> bool:
        """Определяет, изготовлен ли поршень методом горячей объемной штамповки (ковка)."""
        return "кованый" in self.auto_part.part_name.lower()
