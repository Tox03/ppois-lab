"""Фрезерный обрабатывающий центр с числовым программным управлением (ЧПУ)."""

from __future__ import annotations
from typing import Optional
from plant.equipment.machine import Machine
from plant.equipment.cutting_tool import CuttingTool
from plant.exceptions.machine_malfunction_exception import MachineMalfunctionException

class CncMillingMachine:
    """Осуществляет высокоточную фрезерную обработку корпусных автодеталей по G-коду."""

    def __init__(
        self,
        axis_count: int,
        spindle_rpm: int,
        machine: Machine,
        active_tool: Optional[CuttingTool] = None,
        coolant_pump_active: bool = False
    ) -> None:
        # Количество управляемых координат/осей (3-х, 4-х, 5-осевой)
        self.axis_count = axis_count
        # Текущая частота вращения шпинделя (об/мин)
        self.spindle_rpm = spindle_rpm
        # Базовый агрегат станка (Ассоциация)
        self.machine = machine
        # Закрепленная фреза в патроне (Ассоциация: CuttingTool)
        self.active_tool = active_tool
        # Состояние подачи СОЖ в зону резания
        self.coolant_pump_active = coolant_pump_active

    def mount_tool(self, tool: CuttingTool) -> None:
        """Устанавливает режущий инструмент в шпиндель из магазина инструмента."""
        if not tool.is_usable():
            raise MachineMalfunctionException(self.machine.machine_id, f"Инструмент {tool.tool_id} непригоден")
        self.active_tool = tool

    def mill_contour(self, feed_rate_mm_min: float, duration_min: float) -> bool:
        """Выполняет проход фрезерования по контуру заготовки."""
        if not self.machine.is_operational:
            raise MachineMalfunctionException(self.machine.machine_id, "Станок ЧПУ не готов к работе")
        if self.active_tool is None:
            raise MachineMalfunctionException(self.machine.machine_id, "Фреза не установлена в шпиндель")
        
        # Расход ресурса инструмента пропорционально подаче и времени
        wear_delta = (feed_rate_mm_min / 100000.0) * duration_min
        self.active_tool.apply_cut_wear(round(wear_delta, 4))
        self.machine.record_hours(duration_min / 60.0)
        self.machine.current_temperature += duration_min * 0.2
        self.machine.check_overheat()
        return True

    def set_spindle_speed(self, rpm: int) -> None:
        """Задает частоту вращения шпинделя в безопасном диапазоне."""
        if rpm < 100 or rpm > 24000:
            raise ValueError(f"Недопустимая скорость шпинделя {rpm} об/мин")
        self.spindle_rpm = rpm
