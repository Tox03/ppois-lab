# -*- coding: utf-8 -*-
"""Модуль текстовой публикации (статьи)."""

from lab3.network.content.post import Post


class TextPost:
    """Специализированная текстовая запись с расширенным оформлением."""

    def __init__(
        self,
        post_id: str,
        font_style: str = "sans-serif",
        background_color: str = "#FFFFFF",
        reading_time_minutes: int = 1,
        word_count: int = 0,
        summary: str = "",
    ) -> None:
        """Инициализация статьи."""
        self.post_id = post_id
        self.font_style = font_style
        self.background_color = background_color
        self.reading_time_minutes = reading_time_minutes
        self.word_count = word_count
        self.summary = summary

    def calculate_reading_time(self, post: Post) -> int:
        """Рассчитывает ориентировочное время чтения статьи."""
        words = len(post.text_content.split())
        self.word_count = words
        self.reading_time_minutes = max(1, words // 200)
        return self.reading_time_minutes

    def generate_summary(self, post: Post) -> str:
        """Генерирует краткую аннотацию из первого предложения записи."""
        sentences = post.text_content.split(". ")
        self.summary = sentences[0] if sentences else post.text_content[:100]
        return self.summary

    def apply_styling(self, font: str, bg: str) -> None:
        """Настраивает визуальные параметры шрифта и подложки статьи."""
        self.font_style = font
        self.background_color = bg
