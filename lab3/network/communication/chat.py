# -*- coding: utf-8 -*-
"""Модуль диалога (чата)."""


class Chat:
    """Представляет диалог в системе сообщений."""

    def __init__(
        self,
        chat_id: str,
        created_at: str = "2026-01-01",
        last_message_at: str = "2026-01-01",
        messages_count: int = 0,
        is_archived: bool = False,
    ) -> None:
        """Инициализация диалога."""
        self.chat_id = chat_id
        self.created_at = created_at
        self.last_message_at = last_message_at
        self.messages_count = messages_count
        self.is_archived = is_archived

    def archive(self) -> None:
        """Переносит диалог в архив."""
        self.is_archived = True

    def unarchive(self) -> None:
        """Извлекает диалог из архива."""
        self.is_archived = False

    def update_last_activity(self, timestamp: str) -> None:
        """Обновляет время последней активности и инкрементирует число сообщений."""
        self.last_message_at = timestamp
        self.messages_count += 1
