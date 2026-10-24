# -*- coding: utf-8 -*-
"""Модуль тематических хэштегов."""

from lab3.network.exceptions.invalid_content_exception import InvalidContentException


class Hashtag:
    """Хранит информацию о поисковом хэштеге и частоте его использования."""

    def __init__(
        self,
        tag_name: str,
        usage_count: int = 1,
        trending_score: float = 0.0,
        is_blacklisted: bool = False,
    ) -> None:
        """Инициализация хэштега."""
        self.tag_name = tag_name.lower().lstrip("#")
        self.usage_count = usage_count
        self.trending_score = trending_score
        self.is_blacklisted = is_blacklisted

    def increment_usage(self) -> int:
        """Увеличивает счетчик цитируемости хэштега."""
        if self.is_blacklisted:
            raise InvalidContentException(f"Хэштег #{self.tag_name} заблокирован")
        self.usage_count += 1
        return self.usage_count

    def update_trend_score(self, new_posts_last_hour: int) -> float:
        """Пересчитывает показатель трендовости на основе динамики публикаций."""
        self.trending_score = round(self.usage_count * 0.2 + new_posts_last_hour * 1.5, 2)
        return self.trending_score

    def validate_tag(self) -> bool:
        """Проверяет допустимость символов в названии тега."""
        if not self.tag_name or " " in self.tag_name or len(self.tag_name) > 50:
            raise InvalidContentException("Хэштег не должен содержать пробелов и превышать 50 знаков")
        return True
