"""Телеметрический промышленный датчик мониторинга состояния оборудования."""

from __future__ import annotations
from plant.equipment.machine import Machine

class EquipmentSensor:
    """Измеряет вибрацию, температуру, давление масла или ток шпинделя станка."""

    def __init__(
        self,
        sensor_id: str,
        metric_name: str,
        last_reading: float,
        alert_threshold: float,
        machine: Machine
    ) -> None:
        # Уникальный серийный номер сенсора
        self.sensor_id = sensor_id
        # Наименование физической величины (например, Вибрация_RMS, Давление_масла)
        self.metric_name = metric_name
        # Последнее зафиксированное показание
        self.last_reading = last_reading
        # Аварийный порог срабатывания сигнализации
        self.alert_threshold = alert_threshold
        # Ссылка на контролируемый станок (Ассоциация)
        self.machine = machine

    def read_value(self, current_value: float) -> float:
        """Считывает новое мгновенное значение с аналогового входа датчика."""
        self.last_reading = current_value
        return self.last_reading

    def is_threshold_exceeded(self) -> bool:
        """Проверяет превышение допустимой аварийной уставки телеметрии."""
        return self.last_reading >= self.alert_threshold

    def calibrate_offset(self, offset: float) -> None:
        """Корректирует нулевой дрейф сенсора на величину смещения."""
        self.last_reading = max(0.0, self.last_reading - offset)
