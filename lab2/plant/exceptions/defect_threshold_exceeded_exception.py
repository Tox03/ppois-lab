"""Исключение при превышении критического процента брака на производственной линии."""

from plant.exceptions.plant_base_exception import PlantBaseException

class DefectThresholdExceededException(PlantBaseException):
    """Вызывается, если процент дефектных деталей на линии превысил допустимый порог стандарта IATF."""

    def __init__(self, line_id: str, current_scrap_rate: float, max_allowed_rate: float) -> None:
        super().__init__(
            f"Превышен допустимый уровень брака на линии '{line_id}': текущий {current_scrap_rate:.2f}%, максимум {max_allowed_rate:.2f}%",
            error_code="ERR_DEFECT_THRESHOLD_EXCEEDED"
        )
        # Идентификатор производственной линии
        self.line_id = line_id
        # Текущий процент брака
        self.current_scrap_rate = current_scrap_rate
        # Максимально допустимый процент брака
        self.max_allowed_rate = max_allowed_rate

    def get_scrap_excess(self) -> float:
        """Возвращает разницу между фактическим браком и предельным допуском."""
        return max(0.0, self.current_scrap_rate - self.max_allowed_rate)
