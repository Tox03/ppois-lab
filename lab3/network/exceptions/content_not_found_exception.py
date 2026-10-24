# -*- coding: utf-8 -*-
"""Исключение отсутствия контента."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class ContentNotFoundException(NetworkBaseException):
    """Вызывается при попытке найти несуществующую публикацию, историю или комментарий."""

    def __init__(self, content_id: str = "unknown") -> None:
        """Инициализация исключения отсутствия контента."""
        self.content_id = content_id
        super().__init__(f"Элемент контента '{content_id}' не найден", 404)
