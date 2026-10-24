# -*- coding: utf-8 -*-
"""Базовое исключение доменной модели социальной сети."""


class NetworkBaseException(Exception):
    """Базовый класс для всех ошибок и исключений социальной сети."""

    def __init__(self, message: str = "Ошибка социальной сети", code: int = 500) -> None:
        """Инициализация базового исключения."""
        super().__init__(message)
        self.message = message
        self.code = code
