# -*- coding: utf-8 -*-
"""Модуль поисковой службы социальной сети."""

from lab3.network.content.hashtag import Hashtag
from lab3.network.content.post import Post
from lab3.network.core.user_account import UserAccount


class SearchService:
    """Обеспечивает полнотекстовый поиск по пользователям, публикациям и тегам."""

    def __init__(
        self,
        index_name: str = "global_search",
        indexed_items_count: int = 0,
        min_query_length: int = 3,
        fuzzy_matching: bool = True,
        max_results: int = 20,
    ) -> None:
        """Инициализация поискового индекса."""
        self.index_name = index_name
        self.indexed_items_count = indexed_items_count
        self.min_query_length = min_query_length
        self.fuzzy_matching = fuzzy_matching
        self.max_results = max_results

    def search_users(self, query: str, user_pool: list) -> list:
        """Выполняет поиск пользователей по логину."""
        if len(query) < self.min_query_length:
            return []
        query_str = query.lower()
        matches = [user_item for user_item in user_pool if isinstance(user_item, UserAccount) and query_str in user_item.username.lower()]
        return matches[:self.max_results]

    def search_posts(self, query: str, post_pool: list) -> list:
        """Выполняет поиск публикаций по ключевым словам."""
        if len(query) < self.min_query_length:
            return []
        query_str = query.lower()
        matches = [post_item for post_item in post_pool if isinstance(post_item, Post) and query_str in post_item.text_content.lower()]
        return matches[:self.max_results]

    def index_document(self, tag: Hashtag) -> int:
        """Индексирует хэштег для быстрого автодополнения."""
        self.indexed_items_count += 1
        return self.indexed_items_count
