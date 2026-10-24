# -*- coding: utf-8 -*-
"""Модуль канала доставки уведомлений."""

from lab3.network.notification.notification import Notification


class NotificationChannel:
    """Описывает транспорт доставки сообщений (Push, Email, SMS, Web)."""

    def __init__(
        self,
        channel_name: str = "push",
        is_enabled: bool = True,
        delivery_timeout_sec: int = 5,
        retry_count: int = 3,
        priority: int = 1,
    ) -> None:
        """Инициализация канала уведомлений."""
        self.channel_name = channel_name
        self.is_enabled = is_enabled
        self.delivery_timeout_sec = delivery_timeout_sec
        self.retry_count = retry_count
        self.priority = priority

    def deliver(self, notification: Notification) -> bool:
        """Осуществляет отправку уведомления через выбранный канал."""
        if not self.is_enabled:
            return False
        return len(notification.recipient_id) > 0

    def toggle_channel(self) -> bool:
        """Включает или выключает данный транспорт доставки."""
        self.is_enabled = not self.is_enabled
        return self.is_enabled

    def adjust_timeout(self, seconds: int) -> None:
        """Настраивает таймаут ожидания ответа шлюза."""
        self.delivery_timeout_sec = max(1, seconds)
