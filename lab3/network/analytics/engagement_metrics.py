# -*- coding: utf-8 -*-
"""Модуль аналитики вовлеченности аудитории."""

from lab3.network.content.post import Post


class EngagementMetrics:
    """Агрегирует статистику просмотров, репостов, закладок и реакций."""

    def __init__(
        self,
        post_id: str,
        views: int = 0,
        likes: int = 0,
        shares: int = 0,
        bookmarks: int = 0,
        comments_count: int = 0,
    ) -> None:
        """Инициализация счетчиков вовлеченности."""
        self.post_id = post_id
        self.views = views
        self.likes = likes
        self.shares = shares
        self.bookmarks = bookmarks
        self.comments_count = comments_count

    def calculate_engagement_rate(self) -> float:
        """Рассчитывает коэффициент вовлеченности (ER, %)."""
        if self.views == 0:
            return 0.0
        interactions = self.likes + self.shares + self.bookmarks + self.comments_count
        return round((interactions / self.views) * 100.0, 2)

    def record_share(self, post: Post) -> int:
        """Фиксирует распространение записи другим пользователем."""
        if post.post_id == self.post_id:
            self.shares += 1
        return self.shares

    def record_bookmark(self) -> int:
        """Фиксирует сохранение записи в закладки."""
        self.bookmarks += 1
        return self.bookmarks
