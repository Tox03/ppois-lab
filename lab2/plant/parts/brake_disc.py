"""Вентилируемый/цельный тормозной диск дискового тормоза."""

from __future__ import annotations
from plant.parts.auto_part import AutoPart

class BrakeDisc:
    """Описывает тормозной диск с контролем толщины полотна и торцевого биения."""

    def __init__(
        self,
        auto_part: AutoPart,
        disc_thickness_mm: float,
        min_thickness_limit_mm: float,
        is_ventilated: bool = True,
        runout_microns: float = 15.0
    ) -> None:
        # Базовый паспорт автодетали (Ассоциация: AutoPart)
        self.auto_part = auto_part
        # Номинальная толщина тормозного полотна в мм
        self.disc_thickness_mm = disc_thickness_mm
        # Минимально допустимая толщина до выбраковки
        self.min_thickness_limit_mm = min_thickness_limit_mm
        # Конструктивное наличие вентиляционных каналов
        self.is_ventilated = is_ventilated
        # Измеренное торцевое биение диска в микрометрах (мкм)
        self.runout_microns = runout_microns

    def check_wear_limit(self) -> bool:
        """Проверяет пригодность диска по остаточной толщине."""
        return self.disc_thickness_mm >= self.min_thickness_limit_mm

    def verify_axial_runout(self, max_allowed_microns: float = 30.0) -> bool:
        """Проверяет соответствие биения нормам безопасности для исключения биения педали."""
        is_ok = self.runout_microns <= max_allowed_microns
        if not is_ok:
            self.auto_part.is_defect_free = False
        return is_ok

    def simulate_braking_cycle(self, friction_wear_mm: float) -> float:
        """Имитирует истирание полотна диска колодками за цикл испытаний на тормозном стенде."""
        self.disc_thickness_mm = round(max(0.0, self.disc_thickness_mm - friction_wear_mm), 3)
        return self.disc_thickness_mm
