# -*- coding: utf-8 -*-
"""Модуль личного сообщения между пользователями."""

from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.access_denied_exception import AccessDeniedException


class DirectMessage:
    """Представляет приватное сообщение диалога двух участников."""

    def __init__(
        self,
        message_id: str,
        sender_id: str,
        recipient_id: str,
        content: str,
        is_read: bool = False,
        is_delivered: bool = False,
    ) -> None:
        """Инициализация личного сообщения."""
        self.message_id = message_id
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.content = content
        self.is_read = is_read
        self.is_delivered = is_delivered

    def mark_as_read(self, recipient: UserAccount) -> bool:
        """Помечает сообщение прочитанным адресатом."""
        if recipient.user_id != self.recipient_id:
            raise AccessDeniedException("Только получатель может пометить сообщение как прочитанное")
        self.is_read = True
        return self.is_read

    def mark_as_delivered(self) -> None:
        """Устанавливает статус доставки сообщения на устройство."""
        self.is_delivered = True

    def format_preview(self) -> str:
        """Возвращает краткий предпросмотр сообщения для списка чатов."""
        preview = self.content[:30] + "..." if len(self.content) > 30 else self.content
        return f"[{'Проч.' if self.is_read else 'Нов.'}] {preview}"
