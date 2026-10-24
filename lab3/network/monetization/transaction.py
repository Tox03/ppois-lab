# -*- coding: utf-8 -*-
"""Модуль денежной транзакции."""

from lab3.network.exceptions.payment_failed_exception import PaymentFailedException
from lab3.network.monetization.wallet import Wallet


class Transaction:
    """Представляет финансовый перевод между кошельками или оплату услуги."""

    def __init__(
        self,
        tx_id: str,
        sender_wallet_id: str,
        receiver_wallet_id: str,
        amount: float,
        status: str = "pending",
        fee: float = 0.0,
    ) -> None:
        """Инициализация транзакции."""
        self.tx_id = tx_id
        self.sender_wallet_id = sender_wallet_id
        self.receiver_wallet_id = receiver_wallet_id
        self.amount = amount
        self.status = status
        self.fee = fee

    def execute(self, sender: Wallet, receiver: Wallet) -> bool:
        """Исполняет финансовую транзакцию с удержанием комиссии."""
        if self.status != "pending":
            return False
        total = self.amount + self.fee
        sender.withdraw(total)
        receiver.deposit(self.amount)
        self.status = "completed"
        return True

    def refund(self, sender: Wallet, receiver: Wallet) -> None:
        """Выполняет возврат средств отправителю."""
        if self.status == "completed":
            receiver.withdraw(self.amount)
            sender.deposit(self.amount)
            self.status = "refunded"

    def calculate_fee(self, fee_percent: float = 1.5) -> float:
        """Рассчитывает комиссию платежного шлюза."""
        self.fee = round(self.amount * (fee_percent / 100.0), 2)
        return self.fee

    def validate_amount(self) -> bool:
        """Проверяет корректность суммы платежа."""
        if self.amount <= 0:
            raise PaymentFailedException("Сумма перевода должна быть больше нуля")
        return True
