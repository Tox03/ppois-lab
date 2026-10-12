"""Печь термической обработки деталей (закалка, отпуск, цементация)."""

from __future__ import annotations
from plant.equipment.machine import Machine
from plant.exceptions.equipment_overheat_exception import EquipmentOverheatException

class HeatTreatmentFurnace:
    """Управляет термообработкой валов, шестерен и тормозных дисков."""

    def __init__(
        self,
        target_temp_celsius: float,
        quench_medium: str,
        holding_time_minutes: float,
        machine: Machine,
        is_heating: bool = False
    ) -> None:
        # Заданная температура термообработки в камере
        self.target_temp_celsius = target_temp_celsius
        # Охлаждающая закалочная среда (масло, вода, полимерный раствор)
        self.quench_medium = quench_medium
        # Время изотермической выдержки деталей в минутах
        self.holding_time_minutes = holding_time_minutes
        # Базовый термоагрегат (Ассоциация)
        self.machine = machine
        # Статус работы нагревательных ТЭНов
        self.is_heating = is_heating

    def heat_to_target(self, temp_c: float) -> None:
        """Разогревает камеру до заданной температуры технологической карты."""
        if temp_c > 1200.0:
            raise EquipmentOverheatException(self.machine.machine_id, temp_c, 1200.0)
        self.target_temp_celsius = temp_c
        self.machine.current_temperature = temp_c
        self.is_heating = True

    def quench(self) -> str:
        """Производит погружение раскаленных деталей в закалочную ванну."""
        if not self.is_heating:
            return "Печь холодная, закалка не требуется"
        self.is_heating = False
        return f"Закалка выполнена в среде '{self.quench_medium}', сняты внутренние напряжения"

    def perform_hardening_cycle(self, duration_min: float) -> bool:
        """Проводит полный автоматический цикл термической закалки."""
        self.holding_time_minutes = duration_min
        self.machine.record_hours(duration_min / 60.0)
        return True
