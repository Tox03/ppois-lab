# -*- coding: utf-8 -*-
"""Модуль автоматической фильтрации спама и спам-скоринга."""

from lab3.network.exceptions.content_blocked_exception import ContentBlockedException


class ContentFilter:
    """Автоматический анализатор контента на спам и нежелательный материал."""

    def __init__(
        self,
        filter_name: str = "SpamDetector",
        spam_threshold: float = 0.8,
        nsfw_detection: bool = True,
        auto_block: bool = True,
        inspections_count: int = 0,
    ) -> None:
        """Инициализация алгоритма фильтрации."""
        self.filter_name = filter_name
        self.spam_threshold = spam_threshold
        self.nsfw_detection = nsfw_detection
        self.auto_block = auto_block
        self.inspections_count = inspections_count

    def evaluate_spam_score(self, text: str) -> float:
        """Оценивает вероятность спама в текстовом фрагменте от 0.0 до 1.0."""
        self.inspections_count += 1
        suspicious_words = ("http", "скидка", "купи", "крипта", "казино", "бесплатно")
        matches = sum(1 for w in suspicious_words if w in text.lower())
        score = min(1.0, round(matches * 0.25, 2))
        return score

    def inspect_text(self, text: str, content_id: str) -> bool:
        """Проверяет текст и выбрасывает исключение при превышении порога спама."""
        score = self.evaluate_spam_score(text)
        if score >= self.spam_threshold and self.auto_block:
            raise ContentBlockedException(content_id, f"Автофильтр: превышен порог спама ({score})")
        return True

    def update_threshold(self, new_threshold: float) -> None:
        """Настраивает чувствительность детектора спама."""
        self.spam_threshold = max(0.1, min(1.0, new_threshold))
