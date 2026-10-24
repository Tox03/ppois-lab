# -*- coding: utf-8 -*-
"""Исключение превышения лимита активности."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class RateLimitExceededException(NetworkBaseException):
    """Вызывается при превышении допустимого лимита запросов или сообщений."""

    def __init__(self, limit: int = 60) -> None:
        """Инициализация исключения лимита запросов."""
        self.limit = limit
        super().__init__(f"Превышен допустимый лимит активности: максимум {limit} в минуту", 429)
