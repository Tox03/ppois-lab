"""Журнал технического обслуживания и планово-предупредительного ремонта (ППР)."""

from __future__ import annotations
from plant.equipment.machine import Machine

class MaintenanceLog:
    """Фиксирует регламентные работы, замену расходников и аварийные ремонты станка."""

    def __init__(
        self,
        log_id: str,
        machine: Machine,
        maintenance_date: str,
        technician_name: str,
        description: str
    ) -> None:
        # Номер сервисного заказ-наряда
        self.log_id = log_id
        # Обслуживаемое оборудование (Ассоциация)
        self.machine = machine
        # Дата проведения регламента (ГГГГ-ММ-ДД)
        self.maintenance_date = maintenance_date
        # ФИО сервисного инженера или механика
        self.technician_name = technician_name
        # Описание выполненных операций и замененных деталей
        self.description = description

    def log_service_event(self, summary: str) -> None:
        """Добавляет запись о проведенных технологических операциях."""
        self.description = f"{self.description} | {summary}".strip(" |")

    def is_recent_service(self, current_year: str) -> bool:
        """Проверяет, проводилось ли обслуживание в текущем календарном году."""
        return self.maintenance_date.startswith(current_year)

    def format_entry(self) -> str:
        """Формирует паспортную запись о ремонте для архива завода."""
        return f"[{self.maintenance_date}] Станок {self.machine.machine_id}: {self.description} (Мастер: {self.technician_name})"
