"""Электромагнитная форсунка системы впрыска топлива (инжектор)."""

from __future__ import annotations
from plant.parts.auto_part import AutoPart

class FuelInjector:
    """Описывает прецизионный распылитель бензина или дизельного топлива."""

    def __init__(
        self,
        auto_part: AutoPart,
        flow_rate_cc_min: float,
        spray_angle_deg: float,
        operating_pressure_bar: float,
        nozzle_holes_count: int = 6
    ) -> None:
        # Базовый паспорт автодетали (Ассоциация: AutoPart)
        self.auto_part = auto_part
        # Статическая производительность пролива в см³/мин
        self.flow_rate_cc_min = flow_rate_cc_min
        # Конусный угол распыления факела в градусах
        self.spray_angle_deg = spray_angle_deg
        # Номинальное давление топливной рампы в барах
        self.operating_pressure_bar = operating_pressure_bar
        # Количество микродюз распылителя
        self.nozzle_holes_count = nozzle_holes_count

    def test_spray_pattern(self, pattern_uniformity_score: float) -> bool:
        """Оценивает симметрию факела распыла на оптическом лазерном стенде."""
        is_ok = 0.85 <= pattern_uniformity_score <= 1.0
        if not is_ok:
            self.auto_part.is_defect_free = False
        return is_ok

    def calculate_fuel_delivery(self, pulse_width_ms: float) -> float:
        """Рассчитывает дозу топлива за один электрический импульс открытия иглы (см³)."""
        delivery_per_sec = self.flow_rate_cc_min / 60.0
        return round(delivery_per_sec * (pulse_width_ms / 1000.0), 5)

    def is_high_pressure_gdi(self) -> bool:
        """Определяет, предназначена ли форсунка для прямого непосредственного впрыска (>150 бар)."""
        return self.operating_pressure_bar >= 150.0
