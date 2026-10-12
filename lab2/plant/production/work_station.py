"""Рабочий пост / станция производственного конвейера."""

from __future__ import annotations
from typing import Optional
from plant.equipment.machine import Machine
from plant.personnel.machine_operator import MachineOperator

class WorkStation:
    """Объединяет станок, оснастку и закрепленного оператора в единую рабочую ячейку."""

    def __init__(
        self,
        station_id: str,
        machine: Machine,
        operator: Optional[MachineOperator] = None,
        is_active: bool = False
    ) -> None:
        # Номер рабочего поста на линии (например, СТ-01, СТ-02)
        self.station_id = station_id
        # Установленное оборудование (Ассоциация: Machine)
        self.machine = machine
        # Дежурный оператор поста (Ассоциация: MachineOperator)
        self.operator = operator
        # Флаг готовности поста к обработке потока деталей
        self.is_active = is_active

    def assign_operator(self, operator: MachineOperator) -> None:
        """Назначает сертифицированного оператора на пост и закрепляет за станком."""
        self.operator = operator
        operator.assign_machine(self.machine)
        self.is_active = True

    def release_station(self) -> None:
        """Освобождает рабочий пост при пересменке или плановой остановке."""
        self.operator = None
        self.is_active = False

    def process_part_cycle(self) -> bool:
        """Выполняет единичный технологический цикл обработки детали на посту."""
        if not self.is_active or self.operator is None:
            return False
        if not self.machine.is_operational:
            return False
        self.machine.record_hours(0.05)
        return True
