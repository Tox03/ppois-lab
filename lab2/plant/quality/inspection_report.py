"""Сводный акт приемочного контроля партии деталей."""

from __future__ import annotations
from plant.personnel.quality_inspector import QualityInspector

class InspectionReport:
    """Оформляет результаты сплошного или выборочного контроля партии автодеталей."""

    def __init__(
        self,
        report_id: str,
        batch_id: str,
        inspector: QualityInspector,
        passed_items: int,
        rejected_items: int
    ) -> None:
        # Номер акта приемо-сдаточных испытаний
        self.report_id = report_id
        # Номер проверенной партии продукции
        self.batch_id = batch_id
        # Ответственный контролер ОТК (Ассоциация: QualityInspector)
        self.inspector = inspector
        # Количество принятых годных деталей
        self.passed_items = passed_items
        # Количество забракованных деталей
        self.rejected_items = rejected_items

    def calculate_yield_rate(self) -> float:
        """Рассчитывает процент выхода годного (Yield Rate, %)."""
        total = self.passed_items + self.rejected_items
        if total == 0:
            return 0.0
        return round((self.passed_items / total) * 100.0, 2)

    def sign_report(self) -> str:
        """Формирует юридическую электронную подпись акта инспектором."""
        yield_pct = self.calculate_yield_rate()
        badge = self.inspector.inspector_badge_id
        return f"АКТ-{self.report_id} ПОДПИСАН [ОТК {badge}]. Выход годного: {yield_pct}%"

    def is_batch_acceptable(self, min_yield_rate: float = 95.0) -> bool:
        """Определяет допуск всей товарной партии к отгрузке клиенту."""
        return self.calculate_yield_rate() >= min_yield_rate
