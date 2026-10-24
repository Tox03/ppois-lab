"""Календарно-плановое задание цеха."""

from __future__ import annotations

class ProductionPlan:
    """Определяет целевой объем производства компонентов к установленному сроку."""

    def __init__(
        self,
        plan_id: str,
        planned_quantity: int,
        deadline_date: str,
        completed_quantity: int = 0
    ) -> None:
        # Номер производственного плана
        self.plan_id = plan_id
        # Целевое плановое количество деталей в штуках
        self.planned_quantity = planned_quantity
        # Директивный срок выполнения плана
        self.deadline_date = deadline_date
        # Фактически произведенное количество годных деталей
        self.completed_quantity = completed_quantity

    def register_output(self, quantity: int) -> int:
        """Добавляет готовую продукцию к выполненному объему."""
        if quantity <= 0:
            raise ValueError("Количество выпущенной продукции должно быть положительным")
        self.completed_quantity += quantity
        return self.completed_quantity

    def calculate_fulfillment_percentage(self) -> float:
        """Рассчитывает процент фактического выполнения плана."""
        if self.planned_quantity <= 0:
            return 100.0
        return round((self.completed_quantity / self.planned_quantity) * 100.0, 2)

    def is_plan_fulfilled(self) -> bool:
        """Проверяет достижение планового норматива выпуска."""
        return self.completed_quantity >= self.planned_quantity
