# -*- coding: utf-8 -*-
"""Исключение превышения лимита участников группы."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class GroupCapacityExceededException(NetworkBaseException):
    """Вызывается при попытке вступить в переполненную группу или чат."""

    def __init__(self, max_limit: int = 1000) -> None:
        """Инициализация исключения переполнения группы."""
        self.max_limit = max_limit
        super().__init__(f"Превышен лимит участников группы: максимум {max_limit}", 400)
