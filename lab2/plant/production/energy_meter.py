"""Цеховой счетчик потребления электрической энергии."""

from __future__ import annotations

class EnergyMeter:
    """Осуществляет коммерческий и технический учет расхода электроэнергии цехом."""

    def __init__(
        self,
        meter_id: str,
        total_kwh: float = 0.0,
        tariff_per_kwh: float = 0.12
    ) -> None:
        # Серийный номер прибора учета
        self.meter_id = meter_id
        # Накопленный расход энергии в кВт*ч
        self.total_kwh = total_kwh
        # Действующий промышленный тариф (руб/кВт*ч или $/кВт*ч)
        self.tariff_per_kwh = tariff_per_kwh

    def record_consumption(self, kwh: float) -> float:
        """Добавляет зарегистрированное потребление станка или линии к суммарному расходу."""
        if kwh < 0:
            raise ValueError("Расход энергии не может быть отрицательным")
        self.total_kwh = round(self.total_kwh + kwh, 2)
        return self.total_kwh

    def calculate_energy_bill(self) -> float:
        """Вычисляет общую стоимость потребленной электроэнергии за расчетный период."""
        return round(self.total_kwh * self.tariff_per_kwh, 2)

    def reset_monthly_counter(self) -> None:
        """Сбрасывает накопленный месячный счетчик при закрытии финансового периода."""
        self.total_kwh = 0.0
