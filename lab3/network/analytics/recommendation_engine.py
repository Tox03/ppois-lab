# -*- coding: utf-8 -*-
"""Модуль рекомендательной системы."""

from lab3.network.content.post import Post
from lab3.network.core.user_account import UserAccount


class RecommendationEngine:
    """Осуществляет расчет интересов и рекомендацию контента пользователям."""

    def __init__(
        self,
        model_version: str = "v2.4",
        diversity_factor: float = 0.3,
        decay_rate: float = 0.05,
        min_score_threshold: float = 0.5,
    ) -> None:
        """Инициализация алгоритма рекомендаций."""
        self.model_version = model_version
        self.diversity_factor = diversity_factor
        self.decay_rate = decay_rate
        self.min_score_threshold = min_score_threshold

    def score_post(self, post: Post, user: UserAccount) -> float:
        """Вычисляет предсказанную заинтересованность пользователя в записи."""
        if post.is_deleted or not user.is_active:
            return 0.0
        base_score = 0.8
        return round(base_score - self.decay_rate, 2)

    def recommend_users(self, user: UserAccount, candidates: list) -> list:
        """Подбирает рекомендуемых друзей и авторов на основе сходства профилей."""
        if not user.is_active:
            return []
        return [c for c in candidates if isinstance(c, UserAccount) and c.user_id != user.user_id]

    def update_diversity(self, new_factor: float) -> None:
        """Обновляет параметр разнообразия рекомендаций (explore vs exploit)."""
        self.diversity_factor = max(0.0, min(1.0, new_factor))
