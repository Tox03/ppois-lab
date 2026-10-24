# -*- coding: utf-8 -*-
"""Модуль пользовательской подписки на премиум-контент."""

from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.subscription_expired_exception import SubscriptionExpiredException
from lab3.network.monetization.subscription_tier import SubscriptionTier


class Subscription:
    """Управляет активной платной подпиской на автора или сервис."""

    def __init__(
        self,
        subscription_id: str,
        user_id: str,
        creator_id: str,
        tier_name: str = "VIP",
        expires_at: str = "2026-12-31",
        auto_renew: bool = True,
    ) -> None:
        """Инициализация подписки."""
        self.subscription_id = subscription_id
        self.user_id = user_id
        self.creator_id = creator_id
        self.tier_name = tier_name
        self.expires_at = expires_at
        self.auto_renew = auto_renew

    def renew(self, tier: SubscriptionTier, new_expiry: str) -> None:
        """Продлевает срок действия подписки."""
        self.tier_name = tier.name
        self.expires_at = new_expiry

    def cancel_auto_renew(self) -> None:
        """Отключает автоматическое списание за продление."""
        self.auto_renew = False

    def is_valid(self, current_date: str) -> bool:
        """Проверяет актуальность оплаченного периода."""
        if current_date > self.expires_at:
            raise SubscriptionExpiredException(self.tier_name)
        return True

    def belongs_to_subscriber(self, user: UserAccount) -> bool:
        """Проверяет принадлежность подписки пользователю."""
        return self.user_id == user.user_id

    def enable_auto_renew(self) -> None:
        """Включает автоматическое списание за продление."""
        self.auto_renew = True
