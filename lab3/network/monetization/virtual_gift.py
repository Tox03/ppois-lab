# -*- coding: utf-8 -*-
"""Модуль виртуального подарка."""

from lab3.network.core.user_account import UserAccount
from lab3.network.monetization.wallet import Wallet


class VirtualGift:
    """Представляет подарочный стикер/сувенир, отправляемый в профиль."""

    def __init__(
        self,
        gift_id: str,
        gift_name: str,
        price_coins: int = 10,
        icon_code: str = "🎁",
        is_limited_edition: bool = False,
    ) -> None:
        """Инициализация виртуального подарка."""
        self.gift_id = gift_id
        self.gift_name = gift_name
        self.price_coins = price_coins
        self.icon_code = icon_code
        self.is_limited_edition = is_limited_edition

    def send_gift(self, sender_wallet: Wallet, recipient: UserAccount) -> bool:
        """Списывает стоимость подарка с кошелька дарителя."""
        sender_wallet.withdraw(float(self.price_coins))
        return recipient.is_active

    def format_gift_card(self) -> str:
        """Возвращает текстовое оформление подарка."""
        badge = " [Эксклюзив]" if self.is_limited_edition else ""
        return f"{self.icon_code} {self.gift_name}{badge} — {self.price_coins} монет"

    def apply_discount(self, discount_percent: int) -> int:
        """Применяет акционную скидку к стоимости подарка."""
        self.price_coins = max(1, int(self.price_coins * (100 - discount_percent) / 100))
        return self.price_coins
