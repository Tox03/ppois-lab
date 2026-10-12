"""Автоматизированная производственная линия сборки/мехобработки."""

from __future__ import annotations
from typing import List
from plant.production.work_station import WorkStation
from plant.exceptions.production_line_halt_exception import ProductionLineHaltException
from plant.exceptions.defect_threshold_exceeded_exception import DefectThresholdExceededException

class ProductionLine:
    """Управляет последовательностью рабочих постов цеха и мониторит качество."""

    def __init__(
        self,
        line_id: str,
        line_name: str,
        max_allowed_scrap_pct: float = 3.0
    ) -> None:
        # Уникальный код производственной линии (например, ЛИНИЯ-ВАЛОВ-01)
        self.line_id = line_id
        # Название линии
        self.line_name = line_name
        # Список технологических постов (Ассоциация: коллекция WorkStation)
        self.stations: List[WorkStation] = []
        # Состояние конвейера (запущен / остановлен)
        self.is_running: bool = False
        # Текущий процент брака на линии (%)
        self.scrap_rate: float = 0.0
        # Предельно допустимый процент брака по контракту
        self.max_allowed_scrap_pct = max_allowed_scrap_pct

    def add_station(self, station: WorkStation) -> None:
        """Добавляет рабочий пост в цепочку конвейера."""
        self.stations.append(station)

    def start_line(self) -> bool:
        """Запускает линию, если все добавленные посты укомплектованы и активны."""
        if not self.stations:
            return False
        for s in self.stations:
            if not s.is_active:
                return False
        self.is_running = True
        return True

    def emergency_halt(self, reason: str, requires_evacuation: bool = False) -> None:
        """
        Производит аварийный останов всех станков линии.
        Выбрасывает ProductionLineHaltException.
        """
        self.is_running = False
        for s in self.stations:
            s.machine.stop()
        raise ProductionLineHaltException(self.line_id, reason, requires_evacuation)

    def record_scrap(self, total_produced: int, total_defective: int) -> float:
        """
        Фиксирует количество деталей и рассчитывает процент брака.
        Выбрасывает DefectThresholdExceededException при выходе за норматив.
        """
        if total_produced <= 0:
            return 0.0
        self.scrap_rate = round((total_defective / total_produced) * 100.0, 2)
        if self.scrap_rate > self.max_allowed_scrap_pct:
            raise DefectThresholdExceededException(self.line_id, self.scrap_rate, self.max_allowed_scrap_pct)
        return self.scrap_rate
