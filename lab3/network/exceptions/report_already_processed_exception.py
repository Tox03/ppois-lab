# -*- coding: utf-8 -*-
"""Исключение повторной обработки жалобы."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class ReportAlreadyProcessedException(NetworkBaseException):
    """Вызывается при попытке повторно вынести решение по закрытой жалобе."""

    def __init__(self, report_id: str = "") -> None:
        """Инициализация исключения повторной обработки жалобы."""
        self.report_id = report_id
        super().__init__(f"Жалоба '{report_id}' уже рассмотрена модератором", 409)
