"""Исключение при нехватке исходных сырьевых ресурсов для запуска технологической операции."""

from plant.exceptions.plant_base_exception import PlantBaseException

class RawMaterialShortageException(PlantBaseException):
    """Вызывается, если остаток сырья на складе меньше требуемого для партии."""

    def __init__(self, material_name: str, required_amount: float, available_amount: float) -> None:
        super().__init__(
            f"Недостаточно материала '{material_name}'. Требуется: {required_amount}, в наличии: {available_amount}",
            error_code="ERR_RAW_MATERIAL_SHORTAGE"
        )
        # Наименование недостающего сырья
        self.material_name = material_name
        # Требуемое количество
        self.required_amount = required_amount
        # Фактическое доступное количество
        self.available_amount = available_amount

    def calculate_deficit(self) -> float:
        """Вычисляет объем дефицита сырья."""
        return max(0.0, self.required_amount - self.available_amount)
