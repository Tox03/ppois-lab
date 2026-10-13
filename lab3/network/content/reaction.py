# -*- coding: utf-8 -*-
"""Модуль пользовательских реакций на контент."""

from lab3.network.core.user_account import UserAccount


class Reaction:
    """Представляет эмоциональную реакцию пользователя на пост или комментарий."""

    def __init__(
        self,
        reaction_type: str = "like",
        user_id: str = "",
        target_id: str = "",
        created_at: str = "2026-01-01",
    ) -> None:
        """Инициализация реакции пользователя."""
        self.reaction_type = reaction_type
        self.user_id = user_id
        self.target_id = target_id
        self.created_at = created_at

    def update_type(self, new_type: str, user: UserAccount) -> None:
        """Изменяет тип реакции (like, love, haha, wow, sad, angry)."""
        valid_types = ("like", "love", "haha", "wow", "sad", "angry")
        if new_type in valid_types and user.user_id == self.user_id:
            self.reaction_type = new_type

    def is_positive(self) -> bool:
        """Определяет, выражает ли реакция положительные эмоции."""
        return self.reaction_type in ("like", "love", "haha", "wow")

    def get_emoji(self) -> str:
        """Возвращает соответствующий текстовый эмодзи."""
        emojis = {
            "like": "👍",
            "love": "❤️",
            "haha": "😄",
            "wow": "😮",
            "sad": "😢",
            "angry": "😡",
        }
        return emojis.get(self.reaction_type, "👍")
