# -*- coding: utf-8 -*-
"""Модуль сообщения в чате."""

from lab3.network.communication.chat import Chat
from lab3.network.core.user_account import UserAccount


class ChatMessage:
    """Сообщение, отправленное внутри группового или парного чата."""

    def __init__(
        self,
        message_id: str,
        chat_id: str,
        sender_id: str,
        text: str,
        reply_to_id: str = "",
        is_pinned: bool = False,
    ) -> None:
        """Инициализация сообщения чата."""
        self.message_id = message_id
        self.chat_id = chat_id
        self.sender_id = sender_id
        self.text = text
        self.reply_to_id = reply_to_id
        self.is_pinned = is_pinned

    def pin(self, chat: Chat) -> bool:
        """Закрепляет данное сообщение в шапке чата."""
        if chat.chat_id == self.chat_id:
            self.is_pinned = True
            return True
        return False

    def unpin(self) -> None:
        """Снимает закрепление с сообщения."""
        self.is_pinned = False

    def set_reply(self, target_message_id: str, sender: UserAccount) -> None:
        """Устанавливает ссылку на цитируемое сообщение при ответе."""
        if sender.user_id == self.sender_id:
            self.reply_to_id = target_message_id
