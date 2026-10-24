"""Металлорежущий инструмент (фрезы, сверла, пластины)."""

from __future__ import annotations
from plant.exceptions.tool_wear_exceeded_exception import ToolWearExceededException

class CuttingTool:
    """Описывает инструмент для механической обработки деталей на станках ЧПУ."""

    def __init__(
        self,
        tool_id: str,
        tool_material: str,
        flank_wear_mm: float,
        max_wear_limit_mm: float = 0.3,
        is_sharp: bool = True
    ) -> None:
        # Маркировка инструмента
        self.tool_id = tool_id
        # Материал режущей части (твердый сплав ВК8, быстрорез Р6М5, керамика)
        self.tool_material = tool_material
        # Текущий износ по задней поверхности в миллиметрах
        self.flank_wear_mm = flank_wear_mm
        # Предельно допустимая фаска износа по технологической карте
        self.max_wear_limit_mm = max_wear_limit_mm
        # Флаг остроты инструмента
        self.is_sharp = is_sharp

    def apply_cut_wear(self, wear_amount: float) -> None:
        """
        Увеличивает износ кромки после прохода.
        Выбрасывает ToolWearExceededException при превышении предела.
        """
        if wear_amount <= 0:
            raise ValueError("Величина износа должна быть положительной")
        self.flank_wear_mm = round(self.flank_wear_mm + wear_amount, 3)
        if self.flank_wear_mm >= self.max_wear_limit_mm:
            self.is_sharp = False
            raise ToolWearExceededException(self.tool_id, self.flank_wear_mm, self.max_wear_limit_mm)

    def regrind(self) -> None:
        """Выполняет переточку инструмента на заточном станке."""
        self.flank_wear_mm = 0.0
        self.is_sharp = True

    def is_usable(self) -> bool:
        """Проверяет возможность безопасного использования инструмента."""
        return self.is_sharp and self.flank_wear_mm < self.max_wear_limit_mm
