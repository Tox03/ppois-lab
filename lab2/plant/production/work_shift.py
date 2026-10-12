"""Рабочая производственная смена завода."""

from __future__ import annotations
from plant.personnel.shift_supervisor import ShiftSupervisor

class WorkShift:
    """Учитывает выработку за 8-часовую или 12-часовую рабочую смену."""

    def __init__(
        self,
        shift_id: str,
        shift_type: str,
        supervisor: ShiftSupervisor,
        hours_duration: float = 8.0
    ) -> None:
        # Идентификатор смены
        self.shift_id = shift_id
        # Тип смены (ДНЕВНАЯ, НОЧНАЯ, ВЕЧЕРНЯЯ)
        self.shift_type = shift_type.upper()
        # Начальник смены (Ассоциация: ShiftSupervisor)
        self.supervisor = supervisor
        # Продолжительность смены в часах
        self.hours_duration = hours_duration

    def record_shift_output(self, parts_count: int) -> str:
        """Регистрирует завершение смены с фиксацией итогового выпуска."""
        return self.supervisor.end_shift(parts_count)

    def calculate_hourly_productivity(self, total_parts: int) -> float:
        """Рассчитывает средний часовой темп выпуска (тактовое время)."""
        if self.hours_duration <= 0:
            return 0.0
        return round(total_parts / self.hours_duration, 2)

    def is_night_shift(self) -> bool:
        """Определяет, положена ли доплата за работу в ночные часы."""
        return "НОЧ" in self.shift_type
