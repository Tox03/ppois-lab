"""Инженер службы главного механика и энергетика."""

from __future__ import annotations
from typing import Optional
from plant.personnel.employee import Employee
from plant.equipment.machine import Machine

class MaintenanceEngineer:
    """Обеспечивает безаварийную эксплуатацию, ремонт и калибровку производственных линий."""

    def __init__(
        self,
        employee: Employee,
        certification_level: str,
        repairs_performed: int = 0,
        active_repair_machine: Optional[Machine] = None
    ) -> None:
        # Профиль сотрудника (Ассоциация)
        self.employee = employee
        # Уровень квалификационной аттестации (I, II, Эксперт)
        self.certification_level = certification_level
        # Количество успешно выполненных ремонтов
        self.repairs_performed = repairs_performed
        # Станок, находящийся в текущем ремонте (Ассоциация: Machine)
        self.active_repair_machine = active_repair_machine

    def perform_preventive_maintenance(self, machine: Machine) -> bool:
        """Проводит регламентное ТО оборудования: смазка, замена фильтров, проверка люфтов."""
        machine.operating_hours = max(0.0, machine.operating_hours)
        machine.current_temperature = 22.0
        machine.is_operational = True
        self.repairs_performed += 1
        return True

    def repair_breakdown(self, machine: Machine, failure_desc: str) -> None:
        """Устраняет аварийный отказ узлов станка и возвращает его в строй."""
        self.active_repair_machine = machine
        machine.is_operational = True
        machine.current_temperature = 25.0
        self.repairs_performed += 1
        self.active_repair_machine = None

    def is_expert(self) -> bool:
        """Определяет допуск к капремонту 5-осевых центров с ЧПУ."""
        return self.certification_level.lower() == "эксперт" or self.repairs_performed >= 50
