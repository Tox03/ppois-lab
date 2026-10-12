"""Генеральный директор завода по производству автомобильных деталей."""

from __future__ import annotations
from typing import List
from plant.personnel.employee import Employee

class PlantDirector:
    """Осуществляет общее стратегическое и финансовое руководство предприятием."""

    def __init__(
        self,
        employee: Employee,
        annual_budget: float,
        strategic_plan_name: str,
        approved_projects: List[str] = None
    ) -> None:
        # Профиль сотрудника (Ассоциация)
        self.employee = employee
        # Годовой операционный бюджет завода (в у.е.)
        self.annual_budget = annual_budget
        # Наименование утвержденного стратегического плана модернизации
        self.strategic_plan_name = strategic_plan_name
        # Перечень утвержденных инвестиционных проектов
        self.approved_projects = approved_projects if approved_projects is not None else []

    def approve_budget_expense(self, amount: float, purpose: str) -> bool:
        """Согласовывает крупную статью расходов в пределах доступного бюджета."""
        if amount <= 0:
            raise ValueError("Сумма расходов должна быть положительной")
        if amount > self.annual_budget:
            return False
        self.annual_budget = round(self.annual_budget - amount, 2)
        return True

    def authorize_line_expansion(self, project_name: str, investment_cost: float) -> bool:
        """Утверждает запуск проекта модернизации или расширения производственной линии."""
        if self.approve_budget_expense(investment_cost, f"Проект {project_name}"):
            self.approved_projects.append(project_name)
            return True
        return False

    def sign_annual_report(self) -> str:
        """Подписывает годовой аудиторский отчет завода."""
        return f"Отчет завода утвержден директором {self.employee.full_name}. Остаток бюджета: {self.annual_budget}"
