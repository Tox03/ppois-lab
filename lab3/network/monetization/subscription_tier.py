# -*- coding: utf-8 -*-
"""Модуль уровня платной подписки."""


class SubscriptionTier:
    """Описывает тарифный план авторской или платформенной подписки."""

    def __init__(
        self,
        tier_id: str,
        name: str,
        monthly_price: float,
        benefits_count: int = 1,
        badge_icon: str = "⭐",
    ) -> None:
        """Инициализация тарифного плана."""
        self.tier_id = tier_id
        self.name = name
        self.monthly_price = monthly_price
        self.benefits_count = benefits_count
        self.badge_icon = badge_icon

    def is_affordable(self, budget: float) -> bool:
        """Проверяет, достаточно ли средств пользователя для оплаты месяца."""
        return budget >= self.monthly_price

    def add_benefit(self) -> int:
        """Увеличивает число включенных преимуществ тарифа."""
        self.benefits_count += 1
        return self.benefits_count

    def format_price_tag(self) -> str:
        """Формирует ценник подписки."""
        return f"{self.name}: {self.monthly_price} руб./мес. {self.badge_icon}"
