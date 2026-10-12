"""Базовый сотрудник автокомпонентного завода."""

from __future__ import annotations
from plant.core.contact_info import ContactInfo

class Employee:
    """Описывает штатную единицу завода, систему оплаты труда и контактные реквизиты."""

    def __init__(
        self,
        employee_id: str,
        full_name: str,
        position: str,
        salary: float,
        contact_info: ContactInfo
    ) -> None:
        # Табельный номер сотрудника
        self.employee_id = employee_id
        # Фамилия, имя, отчество
        self.full_name = full_name
        # Должность по штатному расписанию
        self.position = position
        # Месячный должностной оклад
        self.salary = salary
        # Контактные данные работника (Ассоциация)
        self.contact_info = contact_info

    def calculate_annual_bonus(self, kpi_score: float) -> float:
        """Рассчитывает годовую премию в зависимости от коэффициента выполнения KPI (0.0 - 2.0)."""
        clamped_kpi = max(0.0, min(2.0, kpi_score))
        return round(self.salary * clamped_kpi, 2)

    def promote(self, new_position: str, raise_percent: float) -> None:
        """Переводит сотрудника на новую должность с индексацией оклада."""
        if raise_percent < 0:
            raise ValueError("Процент повышения не может быть отрицательным")
        self.position = new_position
        self.salary = round(self.salary * (1.0 + (raise_percent / 100.0)), 2)

    def is_management(self) -> bool:
        """Определяет, относится ли должность к руководящему составу завода."""
        mgmt_keywords = ["директор", "начальник", "мастер", "supervisor", "руководитель"]
        return any(keyword in self.position.lower() for keyword in mgmt_keywords)
