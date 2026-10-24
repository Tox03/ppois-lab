"""Складская ячейка или бункер для хранения материалов."""

from __future__ import annotations
from plant.exceptions.storage_exhausted_exception import StorageExhaustedException

class StorageBin:
    """Описывает адресное место хранения (ячейку/бункер) на складе сырья завода."""

    def __init__(
        self,
        bin_code: str,
        max_weight_capacity_kg: float,
        current_weight_kg: float = 0.0,
        is_locked: bool = False
    ) -> None:
        # Адресный индекс ячейки (например, A-12-04)
        self.bin_code = bin_code
        # Предельная грузоподъемность ячейки в кг
        self.max_weight_capacity_kg = max_weight_capacity_kg
        # Текущий вес загруженного сырья в кг
        self.current_weight_kg = current_weight_kg
        # Флаг блокировки ячейки (на время ревизии или дезинфекции)
        self.is_locked = is_locked

    def deposit_material(self, weight_kg: float) -> None:
        """
        Загружает материал в ячейку.
        Выбрасывает StorageExhaustedException при превышении грузоподъемности.
        """
        if self.is_locked:
            raise RuntimeError(f"Ячейка {self.bin_code} заблокирована для размещения")
        if weight_kg <= 0:
            raise ValueError("Масса загрузки должна быть положительной")
        attempted = self.current_weight_kg + weight_kg
        if attempted > self.max_weight_capacity_kg:
            raise StorageExhaustedException(self.bin_code, self.max_weight_capacity_kg, attempted)
        self.current_weight_kg = round(attempted, 2)

    def withdraw_material(self, weight_kg: float) -> float:
        """Выгружает заданное количество материала из ячейки."""
        if weight_kg <= 0:
            raise ValueError("Масса выгрузки должна быть положительной")
        if weight_kg > self.current_weight_kg:
            raise ValueError(f"В ячейке {self.bin_code} недостаточно материала для выгрузки")
        self.current_weight_kg = round(self.current_weight_kg - weight_kg, 2)
        return self.current_weight_kg

    def get_occupancy_ratio(self) -> float:
        """Возвращает коэффициент заполненности ячейки (от 0.0 до 1.0)."""
        if self.max_weight_capacity_kg <= 0:
            return 1.0
        return round(self.current_weight_kg / self.max_weight_capacity_kg, 3)
