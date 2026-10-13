# -*- coding: utf-8 -*-
"""Модуль элемента новостной ленты."""

from lab3.network.content.post import Post


class FeedItem:
    """Представляет публикацию внутри ранжированной пользовательской ленты."""

    def __init__(
        self,
        item_id: str,
        post_id: str,
        relevance_score: float = 1.0,
        source_type: str = "friend",
        seen: bool = False,
    ) -> None:
        """Инициализация элемента ленты."""
        self.item_id = item_id
        self.post_id = post_id
        self.relevance_score = relevance_score
        self.source_type = source_type
        self.seen = seen

    def mark_as_seen(self) -> None:
        """Помечает пост как просмотренный в ленте."""
        self.seen = True

    def boost_score(self, factor: float) -> float:
        """Повышает ранжирующий балл записи в ленте."""
        self.relevance_score = round(self.relevance_score * max(1.0, factor), 3)
        return self.relevance_score

    def penalize_score(self, penalty: float) -> float:
        """Понижает позицию записи в ленте за нерелевантность."""
        self.relevance_score = max(0.01, round(self.relevance_score - penalty, 3))
        return self.relevance_score

    def matches_post(self, post: Post) -> bool:
        """Проверяет соответствие элемента конкретной публикации."""
        return self.post_id == post.post_id
