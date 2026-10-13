# -*- coding: utf-8 -*-
"""Модуль варианта ответа в опросе."""


class PollOption:
    """Представляет отдельный вариант ответа в голосовании."""

    def __init__(
        self,
        option_id: str,
        option_text: str,
        votes_count: int = 0,
        percentage: float = 0.0,
    ) -> None:
        """Инициализация пункта опроса."""
        self.option_id = option_id
        self.option_text = option_text
        self.votes_count = votes_count
        self.percentage = percentage

    def increment_vote(self) -> int:
        """Увеличивает счетчик голосов за данный пункт."""
        self.votes_count += 1
        return self.votes_count

    def update_percentage(self, total_votes: int) -> float:
        """Вычисляет долю голосов в процентах от общего числа участников."""
        if total_votes > 0:
            self.percentage = round((self.votes_count / total_votes) * 100.0, 1)
        else:
            self.percentage = 0.0
        return self.percentage

    def format_label(self) -> str:
        """Формирует текстовую подпись варианта с числом голосов."""
        return f"{self.option_text} ({self.votes_count} гол., {self.percentage}%)"
