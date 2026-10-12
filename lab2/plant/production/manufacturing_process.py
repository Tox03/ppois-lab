"""Технологический процесс изготовления детали (операционная карта)."""

from __future__ import annotations

class ManufacturingProcess:
    """Определяет параметры техпроцесса: время штучной обработки, энергопотребление и режим."""

    def __init__(
        self,
        process_name: str,
        duration_minutes: float,
        energy_consumption_kwh: float,
        required_temperature: float = 20.0
    ) -> None:
        # Наименование операции (штамповка, закалка, шлифовка, покраска)
        self.process_name = process_name
        # Норма времени на 1 деталь в минутах
        self.duration_minutes = duration_minutes
        # Потребляемая электроэнергия на цикл в кВт*ч
        self.energy_consumption_kwh = energy_consumption_kwh
        # Требуемая температура рабочего пространства в °C
        self.required_temperature = required_temperature

    def calculate_power_cost(self, tariff_per_kwh: float) -> float:
        """Рассчитывает затраты на электроэнергию на единицу продукции."""
        if tariff_per_kwh < 0:
            raise ValueError("Тариф не может быть отрицательным")
        return round(self.energy_consumption_kwh * tariff_per_kwh, 3)

    def optimize_duration(self, speedup_ratio: float) -> float:
        """Сокращает время цикла в результате бережливого производства (Kaizen)."""
        if speedup_ratio <= 0 or speedup_ratio >= 1.0:
            raise ValueError("Коэффициент ускорения должен быть в интервале (0, 1)")
        self.duration_minutes = round(self.duration_minutes * (1.0 - speedup_ratio), 2)
        return self.duration_minutes

    def is_thermal_process(self) -> bool:
        """Определяет, сопровождается ли процесс высокотемпературным нагревом (>100°C)."""
        return self.required_temperature > 100.0
