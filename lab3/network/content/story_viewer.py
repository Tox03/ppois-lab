# -*- coding: utf-8 -*-
"""Модуль зрителя истории."""

from lab3.network.core.user_account import UserAccount


class StoryViewer:
    """Фиксирует факт просмотра конкретной истории пользователем."""

    def __init__(
        self,
        viewer_id: str,
        story_id: str,
        viewed_at: str = "2026-01-01",
        has_reacted: bool = False,
    ) -> None:
        """Инициализация записи о просмотре истории."""
        self.viewer_id = viewer_id
        self.story_id = story_id
        self.viewed_at = viewed_at
        self.has_reacted = has_reacted

    def mark_reaction(self, user: UserAccount) -> bool:
        """Отмечает отправку реакции на историю зрителем."""
        if user.user_id == self.viewer_id:
            self.has_reacted = True
        return self.has_reacted

    def get_watch_delay(self) -> str:
        """Возвращает информацию о времени просмотра."""
        return f"Просмотрено в {self.viewed_at}"

    def format_viewer_info(self) -> str:
        """Форматирует краткую сводку о зрителе."""
        status = "с реакцией" if self.has_reacted else "без реакции"
        return f"Зритель {self.viewer_id}: {status}"
