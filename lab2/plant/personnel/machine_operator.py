"""Оператор производственного станка или робота."""

from __future__ import annotations
from typing import Optional
from plant.personnel.employee import Employee
from plant.equipment.machine import Machine
from plant.exceptions.safety_violation_exception import SafetyViolationException

class MachineOperator:
    """Управляет закрепленным станком, производит заготовки и соблюдает охрану труда."""

    def __init__(
        self,
        employee: Employee,
        qualification_rank: int,
        assigned_machine: Optional[Machine] = None,
        safety_certified: bool = False
    ) -> None:
        # Профиль сотрудника (Ассоциация)
        self.employee = employee
        # Квалификационный тарифный разряд (от 2 до 6)
        self.qualification_rank = qualification_rank
        # Закрепленный за оператором станок (Ассоциация: Machine)
        self.assigned_machine = assigned_machine
        # Наличие действующего удостоверения по технике безопасности
        self.safety_certified = safety_certified

    def assign_machine(self, machine: Machine) -> None:
        """Закрепляет оператора за конкретной единицей оборудования."""
        if not self.safety_certified:
            raise SafetyViolationException(
                self.employee.employee_id,
                "Попытка допуска к оборудованию без действующего инструктажа по ТБ",
                penalty_points=3
            )
        self.assigned_machine = machine

    def pass_safety_exam(self) -> None:
        """Фиксирует успешную сдачу ежегодного экзамена по технике безопасности."""
        self.safety_certified = True

    def produce_units(self, count: int) -> int:
        """
        Выполняет выпуск партии деталей за рабочую смену.
        Возвращает фактически изготовленное количество.
        """
        if self.assigned_machine is None or not self.assigned_machine.is_operational:
            return 0
        if count <= 0:
            return 0
        return count
