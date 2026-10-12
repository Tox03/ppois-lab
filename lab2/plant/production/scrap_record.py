"""Акт о браке производственной партии деталей."""

from __future__ import annotations

class ScrapRecord:
    """Учитывает факты технологического и неисправимого брака в цехах завода."""

    def __init__(
        self,
        record_id: str,
        defect_reason: str,
        scrapped_quantity: int,
        registered_date: str
    ) -> None:
        # Номер акта списания в брак
        self.record_id = record_id
        # Причина отбраковки (трещина, задир, несоответствие размеров, раковина)
        self.defect_reason = defect_reason
        # Количество забракованных деталей
        self.scrapped_quantity = scrapped_quantity
        # Дата оформления акта
        self.registered_date = registered_date

    def calculate_financial_loss(self, unit_cost: float) -> float:
        """Рассчитывает сумму прямого материального ущерба от брака."""
        if unit_cost < 0:
            raise ValueError("Себестоимость не может быть отрицательной")
        return round(self.scrapped_quantity * unit_cost, 2)

    def is_critical_scrap(self, threshold: int = 50) -> bool:
        """Определяет, требует ли данный случай созыва чрезвычайной комиссии по качеству."""
        return self.scrapped_quantity >= threshold

    def format_summary(self) -> str:
        """Формирует строку записи для сводной ведомости цехового брака."""
        return f"[{self.registered_date}] Акт {self.record_id}: {self.scrapped_quantity} шт. Причина: {self.defect_reason}"
