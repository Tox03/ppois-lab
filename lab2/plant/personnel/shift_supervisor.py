"""Мастер производственной смены цеха."""

from __future__ import annotations
from plant.personnel.employee import Employee
from plant.personnel.machine_operator import MachineOperator
from plant.equipment.machine import Machine

class ShiftSupervisor:
    """Руководит бригадой операторов цеха, координирует выпуск сменного задания."""

    def __init__(
        self,
        employee: Employee,
        shift_code: str,
        team_size: int,
        active_shift_running: bool = False
    ) -> None:
        # Профиль сотрудника (Ассоциация)
        self.employee = employee
        # Код смены (например, СМЕНА-1-ДЕНЬ, СМЕНА-2-НОЧЬ)
        self.shift_code = shift_code
        # Численность подчиненной рабочей бригады
        self.team_size = team_size
        # Статус активной смены
        self.active_shift_running = active_shift_running

    def start_shift(self) -> None:
        """Открывает производственную смену после проведения сменного инструктажа."""
        self.active_shift_running = True

    def end_shift(self, units_produced: int) -> str:
        """Закрывает смену и формирует краткий сменный рапорт мастерской."""
        self.active_shift_running = False
        return f"Смена {self.shift_code} завершена бригадой из {self.team_size} чел. Выпущено изделий: {units_produced}"

    def reassign_operator(self, operator: MachineOperator, machine: Machine) -> None:
        """Оперативно перенаправляет оператора на свободный резервный станок."""
        operator.assign_machine(machine)
