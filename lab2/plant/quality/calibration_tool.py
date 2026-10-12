"""Калибровочный эталон и регламент поверки измерительного инструмента."""

from __future__ import annotations
from plant.exceptions.calibration_expired_exception import CalibrationExpiredException

class CalibrationTool:
    """Управляет интервалами поверки метрологического оборудования лаборатории ОТК."""

    def __init__(
        self,
        tool_id: str,
        tool_name: str,
        last_calibration_date: str,
        calibration_interval_days: int = 180,
        is_calibrated: bool = True
    ) -> None:
        # Инвентарный номер средства измерений
        self.tool_id = tool_id
        # Наименование прибора (эталонные концевые меры, нутромер, динамометр)
        self.tool_name = tool_name
        # Дата последней метрологической поверки (ГГГГ-ММ-ДД)
        self.last_calibration_date = last_calibration_date
        # Межповерочный интервал в сутках
        self.calibration_interval_days = calibration_interval_days
        # Статус годности поверки
        self.is_calibrated = is_calibrated

    def check_calibration_validity(self, days_since_last_calib: int) -> bool:
        """
        Проверяет срок действия поверки.
        Выбрасывает CalibrationExpiredException при просрочке.
        """
        if days_since_last_calib > self.calibration_interval_days:
            self.is_calibrated = False
            overdue = days_since_last_calib - self.calibration_interval_days
            raise CalibrationExpiredException(self.tool_id, overdue)
        self.is_calibrated = True
        return True

    def recalibrate(self, new_date: str) -> None:
        """Регистрирует успешное прохождение очередной госповерки прибора."""
        self.last_calibration_date = new_date
        self.is_calibrated = True

    def format_calibration_tag(self) -> str:
        """Формирует текст метрологической бирки для наклейки на корпус прибора."""
        status_str = "ГОДЕН" if self.is_calibrated else "ПРОСРОЧЕН"
        return f"ПРИБОР {self.tool_id} [{self.tool_name}]: Поверен {self.last_calibration_date} ({status_str})"
