# -*- coding: utf-8 -*-
"""Модуль комментария к публикации."""

from lab3.network.core.user_account import UserAccount
from lab3.network.content.post import Post
from lab3.network.content.reaction import Reaction


class Comment:
    """Представляет комментарий пользователя под записью."""

    def __init__(
        self,
        comment_id: str,
        post_id: str,
        author_id: str,
        text: str,
        likes_count: int = 0,
        is_hidden: bool = False,
    ) -> None:
        """Инициализация комментария."""
        self.comment_id = comment_id
        self.post_id = post_id
        self.author_id = author_id
        self.text = text
        self.likes_count = likes_count
        self.is_hidden = is_hidden

    def like(self, reaction: Reaction) -> int:
        """Регистрирует положительную реакцию на комментарий."""
        if reaction.is_positive():
            self.likes_count += 1
        return self.likes_count

    def hide(self) -> None:
        """Скрывает комментарий модератором."""
        self.is_hidden = True

    def edit_text(self, new_text: str, author: UserAccount) -> None:
        """Редактирует текст комментария автором."""
        if author.user_id == self.author_id:
            self.text = new_text

    def belongs_to_post(self, post: Post) -> bool:
        """Проверяет принадлежность комментария к конкретной записи."""
        return self.post_id == post.post_id

    def unhide(self) -> None:
        """Делает скрытый комментарий снова видимым."""
        self.is_hidden = False
