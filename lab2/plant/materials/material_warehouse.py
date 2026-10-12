"""Склад исходного сырья и комплектующих автомобильного завода."""

from __future__ import annotations
from typing import List, Optional
from plant.core.address import Address
from plant.materials.storage_bin import StorageBin

class MaterialWarehouse:
    """Управляет складскими ячейками, емкостями и запасами сырья."""

    def __init__(
        self,
        warehouse_id: str,
        address: Address,
        total_capacity_tons: float
    ) -> None:
        # Инвентарный номер склада
        self.warehouse_id = warehouse_id
        # Физический адрес складского комплекса (Ассоциация)
        self.address = address
        # Список ячеек хранения (Ассоциация: коллекция StorageBin)
        self.storage_bins: List[StorageBin] = []
        # Суммарная паспортная вместимость склада в тоннах
        self.total_capacity_tons = total_capacity_tons

    def add_bin(self, storage_bin: StorageBin) -> None:
        """Регистрирует новую ячейку или бункер в складской системе."""
        self.storage_bins.append(storage_bin)

    def find_available_bin(self, weight_kg: float) -> Optional[StorageBin]:
        """Ищет незаблокированную ячейку с достаточным запасом грузоподъемности."""
        for b in self.storage_bins:
            if not b.is_locked and (b.max_weight_capacity_kg - b.current_weight_kg) >= weight_kg:
                return b
        return None

    def calculate_total_stored_weight(self) -> float:
        """Рассчитывает общий фактический вес хранящегося сырья в тоннах."""
        total_kg = sum(b.current_weight_kg for b in self.storage_bins)
        return round(total_kg / 1000.0, 2)
