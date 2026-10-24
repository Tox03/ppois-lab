"""Исключение при попытке использования измерительного прибора с истекшим сроком поверки."""

from plant.exceptions.plant_base_exception import PlantBaseException

class CalibrationExpiredException(PlantBaseException):
    """Вызывается, если метрологический прибор или датчик не прошел периодическую поверку."""

    def __init__(self, tool_id: str, days_overdue: int) -> None:
        super().__init__(
            f"Калибровка прибора '{tool_id}' просрочена на {days_overdue} дней! Использование запрещено.",
            error_code="ERR_CALIBRATION_EXPIRED"
        )
        # Идентификатор средства измерений
        self.tool_id = tool_id
        # Количество дней просрочки
        self.days_overdue = days_overdue

    def is_grace_period_exceeded(self) -> bool:
        """Проверяет, превышен ли льготный период допустимой эксплуатации (3 дня)."""
        return self.days_overdue > 3
