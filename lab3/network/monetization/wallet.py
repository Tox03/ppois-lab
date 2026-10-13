# -*- coding: utf-8 -*-
"""Модуль виртуального кошелька пользователя."""

from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.payment_failed_exception import PaymentFailedException


class Wallet:
    """Хранит денежный баланс и токены внутренней экономики сети."""

    def __init__(
        self,
        wallet_id: str,
        user_id: str,
        balance: float = 0.0,
        currency: str = "RUB",
        is_frozen: bool = False,
    ) -> None:
        """Инициализация электронного кошелька."""
        self.wallet_id = wallet_id
        self.user_id = user_id
        self.balance = balance
        self.currency = currency
        self.is_frozen = is_frozen

    def deposit(self, amount: float) -> float:
        """Пополняет баланс кошелька."""
        if amount <= 0:
            raise PaymentFailedException("Сумма пополнения должна быть положительной")
        self.balance += round(amount, 2)
        return self.balance

    def withdraw(self, amount: float) -> float:
        """Списывает средства с баланса с проверкой остатка."""
        if self.is_frozen:
            raise PaymentFailedException("Кошелек заблокирован системой безопасности")
        if amount > self.balance:
            raise PaymentFailedException(f"Недостаточно средств: запрошено {amount}, доступно {self.balance}")
        self.balance -= round(amount, 2)
        return self.balance

    def freeze(self) -> None:
        """Замораживает проведение операций по кошельку."""
        self.is_frozen = True

    def unfreeze(self) -> None:
        """Размораживает баланс кошелька."""
        self.is_frozen = False

    def belongs_to_user(self, user: UserAccount) -> bool:
        """Проверяет принадлежность кошелька владельцу."""
        return self.user_id == user.user_id
