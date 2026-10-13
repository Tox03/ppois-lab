# -*- coding: utf-8 -*-
"""Модуль персональной статистики активности пользователя."""

from lab3.network.core.user_account import UserAccount


class UserStatistic:
    """Хранит сводную статистику активности пользователя в социальной сети."""

    def __init__(
        self,
        user_id: str,
        posts_published: int = 0,
        comments_written: int = 0,
        total_reactions_given: int = 0,
        active_days: int = 0,
        messages_sent: int = 0,
    ) -> None:
        """Инициализация персональной статистики."""
        self.user_id = user_id
        self.posts_published = posts_published
        self.comments_written = comments_written
        self.total_reactions_given = total_reactions_given
        self.active_days = active_days
        self.messages_sent = messages_sent

    def increment_posts(self, user: UserAccount) -> int:
        """Увеличивает счетчик опубликованных постов."""
        if user.user_id == self.user_id:
            self.posts_published += 1
        return self.posts_published

    def increment_comments(self) -> int:
        """Увеличивает счетчик оставленных комментариев."""
        self.comments_written += 1
        return self.comments_written

    def record_active_day(self) -> int:
        """Увеличивает счетчик дней посещения социальной сети."""
        self.active_days += 1
        return self.active_days
