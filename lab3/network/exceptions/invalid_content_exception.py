# -*- coding: utf-8 -*-
"""Исключение некорректного контента."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class InvalidContentException(NetworkBaseException):
    """Вызывается при нарушении формата текста, длины или недопустимых символах."""

    def __init__(self, details: str = "Некорректное содержимое") -> None:
        """Инициализация исключения некорректного контента."""
        self.details = details
        super().__init__(f"Недопустимое содержимое публикации: {details}", 400)
