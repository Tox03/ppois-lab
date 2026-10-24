"""Первичный/вторичный вал коробки перемены передач (МКПП/АКПП)."""

from __future__ import annotations
from plant.parts.auto_part import AutoPart

class GearboxShaft:
    """Описывает зубчатый шлицевой вал трансмиссии высокой твердости."""

    def __init__(
        self,
        auto_part: AutoPart,
        gear_teeth_count: int,
        surface_hardness_hrc: float,
        spline_count: int,
        is_hardened: bool = True
    ) -> None:
        # Базовый паспорт автодетали (Ассоциация: AutoPart)
        self.auto_part = auto_part
        # Количество зубьев ведущего венца
        self.gear_teeth_count = gear_teeth_count
        # Твердость цементированного слоя по Роквеллу (HRC)
        self.surface_hardness_hrc = surface_hardness_hrc
        # Число шлицев под муфту синхронизатора
        self.spline_count = spline_count
        # Признак завершения химико-термической обработки
        self.is_hardened = is_hardened

    def validate_hardness(self, min_hrc: float = 58.0) -> bool:
        """Проверяет твердость зубьев шестерни на соответствие техническим условиям."""
        is_valid = self.surface_hardness_hrc >= min_hrc
        if not is_valid:
            self.auto_part.is_defect_free = False
        return is_valid

    def calculate_gear_ratio(self, matching_gear_teeth: int) -> float:
        """Рассчитывает передаточное отношение зацепления с парной шестерней."""
        if self.gear_teeth_count <= 0:
            raise ValueError("Число зубьев должно быть больше 0")
        return round(matching_gear_teeth / self.gear_teeth_count, 3)

    def verify_spline_mesh(self, matching_splines: int) -> bool:
        """Проверяет возможность сборки шлицевого соединения со скользящей муфтой."""
        return self.spline_count == matching_splines
