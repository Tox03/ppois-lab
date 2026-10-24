# -*- coding: utf-8 -*-
"""Модуль исчезающих историй (Stories)."""

from lab3.network.core.user_account import UserAccount


class Story:
    """Представляет короткую историю с ограниченным сроком жизни (24 часа)."""

    def __init__(
        self,
        story_id: str,
        author_id: str,
        media_url: str,
        duration_seconds: int = 15,
        views_count: int = 0,
        is_expired: bool = False,
    ) -> None:
        """Инициализация истории."""
        self.story_id = story_id
        self.author_id = author_id
        self.media_url = media_url
        self.duration_seconds = duration_seconds
        self.views_count = views_count
        self.is_expired = is_expired

    def record_view(self, viewer: UserAccount) -> int:
        """Фиксирует просмотр истории другим пользователем."""
        if not self.is_expired and viewer.user_id != self.author_id:
            self.views_count += 1
        return self.views_count

    def check_expiration(self, hours_passed: int) -> bool:
        """Проверяет истечение срока действия истории по прошедшим часам."""
        if hours_passed >= 24:
            self.is_expired = True
        return self.is_expired

    def archive(self) -> None:
        """Принудительно переводит историю в архив."""
        self.is_expired = True

    def add_interactive_sticker(self, sticker_name: str) -> str:
        """Прикрепляет интерактивный стикер к истории."""
        return f"Стикер '{sticker_name}' добавлен к истории {self.story_id}"
