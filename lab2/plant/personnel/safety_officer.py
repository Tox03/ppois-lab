"""Специалист по охране труда и производственной безопасности."""

from __future__ import annotations
from plant.personnel.employee import Employee
from plant.exceptions.safety_violation_exception import SafetyViolationException

class SafetyOfficer:
    """Контролирует соблюдение требований техники безопасности и пожарной безопасности."""

    def __init__(
        self,
        employee: Employee,
        inspections_conducted: int = 0,
        violations_reported: int = 0,
        safety_policy_version: str = "ISO-45001-v2"
    ) -> None:
        # Профиль сотрудника (Ассоциация)
        self.employee = employee
        # Количество проведенных рейдовых проверок цехов
        self.inspections_conducted = inspections_conducted
        # Количество зафиксированных нарушений ТБ
        self.violations_reported = violations_reported
        # Действующая версия регламента охраны труда
        self.safety_policy_version = safety_policy_version

    def conduct_line_audit(self, is_safe: bool, employee_id: str) -> None:
        """Проводит инспекцию рабочего поста цеха."""
        self.inspections_conducted += 1
        if not is_safe:
            self.violations_reported += 1
            raise SafetyViolationException(
                employee_id,
                "Нарушение регламента ношения средств индивидуальной защиты (СИЗ)",
                penalty_points=2
            )

    def issue_violation(self, violator_id: str, reason: str) -> str:
        """Оформляет официальное предписание об устранении нарушения ТБ."""
        self.violations_reported += 1
        return f"ПРЕДПИСАНИЕ: Работник {violator_id} допустил нарушение: '{reason}'. Провести внеплановый инструктаж."

    def update_policy(self, new_version: str) -> None:
        """Вводит в действие обновленные корпоративные стандарты охраны труда."""
        self.safety_policy_version = new_version
