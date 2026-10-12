"""Исключение при превышении вместимости складской зоны или стеллажной ячейки."""

from plant.exceptions.plant_base_exception import PlantBaseException

class StorageExhaustedException(PlantBaseException):
    """Вызывается при попытке складирования материала в переполненную ячейку хранения."""

    def __init__(self, bin_code: str, max_weight: float, attempted_weight: float) -> None:
        super().__init__(
            f"Переполнение ячейки '{bin_code}'! Лимит: {max_weight} кг, попытка загрузить: {attempted_weight} кг",
            error_code="ERR_STORAGE_EXHAUSTED"
        )
        # Код ячейки склада
        self.bin_code = bin_code
        # Максимальная грузоподъемность ячейки в кг
        self.max_weight = max_weight
        # Суммарный вес с учетом добавляемого материала
        self.attempted_weight = attempted_weight

    def get_excess_weight(self) -> float:
        """Возвращает вес превышения грузоподъемности ячейки."""
        return max(0.0, self.attempted_weight - self.max_weight)
