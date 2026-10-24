"""Промышленный робот дуговой/лазерной сварки кузовных узлов."""

from __future__ import annotations
from plant.equipment.machine import Machine
from plant.exceptions.machine_malfunction_exception import MachineMalfunctionException

class WeldingRobot:
    """Осуществляет автоматическую сварку рычагов подвески, рам и подрамников."""

    def __init__(
        self,
        current_amperage: float,
        gas_flow_rate_lpm: float,
        machine: Machine,
        welding_wire_type: str,
        arc_ignited: bool = False
    ) -> None:
        # Сила сварочного тока в амперах
        self.current_amperage = current_amperage
        # Расход защитного газа (аргон/CO2) в л/мин
        self.gas_flow_rate_lpm = gas_flow_rate_lpm
        # Базовый робот-манипулятор (Ассоциация)
        self.machine = machine
        # Марка сварочной проволоки (например, Св-08Г2С)
        self.welding_wire_type = welding_wire_type
        # Признак зажженной сварочной дуги
        self.arc_ignited = arc_ignited

    def ignite_arc(self) -> None:
        """Зажигает сварочную дугу при наличии достаточного потока защитного газа."""
        if not self.machine.is_operational:
            raise MachineMalfunctionException(self.machine.machine_id, "Робот обесточен")
        if self.gas_flow_rate_lpm < 10.0:
            raise MachineMalfunctionException(
                self.machine.machine_id,
                f"Недостаточный расход защитного газа {self.gas_flow_rate_lpm} л/мин (мин. 10 л/мин)"
            )
        self.arc_ignited = True

    def extinguish_arc(self) -> None:
        """Гасит дугу и проводит продувку шва защитным газом."""
        self.arc_ignited = False

    def perform_seam_weld(self, length_cm: float, speed_cm_per_s: float = 1.5) -> float:
        """Выполняет сварной шов заданной длины и возвращает время операции."""
        if not self.arc_ignited:
            self.ignite_arc()
        duration_sec = length_cm / max(0.1, speed_cm_per_s)
        self.machine.record_hours(duration_sec / 3600.0)
        self.machine.current_temperature += duration_sec * 0.05
        self.machine.check_overheat()
        self.extinguish_arc()
        return round(duration_sec, 2)
