"""Кривошипный/гидравлический штамповочный пресс цеха холодной штамповки."""

from __future__ import annotations
from typing import Optional
from plant.equipment.machine import Machine
from plant.equipment.tooling_fixture import ToolingFixture
from plant.exceptions.machine_malfunction_exception import MachineMalfunctionException

class StampingPress:
    """Управляет прессовым оборудованием и штамповой оснасткой для формовки деталей."""

    def __init__(
        self,
        press_tonnage: float,
        stroke_length_mm: float,
        machine: Machine,
        tooling_fixture: Optional[ToolingFixture] = None,
        parts_stamped: int = 0
    ) -> None:
        # Номинальное усилие пресса в тоннах (например, 250 т, 500 т)
        self.press_tonnage = press_tonnage
        # Длина хода ползуна в миллиметрах
        self.stroke_length_mm = stroke_length_mm
        # Базовый агрегат станка (Ассоциация)
        self.machine = machine
        # Установленный штамп (Ассоциация: ToolingFixture)
        self.tooling_fixture = tooling_fixture
        # Счетчик отштампованных заготовок
        self.parts_stamped = parts_stamped

    def install_die(self, die: ToolingFixture) -> None:
        """Монтирует штамп на плиту пресса."""
        if die.is_worn_out:
            raise MachineMalfunctionException(self.machine.machine_id, f"Штамп {die.fixture_id} изношен")
        self.tooling_fixture = die

    def execute_stroke(self) -> bool:
        """Выполняет рабочий ход пресса (штамповку заготовки)."""
        if not self.machine.is_operational:
            raise MachineMalfunctionException(self.machine.machine_id, "Пресс отключен или неисправен")
        if self.tooling_fixture is None:
            raise MachineMalfunctionException(self.machine.machine_id, "Штамповая оснастка не установлена")
        
        self.tooling_fixture.increment_cycles(1)
        self.parts_stamped += 1
        # Повышаем температуру узлов трения пресса
        self.machine.current_temperature += 0.05
        self.machine.check_overheat()
        return True

    def calibrate_pressure(self, required_tonnage: float) -> bool:
        """Калибрует гидравлическое давление под требуемое усилие вытяжки."""
        if required_tonnage > self.press_tonnage:
            raise ValueError(f"Требуемое усилие {required_tonnage} т превышает мощность пресса {self.press_tonnage} т")
        return True
