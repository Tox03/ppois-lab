# -*- coding: utf-8 -*-
"""Базовый модуль публикации (поста)."""

from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.content_blocked_exception import ContentBlockedException
from lab3.network.exceptions.invalid_content_exception import InvalidContentException


class Post:
    """Представляет запись на стене пользователя или в ленте социальной сети."""

    def __init__(
        self,
        post_id: str,
        author_id: str,
        text_content: str,
        created_at: str = "2026-01-01",
        is_pinned: bool = False,
        is_deleted: bool = False,
    ) -> None:
        """Инициализация публикации."""
        self.post_id = post_id
        self.author_id = author_id
        self.text_content = text_content
        self.created_at = created_at
        self.is_pinned = is_pinned
        self.is_deleted = is_deleted

    def pin(self, author: UserAccount) -> bool:
        """Закрепляет публикацию вверху ленты профиля."""
        if author.user_id != self.author_id:
            return False
        self.is_pinned = True
        return True

    def unpin(self) -> None:
        """Открепляет публикацию."""
        self.is_pinned = False

    def soft_delete(self) -> None:
        """Помечает публикацию удаленной."""
        self.is_deleted = True

    def edit_content(self, new_text: str, author: UserAccount) -> None:
        """Редактирует текст записи с проверкой авторства."""
        if self.is_deleted:
            raise ContentBlockedException(self.post_id, "Публикация уже удалена")
        if author.user_id != self.author_id:
            raise InvalidContentException("Редактировать запись может только автор")
        self.text_content = new_text
