"""Транспортное средство автоколонны заводской логистики (еврофура, грузовик)."""

from __future__ import annotations

class DeliveryVehicle:
    """Обеспечивает межзаводскую транспортировку паллет с готовыми деталями."""

    def __init__(
        self,
        vehicle_plate: str,
        carrying_capacity_tons: float,
        current_load_tons: float = 0.0,
        pallets_count: int = 0,
        is_ready: bool = True
    ) -> None:
        # Государственный регистрационный знак автомобиля
        self.vehicle_plate = vehicle_plate
        # Паспортная грузоподъемность в тоннах (например, 20.0 т)
        self.carrying_capacity_tons = carrying_capacity_tons
        # Текущий вес загруженных паллет в тоннах
        self.current_load_tons = current_load_tons
        # Число загруженных поддонов в полуприцеп
        self.pallets_count = pallets_count
        # Техническая готовность к дальнему рейсу
        self.is_ready = is_ready

    def load_pallet(self, pallet_weight_tons: float) -> bool:
        """Загружает один паллет в кузов с проверкой предельной грузоподъемности."""
        if not self.is_ready:
            raise RuntimeError(f"Транспорт {self.vehicle_plate} находится на ТО или неисправен")
        if self.current_load_tons + pallet_weight_tons > self.carrying_capacity_tons:
            return False
        self.current_load_tons = round(self.current_load_tons + pallet_weight_tons, 3)
        self.pallets_count += 1
        return True

    def depart_for_delivery(self) -> str:
        """Отправляет загруженный автопоезд в рейс по путевому листу."""
        if self.pallets_count == 0:
            raise RuntimeError("Нельзя отправлять в рейс порожний грузовик")
        self.is_ready = False
        return f"Автомобиль {self.vehicle_plate} убыл в рейс с {self.pallets_count} паллетами ({self.current_load_tons} т)"

    def get_load_factor(self) -> float:
        """Возвращает коэффициент полезного использования грузоподъемности (0.0 - 1.0)."""
        if self.carrying_capacity_tons <= 0:
            return 1.0
        return round(min(1.0, self.current_load_tons / self.carrying_capacity_tons), 3)
