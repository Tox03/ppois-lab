# -*- coding: utf-8 -*-
"""Модуль пакета сгруппированных уведомлений."""

from lab3.network.core.user_account import UserAccount
from lab3.network.notification.notification import Notification


class NotificationBatch:
    """Группирует однотипные уведомления для предотвращения спама."""

    def __init__(
        self,
        batch_id: str,
        recipient_id: str,
        count: int = 0,
        event_category: str = "likes",
        is_dispatched: bool = False,
    ) -> None:
        """Инициализация пакета уведомлений."""
        self.batch_id = batch_id
        self.recipient_id = recipient_id
        self.count = count
        self.event_category = event_category
        self.is_dispatched = is_dispatched

    def aggregate(self, notification: Notification) -> int:
        """Добавляет единичное уведомление в накопительный пакет."""
        if notification.recipient_id == self.recipient_id:
            self.count += 1
        return self.count

    def dispatch(self, recipient: UserAccount) -> str:
        """Формирует и отправляет сводное уведомление пользователю."""
        if recipient.user_id == self.recipient_id:
            self.is_dispatched = True
            return f"У вас {self.count} новых событий категории '{self.event_category}'"
        return "Ошибка адресата"

    def is_empty_batch(self) -> bool:
        """Проверяет, пуст ли текущий пакет уведомлений."""
        return self.count == 0
