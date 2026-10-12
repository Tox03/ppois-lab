"""Производственный наряд-заказ цеха."""

from __future__ import annotations
from typing import Optional
from plant.production.production_plan import ProductionPlan
from plant.exceptions.order_capacity_exceeded_exception import OrderCapacityExceededException

class ProductionOrder:
    """Оформляет запуск серии автодеталей в производственный процесс."""

    def __init__(
        self,
        order_id: str,
        target_part_type: str,
        quantity: int,
        status: str = "НОВЫЙ",
        production_plan: Optional[ProductionPlan] = None
    ) -> None:
        # Уникальный номер наряда-заказа
        self.order_id = order_id
        # Номенклатурный тип изготавливаемой детали
        self.target_part_type = target_part_type
        # Требуемый объем партии
        self.quantity = quantity
        # Статус заказа (НОВЫЙ, В_ПРОИЗВОДСТВЕ, ВЫПОЛНЕН, ОТМЕНЕН)
        self.status = status
        # Привязанный календарный план (Ассоциация: ProductionPlan)
        self.production_plan = production_plan

    def link_plan(self, plan: ProductionPlan) -> None:
        """Связывает производственный заказ со сводным планом выпуска."""
        self.production_plan = plan

    def start_production(self, max_capacity: int = 50000) -> None:
        """
        Переводит заказ в работу при наличии свободной мощности цеха.
        Выбрасывает OrderCapacityExceededException при превышении мощности.
        """
        if self.quantity > max_capacity:
            raise OrderCapacityExceededException(self.order_id, self.quantity, max_capacity)
        self.status = "В_ПРОИЗВОДСТВЕ"

    def complete_order(self) -> None:
        """Завершает выполнение наряда-заказа и передает продукцию в отдел логистики."""
        if self.status != "В_ПРОИЗВОДСТВЕ":
            raise RuntimeError("Нельзя завершить заказ, который не находится в производстве")
        self.status = "ВЫПОЛНЕН"
        if self.production_plan is not None:
            self.production_plan.register_output(self.quantity)
