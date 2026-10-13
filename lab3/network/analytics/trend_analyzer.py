# -*- coding: utf-8 -*-
"""Модуль анализа трендов и виральности."""

from lab3.network.content.hashtag import Hashtag


class TrendAnalyzer:
    """Выявляет быстрорастущие тренды и популярные обсуждения."""

    def __init__(
        self,
        window_hours: int = 24,
        top_limit: int = 10,
        velocity_multiplier: float = 1.25,
        min_occurrences: int = 50,
    ) -> None:
        """Инициализация анализатора трендов."""
        self.window_hours = window_hours
        self.top_limit = top_limit
        self.velocity_multiplier = velocity_multiplier
        self.min_occurrences = min_occurrences

    def identify_trending_topics(self, tags: list) -> list:
        """Фильтрует список тегов по критерию популярности."""
        trending = []
        for tag in tags:
            if isinstance(tag, Hashtag) and tag.usage_count >= self.min_occurrences:
                trending.append(tag.tag_name)
        return trending[:self.top_limit]

    def calculate_growth_velocity(self, count_now: int, count_before: int) -> float:
        """Рассчитывает скорость роста цитируемости инфоповода."""
        if count_before <= 0:
            return float(count_now)
        velocity = (count_now - count_before) / count_before
        return round(velocity * self.velocity_multiplier, 2)

    def adjust_window(self, hours: int) -> None:
        """Изменяет временное окно агрегации трендов."""
        self.window_hours = max(1, min(168, hours))
