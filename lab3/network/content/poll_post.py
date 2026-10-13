# -*- coding: utf-8 -*-
"""Модуль интерактивного опроса."""

from lab3.network.content.poll_option import PollOption
from lab3.network.content.post import Post
from lab3.network.exceptions.invalid_content_exception import InvalidContentException


class PollPost:
    """Публикация с голосованием и вариантами ответов."""

    def __init__(
        self,
        post_id: str,
        question: str,
        is_anonymous: bool = True,
        is_closed: bool = False,
        max_choices: int = 1,
        total_votes: int = 0,
    ) -> None:
        """Инициализация опроса."""
        self.post_id = post_id
        self.question = question
        self.is_anonymous = is_anonymous
        self.is_closed = is_closed
        self.max_choices = max_choices
        self.total_votes = total_votes

    def close_poll(self) -> None:
        """Завершает прием голосов в опросе."""
        self.is_closed = True

    def add_vote(self, option: PollOption) -> int:
        """Учитывает голос пользователя за выбранный вариант."""
        if self.is_closed:
            raise InvalidContentException("Голосование уже завершено")
        option.increment_vote()
        self.total_votes += 1
        return self.total_votes

    def calculate_results(self, options: list) -> None:
        """Пересчитывает проценты для всех вариантов ответа."""
        for opt in options:
            if isinstance(opt, PollOption):
                opt.update_percentage(self.total_votes)

    def can_vote(self, post: Post) -> bool:
        """Проверяет доступность опроса для голосования."""
        return not self.is_closed and not post.is_deleted
