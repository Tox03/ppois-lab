"""Исключение при критическом превышении рабочей температуры оборудования завода."""

from plant.exceptions.plant_base_exception import PlantBaseException

class EquipmentOverheatException(PlantBaseException):
    """Вызывается при превышении максимально допустимой рабочей температуры станка или печи."""

    def __init__(self, machine_id: str, current_temp: float, max_temp: float) -> None:
        super().__init__(
            f"Оборудование '{machine_id}' перегрето! Текущая температура: {current_temp}°C, максимум: {max_temp}°C",
            error_code="ERR_EQUIPMENT_OVERHEAT"
        )
        # Идентификатор перегретого оборудования
        self.machine_id = machine_id
        # Текущая зафиксированная температура
        self.current_temp = current_temp
        # Максимально допустимая температура
        self.max_temp = max_temp

    def get_excess_temp(self) -> float:
        """Возвращает величину превышения температуры выше критического порога."""
        return max(0.0, self.current_temp - self.max_temp)
