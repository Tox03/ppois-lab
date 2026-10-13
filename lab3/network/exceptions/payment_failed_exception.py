# -*- coding: utf-8 -*-
"""Исключение ошибки платежа."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class PaymentFailedException(NetworkBaseException):
    """Вызывается при неудачном списании средств или недостатке баланса."""

    def __init__(self, reason: str = "Недостаточно средств") -> None:
        """Инициализация исключения платежа."""
        self.reason = reason
        super().__init__(f"Транзакция отклонена: {reason}", 402)
