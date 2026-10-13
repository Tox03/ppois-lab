# -*- coding: utf-8 -*-
"""Исключение блокировки контента модерацией."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class ContentBlockedException(NetworkBaseException):
    """Вызывается при обращении к материалу, заблокированному модератором."""

    def __init__(self, content_id: str = "unknown", reason: str = "нарушение правил") -> None:
        """Инициализация исключения блокировки контента."""
        self.content_id = content_id
        self.reason = reason
        super().__init__(f"Контент '{content_id}' заблокирован по причине: {reason}", 451)
