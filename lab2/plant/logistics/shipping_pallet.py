"""Транспортировочный поддон (европаллет) для готовых автодеталей."""

from __future__ import annotations
from typing import List
from plant.parts.auto_part import AutoPart
from plant.exceptions.storage_exhausted_exception import StorageExhaustedException

class ShippingPallet:
    """Обеспечивает формирование транспортного пакета деталей для автопогрузчика."""

    def __init__(
        self,
        pallet_id: str,
        max_capacity_parts: int,
        max_weight_kg: float = 1000.0,
        current_weight_kg: float = 0.0
    ) -> None:
        # Уникальный код паллета
        self.pallet_id = pallet_id
        # Максимальная вместимость деталей в штуках
        self.max_capacity_parts = max_capacity_parts
        # Уложенные на паллет готовые детали (Ассоциация: коллекция AutoPart)
        self.loaded_parts: List[AutoPart] = []
        # Предельная грузоподъемность поддона в кг
        self.max_weight_kg = max_weight_kg
        # Текущий суммарный вес поддона с грузом в кг
        self.current_weight_kg = current_weight_kg

    def load_part(self, part: AutoPart, part_weight_kg: float) -> bool:
        """
        Укладывает проверенную деталь на поддон.
        Выбрасывает StorageExhaustedException при перегрузе поддона.
        """
        if not part.is_defect_free:
            raise ValueError(f"Нельзя грузить бракованную деталь {part.part_number} на отгрузочный паллет")
        if len(self.loaded_parts) >= self.max_capacity_parts:
            raise StorageExhaustedException(self.pallet_id, self.max_capacity_parts, len(self.loaded_parts) + 1)
        if self.current_weight_kg + part_weight_kg > self.max_weight_kg:
            raise StorageExhaustedException(self.pallet_id, self.max_weight_kg, self.current_weight_kg + part_weight_kg)
        
        self.loaded_parts.append(part)
        self.current_weight_kg = round(self.current_weight_kg + part_weight_kg, 2)
        return True

    def unload_all(self) -> List[AutoPart]:
        """Снимает всю партию деталей с поддона на складе дилера."""
        parts = list(self.loaded_parts)
        self.loaded_parts.clear()
        self.current_weight_kg = 0.0
        return parts

    def is_full(self) -> bool:
        """Проверяет комплектность укладки паллета перед обмоткой стрейч-пленкой."""
        return len(self.loaded_parts) >= self.max_capacity_parts
