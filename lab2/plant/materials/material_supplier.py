"""Поставщик сырья и металлопроката."""

from __future__ import annotations
from plant.core.contact_info import ContactInfo

class MaterialSupplier:
    """Описывает внешнего поставщика металлов, химикатов и полимеров."""

    def __init__(
        self,
        supplier_id: str,
        company_name: str,
        rating: float,
        contact_info: ContactInfo
    ) -> None:
        # Уникальный код поставщика в реестре закупок
        self.supplier_id = supplier_id
        # Юридическое наименование компании-поставщика
        self.company_name = company_name
        # Рейтинг надежности по шкале от 0.0 до 5.0
        self.rating = rating
        # Контактные данные коммерческого отдела (Ассоциация)
        self.contact_info = contact_info

    def update_rating(self, score: float) -> float:
        """Пересчитывает рейтинг поставщика по результатам последней поставки."""
        self.rating = round(max(0.0, min(5.0, (self.rating * 0.7) + (score * 0.3))), 2)
        return self.rating

    def is_certified_vendor(self) -> bool:
        """Проверяет аккредитацию поставщика для ответственных автокомпонентов (рейтинг >= 4.0)."""
        return self.rating >= 4.0 and self.contact_info.validate_contact()

    def send_quality_claim(self, claim_reason: str) -> str:
        """Формирует юридическую рекламацию поставщику при поставке бракованного сырья."""
        return f"ПРЕТЕНЗИЯ поставщику {self.company_name} ({self.contact_info.email}): {claim_reason}"
