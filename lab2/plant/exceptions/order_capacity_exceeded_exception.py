"""Исключение при попытке запуска заказа, превышающего доступную мощность завода."""

from plant.exceptions.plant_base_exception import PlantBaseException

class OrderCapacityExceededException(PlantBaseException):
    """Вызывается при нехватке производственных мощностей цеха для выполнения заказа в срок."""

    def __init__(self, order_id: str, requested_volume: int, max_capacity: int) -> None:
        super().__init__(
            f"Заказ '{order_id}' превышает лимит мощности цеха: запрошено {requested_volume}, максимум {max_capacity}",
            error_code="ERR_ORDER_CAPACITY_EXCEEDED"
        )
        # Идентификатор заказа
        self.order_id = order_id
        # Запрошенный объем партии
        self.requested_volume = requested_volume
        # Максимальная пропускная способность цеха
        self.max_capacity = max_capacity

    def get_overflow_amount(self) -> int:
        """Возвращает количество единиц продукции, превышающее лимит мощности."""
        return max(0, self.requested_volume - self.max_capacity)
