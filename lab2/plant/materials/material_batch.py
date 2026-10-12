"""Партия сырьевого материала на складе завода."""

from __future__ import annotations
from plant.materials.raw_material import RawMaterial
from plant.exceptions.raw_material_shortage_exception import RawMaterialShortageException

class MaterialBatch:
    """Учитывает поступление и расходование сырья в рамках одной поставки."""

    def __init__(
        self,
        batch_id: str,
        raw_material: RawMaterial,
        quantity_kg: float,
        received_date: str,
        is_inspected: bool = False
    ) -> None:
        # Номер партии в ERP-системе завода
        self.batch_id = batch_id
        # Ссылка на базовый материал (Ассоциация)
        self.raw_material = raw_material
        # Текущий остаток массы партии в кг
        self.quantity_kg = quantity_kg
        # Дата оприходования на склад
        self.received_date = received_date
        # Отметка о прохождении входного контроля лаборатории
        self.is_inspected = is_inspected

    def consume_material(self, amount_kg: float) -> float:
        """
        Списывает сырье на производство детали.
        Выбрасывает RawMaterialShortageException при нехватке.
        """
        if amount_kg <= 0:
            raise ValueError("Списываемое количество должно быть положительным")
        if amount_kg > self.quantity_kg:
            raise RawMaterialShortageException(self.raw_material.name, amount_kg, self.quantity_kg)
        self.quantity_kg = round(self.quantity_kg - amount_kg, 3)
        return self.quantity_kg

    def approve_inspection(self) -> None:
        """Подтверждает успешный входной контроль химического состава."""
        self.is_inspected = True

    def calculate_total_value(self) -> float:
        """Вычисляет балансовую стоимость оставшегося сырья партии."""
        return round(self.quantity_kg * self.raw_material.base_cost_per_kg, 2)
