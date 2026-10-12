"""Листовой металлопрокат для кузовных и штампованных деталей."""

from __future__ import annotations
from plant.materials.raw_material import RawMaterial

class MetalSheet:
    """Описывает листовой прокат, используемый на операциях вырубки и вытяжки."""

    def __init__(
        self,
        sheet_id: str,
        thickness_mm: float,
        steel_grade: str,
        is_galvanized: bool,
        raw_material: RawMaterial
    ) -> None:
        # Инвентарный номер металлического листа
        self.sheet_id = sheet_id
        # Толщина листа в миллиметрах
        self.thickness_mm = thickness_mm
        # Марка стали (например, 08Ю)
        self.steel_grade = steel_grade
        # Признак антикоррозийного цинкового покрытия
        self.is_galvanized = is_galvanized
        # Ссылка на исходный сырьевой материал (Ассоциация)
        self.raw_material = raw_material

    def calculate_sheet_mass(self, area_m2: float) -> float:
        """Рассчитывает вес металлического листа заданной площади раскроя."""
        if area_m2 <= 0:
            raise ValueError("Площадь должна быть строго больше нуля")
        # Переводим объем листа в см³: площадь в см² * толщина в см
        volume_cm3 = (area_m2 * 10000.0) * (self.thickness_mm / 10.0)
        return self.raw_material.estimate_mass_kg(volume_cm3)

    def check_formability(self) -> bool:
        """Проверяет пригодность листа для глубокой вытяжки на прессе."""
        deep_drawing_grades = ["08Ю", "08КП", "DC04", "DC06"]
        return self.steel_grade.upper() in deep_drawing_grades and self.thickness_mm <= 2.5

    def apply_galvanizing(self) -> None:
        """Проводит технологический процесс горячего оцинкования листа."""
        self.is_galvanized = True
