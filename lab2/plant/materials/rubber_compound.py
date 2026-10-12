"""Резиновая сырая смесь для виброизоляторов и сальников."""

from __future__ import annotations

class RubberCompound:
    """Описывает эластомерную смесь для производства сайлентблоков, уплотнений и пыльников."""

    def __init__(
        self,
        compound_id: str,
        shore_hardness: int,
        cure_time_minutes: float,
        is_vulcanized: bool = False
    ) -> None:
        # Шифр рецептуры резиновой смеси
        self.compound_id = compound_id
        # Твердость по шкале Шора А (единиц)
        self.shore_hardness = shore_hardness
        # Время цикла вулканизации в минутах
        self.cure_time_minutes = cure_time_minutes
        # Статус завершения процесса вулканизации
        self.is_vulcanized = is_vulcanized

    def validate_hardness(self, target_hardness: int, tolerance: int = 5) -> bool:
        """Проверяет соответствие твердости по Шору заданному диапазону конструкторского чертежа."""
        return abs(self.shore_hardness - target_hardness) <= tolerance

    def simulate_vulcanization(self, temperature_c: float) -> bool:
        """Симулирует автоклавную вулканизацию под температурой (требуется от 140°C до 200°C)."""
        if 140.0 <= temperature_c <= 200.0:
            self.is_vulcanized = True
            return True
        return False

    def is_ready_for_assembly(self) -> bool:
        """Определяет готовность резинового элемента к запрессовке в металлический узел."""
        return self.is_vulcanized and self.shore_hardness >= 40
