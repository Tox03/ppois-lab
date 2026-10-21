# -*- coding: utf-8 -*-
"""Модуль участника группового чата."""

from lab3.network.core.user_account import UserAccount


class ChatMember:
    """Определяет роль и статус участника группового чата."""

    def __init__(
        self,
        member_id: str,
        chat_id: str,
        role: str = "member",
        joined_at: str = "2026-01-01",
        is_banned: bool = False,
    ) -> None:
        """Инициализация участника беседы."""
        self.member_id = member_id
        self.chat_id = chat_id
        self.role = role
        self.joined_at = joined_at
        self.is_banned = is_banned

    def promote_to_admin(self, admin_account: UserAccount) -> bool:
        """Повышает участника до администратора чата."""
        if admin_account.is_active and not self.is_banned:
            self.role = "admin"
            return True
        return False

    def demote(self) -> None:
        """Понижает статус участника до обычного."""
        self.role = "member"

    def ban(self) -> None:
        """Блокирует участника в данном чате."""
        self.is_banned = True
        self.role = "banned"

    def unban(self) -> None:
        """Снимает блокировку с участника чата."""
        self.is_banned = False
        self.role = "member"
