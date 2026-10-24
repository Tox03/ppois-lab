"""Контролер отдела технического контроля (ОТК)."""

from __future__ import annotations
from typing import List
from plant.personnel.employee import Employee

class QualityInspector:
    """Выполняет входной, операционный и выходной контроль качества продукции."""

    def __init__(
        self,
        employee: Employee,
        inspector_badge_id: str,
        inspections_count: int = 0,
        certified_standards: List[str] = None
    ) -> None:
        # Профиль сотрудника (Ассоциация)
        self.employee = employee
        # Номер личного клейма контролера ОТК
        self.inspector_badge_id = inspector_badge_id
        # Количество проведенных проверок деталей
        self.inspections_count = inspections_count
        # Перечень аттестованных стандартов (ISO 9001, IATF 16949 и др.)
        self.certified_standards = certified_standards if certified_standards is not None else []

    def inspect_part(self, is_ok: bool) -> str:
        """Регистрирует факт проверки автодетали и ставит клеймо при успехе."""
        self.inspections_count += 1
        if is_ok:
            return f"КЛЕЙМО_{self.inspector_badge_id}_ПРИНЯТО"
        return f"КЛЕЙМО_{self.inspector_badge_id}_БРАК"

    def add_certification(self, standard_code: str) -> None:
        """Добавляет новый сертификат в квалификационный лист инспектора."""
        if standard_code not in self.certified_standards:
            self.certified_standards.append(standard_code)

    def get_rejection_rate(self, rejected_count: int) -> float:
        """Вычисляет процент забракованных инспектором деталей."""
        if self.inspections_count == 0:
            return 0.0
        return round((rejected_count / self.inspections_count) * 100.0, 2)
