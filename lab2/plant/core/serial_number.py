"""Серийный номер и лазерная маркировка деталей."""

from __future__ import annotations

class SerialNumber:
    """Генератор и валидатор заводской сквозной маркировки автокомпонентов."""

    def __init__(self, prefix: str, year: int, sequence_id: int, is_active: bool = True) -> None:
        # Трехбуквенный префикс типа детали (например, PST для поршней)
        self.prefix = prefix.upper()
        # Год выпуска партии
        self.year = year
        # Порядковый номер изделия в производственной серии
        self.sequence_id = sequence_id
        # Статус валидности маркировки в единой базе завода
        self.is_active = is_active

    def generate_code(self) -> str:
        """Генерирует форматированный код детали для лазерной гравировки (например, PST-2026-000452)."""
        return f"{self.prefix}-{self.year}-{self.sequence_id:06d}"

    def validate_format(self, code_str: str) -> bool:
        """Проверяет соответствие переданной строки формату заводского номера."""
        parts = code_str.split("-")
        if len(parts) != 3:
            return False
        return parts[0] == self.prefix and parts[1] == str(self.year) and parts[2].isdigit()

    def deactivate(self) -> None:
        """Аннулирует серийный номер в случае списания или утилизации детали."""
        self.is_active = False
