"""Выпускной коллектор двигателя из жаропрочного чугуна или нержавеющей стали."""

from __future__ import annotations
from plant.parts.auto_part import AutoPart

class ExhaustManifold:
    """Описывает многоканальный коллектор отвода отработавших газов."""

    def __init__(
        self,
        auto_part: AutoPart,
        runner_count: int,
        max_operating_temp_c: float,
        is_leak_tested: bool = False,
        wall_thickness_mm: float = 3.5
    ) -> None:
        # Базовый паспорт автодетали (Ассоциация: AutoPart)
        self.auto_part = auto_part
        # Количество выпускных патрубков (раннеров) по числу цилиндров
        self.runner_count = runner_count
        # Предельная рабочая температура выхлопных газов (°C)
        self.max_operating_temp_c = max_operating_temp_c
        # Отметка об опрессовке на герметичность
        self.is_leak_tested = is_leak_tested
        # Минимальная толщина стенки литья в мм
        self.wall_thickness_mm = wall_thickness_mm

    def perform_pressure_leak_test(self, test_pressure_bar: float) -> bool:
        """Проводит пневмоиспытание под водой на герметичность швов и отсутствие микропор."""
        if test_pressure_bar >= 2.0:
            self.is_leak_tested = True
            return True
        return False

    def verify_thermal_resistance(self, exhaust_gas_temp_c: float) -> bool:
        """Проверяет термостойкость коллектора в условиях максимальной мощности мотора."""
        resistant = exhaust_gas_temp_c <= self.max_operating_temp_c
        if not resistant:
            self.auto_part.is_defect_free = False
        return resistant

    def is_equal_length_runner(self) -> bool:
        """Определяет равнодлинную спортивную конфигурацию коллектора («паук»)."""
        return "паук" in self.auto_part.part_name.lower() or "спорт" in self.auto_part.part_name.lower()
