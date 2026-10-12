"""Технологическая оснастка, штамп или пресс-форма."""

from __future__ import annotations
from plant.exceptions.tool_wear_exceeded_exception import ToolWearExceededException

class ToolingFixture:
    """Описывает формообразующую оснастку для штамповки и литья."""

    def __init__(
        self,
        fixture_id: str,
        fixture_type: str,
        cycles_used: int,
        max_cycles_lifetime: int,
        is_worn_out: bool = False
    ) -> None:
        # Инвентарный номер штампа / формы
        self.fixture_id = fixture_id
        # Тип оснастки (вырубной штамп, гибочный штамп, литьевая матрица)
        self.fixture_type = fixture_type
        # Количество выполненных рабочих циклов (ударов пресса)
        self.cycles_used = cycles_used
        # Предельный ресурс оснастки в циклах до капремонта
        self.max_cycles_lifetime = max_cycles_lifetime
        # Статус предельного износа
        self.is_worn_out = is_worn_out

    def increment_cycles(self, count: int = 1) -> None:
        """
        Регистрирует выполнение рабочих ходов пресса.
        Выбрасывает ToolWearExceededException при превышении лимита.
        """
        if count <= 0:
            raise ValueError("Число циклов должно быть положительным")
        self.cycles_used += count
        if self.cycles_used >= self.max_cycles_lifetime:
            self.is_worn_out = True
            raise ToolWearExceededException(self.fixture_id, self.cycles_used, self.max_cycles_lifetime)

    def refurbish(self) -> None:
        """Восстанавливает геометрию штампа шлифовкой и наплавкой кромок."""
        self.cycles_used = 0
        self.is_worn_out = False

    def get_wear_ratio(self) -> float:
        """Возвращает степень выработки ресурса штампа (от 0.0 до 1.0)."""
        if self.max_cycles_lifetime <= 0:
            return 1.0
        return round(min(1.0, self.cycles_used / self.max_cycles_lifetime), 3)
