"""Камера электростатической порошковой покраски и полимеризации."""

from __future__ import annotations
from plant.equipment.machine import Machine
from plant.exceptions.machine_malfunction_exception import MachineMalfunctionException

class PaintingBooth:
    """Обеспечивает нанесение антикоррозийных и декоративных лакокрасочных покрытий."""

    def __init__(
        self,
        airflow_speed_mps: float,
        paint_type: str,
        chamber_humidity_pct: float,
        machine: Machine,
        electrostatic_charge_kv: float = 60.0
    ) -> None:
        # Скорость ламинарного потока воздуха вытяжки в м/с
        self.airflow_speed_mps = airflow_speed_mps
        # Марка порошковой краски (например, эпоксидно-полиэфирная RAL 9005)
        self.paint_type = paint_type
        # Влажность в окрасочной камере в процентах
        self.chamber_humidity_pct = chamber_humidity_pct
        # Базовый агрегат окрасочной камеры (Ассоциация)
        self.machine = machine
        # Высоковольтный электростатический заряд распылителя в кВ
        self.electrostatic_charge_kv = electrostatic_charge_kv

    def apply_powder_coat(self, thickness_microns: float) -> bool:
        """Наносит порошковый слой на металлическую деталь."""
        if not self.machine.is_operational:
            raise MachineMalfunctionException(self.machine.machine_id, "Окрасочный комплекс выключен")
        if self.chamber_humidity_pct > 65.0:
            raise MachineMalfunctionException(
                self.machine.machine_id,
                f"Влажность {self.chamber_humidity_pct}% превышает предел 65% для порошкового напыления"
            )
        return thickness_microns >= 50.0

    def bake_paint(self, temp_c: float, duration_min: float) -> bool:
        """Выполняет полимеризацию напыленного порошка в термопечи при 180-220°C."""
        if temp_c < 180.0 or temp_c > 240.0:
            raise ValueError(f"Температура запекания {temp_c}°C вне технологического регламента")
        self.machine.record_hours(duration_min / 60.0)
        return True

    def ventilate(self) -> None:
        """Включает форсированную рециркуляцию и фильтрацию взвеси в камере."""
        self.airflow_speed_mps = 0.5
        self.chamber_humidity_pct = max(30.0, self.chamber_humidity_pct - 5.0)
