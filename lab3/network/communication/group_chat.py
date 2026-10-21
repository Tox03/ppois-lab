# -*- coding: utf-8 -*-
"""Модуль групповой беседы."""

from lab3.network.communication.chat import Chat
from lab3.network.communication.chat_member import ChatMember
from lab3.network.exceptions.group_capacity_exceeded_exception import GroupCapacityExceededException


class GroupChat:
    """Управляет групповой многопользовательской беседой."""

    def __init__(
        self,
        chat_id: str,
        title: str,
        admin_id: str,
        members_limit: int = 200,
        invite_code: str = "code123",
        is_muted: bool = False,
    ) -> None:
        """Инициализация групповой беседы."""
        self.chat_id = chat_id
        self.title = title
        self.admin_id = admin_id
        self.members_limit = members_limit
        self.invite_code = invite_code
        self.is_muted = is_muted

    def add_participant(self, member: ChatMember, current_count: int) -> bool:
        """Добавляет нового участника в групповой чат с проверкой лимита."""
        if current_count >= self.members_limit:
            raise GroupCapacityExceededException(self.members_limit)
        return not member.is_banned

    def remove_participant(self, member: ChatMember) -> None:
        """Исключает участника из беседы."""
        member.ban()

    def generate_invite(self, base_chat: Chat) -> str:
        """Генерирует новую ссылку-приглашение в групповой диалог."""
        self.invite_code = f"invite_{base_chat.chat_id}_{len(self.title)}"
        return self.invite_code

    def mute(self) -> None:
        """Отключает звуковые уведомления о сообщениях группы."""
        self.is_muted = True

    def unmute(self) -> None:
        """Включает звуковые уведомления о сообщениях группы."""
        self.is_muted = False
