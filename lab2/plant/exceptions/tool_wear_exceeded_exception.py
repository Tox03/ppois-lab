"""Исключение при критическом износе оснастки, штампа или режущего инструмента."""

from plant.exceptions.plant_base_exception import PlantBaseException

class ToolWearExceededException(PlantBaseException):
    """Вызывается при превышении предельно допустимого ресурса работы инструмента."""

    def __init__(self, tool_id: str, current_wear: float, max_wear: float) -> None:
        super().__init__(
            f"Инструмент/оснастка '{tool_id}' изношен! Текущий износ: {current_wear}, предел: {max_wear}",
            error_code="ERR_TOOL_WEAR_EXCEEDED"
        )
        # Идентификатор инструмента или штампа
        self.tool_id = tool_id
        # Текущий износ (в циклах или миллиметрах износа кромки)
        self.current_wear = current_wear
        # Максимально допустимый износ
        self.max_wear = max_wear

    def get_wear_percentage(self) -> float:
        """Возвращает процент выработки ресурса инструмента."""
        if self.max_wear <= 0:
            return 100.0
        return (self.current_wear / self.max_wear) * 100.0
