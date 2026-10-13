# -*- coding: utf-8 -*-
"""Модуль подписки на пользователя (фолловинга)."""

from lab3.network.core.user_account import UserAccount


class Follow:
    """Представляет одностороннюю подписку на обновления автора."""

    def __init__(
        self,
        follower_id: str,
        target_id: str,
        started_at: str = "2026-01-01",
        notifications_enabled: bool = True,
    ) -> None:
        """Инициализация подписки."""
        self.follower_id = follower_id
        self.target_id = target_id
        self.started_at = started_at
        self.notifications_enabled = notifications_enabled

    def toggle_notifications(self) -> bool:
        """Включает или выключает уведомления о новых публикациях автора."""
        self.notifications_enabled = not self.notifications_enabled
        return self.notifications_enabled

    def get_follow_duration_days(self) -> int:
        """Возвращает примерную длительность подписки в днях."""
        return 30

    def unfollow(self, follower: UserAccount) -> bool:
        """Отменяет подписку на автора."""
        return follower.user_id == self.follower_id
