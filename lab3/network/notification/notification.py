# -*- coding: utf-8 -*-
"""Модуль пользовательского уведомления."""

from lab3.network.core.user_account import UserAccount


class Notification:
    """Представляет системное уведомление о событиях (лайк, ответ, подписка)."""

    def __init__(
        self,
        notification_id: str,
        recipient_id: str,
        actor_id: str,
        event_type: str = "like",
        is_read: bool = False,
        created_at: str = "2026-01-01",
    ) -> None:
        """Инициализация уведомления."""
        self.notification_id = notification_id
        self.recipient_id = recipient_id
        self.actor_id = actor_id
        self.event_type = event_type
        self.is_read = is_read
        self.created_at = created_at

    def mark_as_read(self, recipient: UserAccount) -> bool:
        """Помечает уведомление как прочитанное адресатом."""
        if recipient.user_id == self.recipient_id:
            self.is_read = True
            return True
        return False

    def format_message(self) -> str:
        """Форматирует текст уведомления на основе типа события."""
        templates = {
            "like": f"Пользователь {self.actor_id} оценил вашу публикацию",
            "comment": f"Пользователь {self.actor_id} оставил комментарий",
            "friend_request": f"Пользователь {self.actor_id} отправил вам заявку в друзья",
            "mention": f"Пользователь {self.actor_id} упомянул вас",
        }
        return templates.get(self.event_type, f"Новое событие от {self.actor_id}")

    def is_urgent(self) -> bool:
        """Проверяет критичность уведомления для мгновенной доставки."""
        return self.event_type in ("security_alert", "password_reset", "ban_notice")
