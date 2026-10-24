"""Товарно-транспортная накладная (ТТН) и путевой лист отгрузки."""

from __future__ import annotations
from plant.logistics.customer_order import CustomerOrder
from plant.logistics.delivery_vehicle import DeliveryVehicle

class DispatchOrder:
    """Связывает коммерческий заказ с транспортом доставки и маршрутным листом."""

    def __init__(
        self,
        dispatch_id: str,
        customer_order: CustomerOrder,
        delivery_vehicle: DeliveryVehicle,
        departure_date: str,
        is_delivered: bool = False
    ) -> None:
        # Номер товарно-транспортной накладной (ТТН)
        self.dispatch_id = dispatch_id
        # Обеспечиваемый заказ покупателя (Ассоциация: CustomerOrder)
        self.customer_order = customer_order
        # Назначенный грузовой автомобиль (Ассоциация: DeliveryVehicle)
        self.delivery_vehicle = delivery_vehicle
        # Дата отправки рейса
        self.departure_date = departure_date
        # Статус вручения груза получателю
        self.is_delivered = is_delivered

    def confirm_delivery(self) -> None:
        """Подтверждает получение груза автосборочным предприятием с подписанием акта приема-передачи."""
        self.is_delivered = True
        self.delivery_vehicle.is_ready = True
        self.delivery_vehicle.current_load_tons = 0.0
        self.delivery_vehicle.pallets_count = 0

    def calculate_transport_cost(self, distance_km: float, rate_per_km: float = 1.8) -> float:
        """Рассчитывает логистические затраты на доставку партии автодеталей заказчику."""
        if distance_km < 0:
            raise ValueError("Расстояние рейса не может быть отрицательным")
        return round(distance_km * rate_per_km, 2)

    def generate_waybill(self) -> str:
        """Формирует текст товарно-транспортной накладной для водителя-экспедитора."""
        client_name = self.customer_order.customer.company_name
        plate = self.delivery_vehicle.vehicle_plate
        return f"ТТН №{self.dispatch_id} от {self.departure_date}: Груз для '{client_name}', Авто: {plate}"
