"""Гидравлический/газонаполненный автомобильный амортизатор."""

from __future__ import annotations
from plant.parts.auto_part import AutoPart

class ShockAbsorber:
    """Описывает стойку подвески или амортизатор с характеристиками демпфирования."""

    def __init__(
        self,
        auto_part: AutoPart,
        damping_force_n: float,
        stroke_length_mm: float,
        gas_pressure_bar: float,
        is_pressurized: bool = True
    ) -> None:
        # Базовый паспорт автодетали (Ассоциация: AutoPart)
        self.auto_part = auto_part
        # Сила сопротивления отбоя/сжатия в ньютонах (Н)
        self.damping_force_n = damping_force_n
        # Полный рабочий ход штока в мм
        self.stroke_length_mm = stroke_length_mm
        # Давление газового подпора азота в барах
        self.gas_pressure_bar = gas_pressure_bar
        # Статус герметичности газовой камеры
        self.is_pressurized = is_pressurized

    def test_damping_performance(self, compression_speed_mps: float) -> float:
        """Рассчитывает эффективное усилие гашения колебаний на динамометрическом стенде."""
        effective_force = self.damping_force_n * (compression_speed_mps ** 0.8)
        return round(effective_force, 2)

    def recharge_gas(self, pressure_bar: float) -> None:
        """Производит закачку азота под давлением через донный клапан."""
        if pressure_bar <= 0:
            raise ValueError("Давление газа должно быть положительным")
        self.gas_pressure_bar = pressure_bar
        self.is_pressurized = True

    def is_leak_free(self) -> bool:
        """Проверяет отсутствие утечек рабочей жидкости по штоку."""
        return self.is_pressurized and self.gas_pressure_bar >= 15.0
