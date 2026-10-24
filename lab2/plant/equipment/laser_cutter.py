"""Оптоволоконный комплекс лазерного раскроя листового металла."""

from __future__ import annotations
from plant.equipment.machine import Machine
from plant.exceptions.machine_malfunction_exception import MachineMalfunctionException

class LaserCutter:
    """Осуществляет прецизионную контурную резку листовых заготовок."""

    def __init__(
        self,
        laser_power_watts: float,
        cutting_speed_m_per_min: float,
        machine: Machine,
        assist_gas: str = "Азот",
        beam_focused: bool = True
    ) -> None:
        # Мощность волоконного лазерного источника в ваттах (например, 6000 Вт)
        self.laser_power_watts = laser_power_watts
        # Скорость резки металлического листа в м/мин
        self.cutting_speed_m_per_min = cutting_speed_m_per_min
        # Базовый координатный станок (Ассоциация)
        self.machine = machine
        # Вспомогательный продувочный газ (Азот высокой чистоты или Кислород)
        self.assist_gas = assist_gas
        # Статус юстировки фокуса оптической головки
        self.beam_focused = beam_focused

    def focus_beam(self) -> None:
        """Выполняет автофокусировку линзы на поверхность металла."""
        self.beam_focused = True

    def cut_sheet_profile(self, length_meters: float) -> float:
        """Выполняет раскрой контура листа заданной длины и возвращает время в секундах."""
        if not self.machine.is_operational:
            raise MachineMalfunctionException(self.machine.machine_id, "Лазерный комплекс отключен")
        if not self.beam_focused:
            raise MachineMalfunctionException(self.machine.machine_id, "Оптический луч расфокусирован")
        
        minutes = length_meters / max(0.1, self.cutting_speed_m_per_min)
        self.machine.record_hours(minutes / 60.0)
        self.machine.current_temperature += minutes * 0.1
        self.machine.check_overheat()
        return round(minutes * 60.0, 2)

    def set_power(self, watts: float) -> None:
        """Регулирует излучаемую мощность лазерного резонатора."""
        if watts < 500.0 or watts > 12000.0:
            raise ValueError(f"Мощность {watts} Вт вне рабочего диапазона источника")
        self.laser_power_watts = watts
