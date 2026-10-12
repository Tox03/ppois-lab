"""Коммерческий заказ автокомпонентов от автопроизводителя."""

from __future__ import annotations
from typing import Dict
from plant.logistics.customer import Customer

class CustomerOrder:
    """Оформляет спецификацию поставки партии автокомпонентов заказчику."""

    def __init__(
        self,
        order_id: str,
        customer: Customer,
        total_price: float = 0.0,
        is_dispatched: bool = False
    ) -> None:
        # Номер внешнего коммерческого контракта/заказа
        self.order_id = order_id
        # Контрагент-заказчик (Ассоциация: Customer)
        self.customer = customer
        # Состав заказа: наименование детали -> количество (шт.)
        self.requested_parts: Dict[str, int] = {}
        # Суммарная стоимость заказа без скидки
        self.total_price = total_price
        # Статус фактической отгрузки со склада готовой продукции
        self.is_dispatched = is_dispatched

    def add_part_order(self, part_name: str, quantity: int, unit_price: float) -> None:
        """Добавляет номенклатурную позицию в заказ и обновляет итоговую сумму."""
        if quantity <= 0 or unit_price < 0:
            raise ValueError("Некорректное количество или цена единицы")
        current_qty = self.requested_parts.get(part_name, 0)
        self.requested_parts[part_name] = current_qty + quantity
        self.total_price = round(self.total_price + (quantity * unit_price), 2)

    def dispatch(self) -> None:
        """Подтверждает отгрузку сформированного заказа в транспортную компанию."""
        if not self.requested_parts:
            raise RuntimeError("Нельзя отгрузить пустой заказ без позиций")
        self.is_dispatched = True

    def calculate_final_price(self) -> float:
        """Рассчитывает итоговую сумму с учетом клиентской скидки по договору."""
        discounted = self.total_price * (1.0 - self.customer.discount_rate)
        return round(discounted, 2)
