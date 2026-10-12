"""Слесарь-инструментальщик инструментального цеха."""

from __future__ import annotations
from plant.personnel.employee import Employee
from plant.equipment.cutting_tool import CuttingTool
from plant.equipment.tooling_fixture import ToolingFixture

class Toolmaker:
    """Изготавливает и доводит высокоточную оснастку, штампы и режущий инструмент."""

    def __init__(
        self,
        employee: Employee,
        specialty: str,
        refurbished_tools_count: int = 0,
        precision_tolerance_mm: float = 0.005
    ) -> None:
        # Профиль сотрудника (Ассоциация)
        self.employee = employee
        # Специализация (штампы, пресс-формы, твердосплавный инструмент)
        self.specialty = specialty
        # Число восстановленных единиц инструмента
        self.refurbished_tools_count = refurbished_tools_count
        # Достижимая точность доводки поверхностей в миллиметрах
        self.precision_tolerance_mm = precision_tolerance_mm

    def regrind_cutting_tool(self, tool: CuttingTool) -> None:
        """Перетачивает изношенный режущий инструмент на заточном станке."""
        tool.regrind()
        self.refurbished_tools_count += 1

    def refurbish_die(self, fixture: ToolingFixture) -> None:
        """Реставрирует рабочие кромки штампа или литьевой матрицы."""
        fixture.refurbish()
        self.refurbished_tools_count += 1

    def verify_die_precision(self, fixture: ToolingFixture) -> bool:
        """Выполняет микрометрический контроль геометрии посадочных мест оснастки."""
        return not fixture.is_worn_out and self.precision_tolerance_mm <= 0.01
