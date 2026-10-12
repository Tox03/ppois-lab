"""Смазочно-охлаждающая технологическая жидкость (СОЖ)."""

from __future__ import annotations

class ChemicalCoolant:
    """Описывает эмульсию СОЖ для фрезерных и токарных центров ЧПУ."""

    def __init__(
        self,
        coolant_id: str,
        concentration_pct: float,
        ph_level: float,
        is_contaminated: bool = False
    ) -> None:
        # Идентификатор резервуара СОЖ
        self.coolant_id = coolant_id
        # Концентрация масляного концентрата в воде (%)
        self.concentration_pct = concentration_pct
        # Кислотно-щелочной баланс (pH)
        self.ph_level = ph_level
        # Наличие механического или бактериального загрязнения
        self.is_contaminated = is_contaminated

    def is_within_ph_limits(self, min_ph: float = 8.5, max_ph: float = 9.5) -> bool:
        """Проверяет антикоррозионные свойства СОЖ по уровню pH."""
        return min_ph <= self.ph_level <= max_ph and not self.is_contaminated

    def dilute_with_water(self, water_liters: float, total_liters: float) -> None:
        """Пересчитывает концентрацию раствора при доливе очищенной воды."""
        if total_liters <= 0 or water_liters < 0:
            raise ValueError("Некорректный объем жидкости")
        dilution_factor = total_liters / (total_liters + water_liters)
        self.concentration_pct = round(self.concentration_pct * dilution_factor, 2)

    def replace_fluid(self) -> None:
        """Сбрасывает загрязнение и обновляет раствор до нормативных заводских 7.0% концентрации."""
        self.is_contaminated = False
        self.concentration_pct = 7.0
        self.ph_level = 9.0
