# -*- coding: utf-8 -*-
"""Модуль персонализированной ленты новостей."""

from lab3.network.analytics.feed_item import FeedItem
from lab3.network.core.user_account import UserAccount


class Feed:
    """Формирует и ранжирует новостную ленту для пользователя."""

    def __init__(
        self,
        user_id: str,
        algorithm_type: str = "chronological",
        items_count: int = 0,
        refresh_interval_sec: int = 60,
        include_ads: bool = True,
    ) -> None:
        """Инициализация ленты."""
        self.user_id = user_id
        self.algorithm_type = algorithm_type
        self.items_count = items_count
        self.refresh_interval_sec = refresh_interval_sec
        self.include_ads = include_ads

    def add_item(self, item: FeedItem) -> int:
        """Включает новую запись в ленту."""
        self.items_count += 1
        return self.items_count

    def filter_by_algorithm(self, user: UserAccount) -> str:
        """Применяет алгоритмическое либо хронологическое ранжирование."""
        if user.user_id == self.user_id:
            return f"Лента {self.user_id} обновлена по алгоритму {self.algorithm_type}"
        return "Чужая лента"

    def clear_feed(self) -> None:
        """Очищает кэшированные публикации в ленте."""
        self.items_count = 0

    def remove_item(self) -> int:
        """Удаляет элемент из ленты."""
        if self.items_count > 0:
            self.items_count -= 1
        return self.items_count
