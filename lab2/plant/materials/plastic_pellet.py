"""Полимерные гранулы для литья под давлением (термопластавтоматы)."""

from __future__ import annotations
from plant.exceptions.material_defect_exception import MaterialDefectException

class PlasticPellet:
    """Описывает партию гранулированного пластика (PA66, POM, PP) для отливки бачков и коллекторов."""

    def __init__(
        self,
        pellet_id: str,
        polymer_type: str,
        melt_flow_index: float,
        moisture_pct: float
    ) -> None:
        # Номер партии гранулята
        self.pellet_id = pellet_id
        # Тип полимера (например, PA66-GF30 с стекловолокном)
        self.polymer_type = polymer_type
        # Показатель текучести расплава (ПТР, г/10 мин)
        self.melt_flow_index = melt_flow_index
        # Содержание остаточной влаги в процентах
        self.moisture_pct = moisture_pct

    def requires_drying(self, threshold_moisture: float = 0.15) -> bool:
        """Проверяет необходимость сушки гранулята в бункере-сушилке перед литьем."""
        return self.moisture_pct > threshold_moisture

    def perform_drying(self, hours: float) -> None:
        """Выполняет сушку полимера горячим воздухом, снижая влажность пропорционально времени."""
        reduction = hours * 0.08
        self.moisture_pct = max(0.01, round(self.moisture_pct - reduction, 3))

    def is_suitable_for_injection(self) -> bool:
        """Проверяет пригодность к литью; если влажность критическая (>0.5%), выбрасывает исключение."""
        if self.moisture_pct > 0.5:
            raise MaterialDefectException(
                f"Гранулы {self.polymer_type} ({self.pellet_id})",
                f"Критическая влажность {self.moisture_pct}%, приведет к гидролизу и порам"
            )
        return 2.0 <= self.melt_flow_index <= 35.0
