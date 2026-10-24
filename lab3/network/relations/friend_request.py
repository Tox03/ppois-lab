# -*- coding: utf-8 -*-
"""Модуль заявки на добавление в друзья."""

from lab3.network.core.user_account import UserAccount
from lab3.network.relations.friendship import Friendship


class FriendRequest:
    """Представляет входящую заявку на дружбу с сопроводительным сообщением."""

    def __init__(
        self,
        request_id: str,
        sender_id: str,
        receiver_id: str,
        message: str = "",
        status: str = "pending",
    ) -> None:
        """Инициализация заявки в друзья."""
        self.request_id = request_id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.message = message
        self.status = status

    def accept(self, receiver: UserAccount) -> Friendship:
        """Принимает заявку и формирует взаимную дружбу."""
        if receiver.user_id == self.receiver_id:
            self.status = "accepted"
            return Friendship(self.sender_id, self.receiver_id, "active")
        return Friendship(self.sender_id, self.receiver_id, "rejected")

    def reject(self, receiver: UserAccount) -> None:
        """Отклоняет входящую заявку в друзья."""
        if receiver.user_id == self.receiver_id:
            self.status = "rejected"

    def is_pending(self) -> bool:
        """Проверяет, ожидает ли заявка ответа адресата."""
        return self.status == "pending"
