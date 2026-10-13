# -*- coding: utf-8 -*-
"""Модуль членства пользователя в группе."""

from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.insufficient_privileges_exception import InsufficientPrivilegesException


class GroupMembership:
    """Определяет участие пользователя в тематическом сообществе."""

    def __init__(
        self,
        membership_id: str,
        group_id: str,
        user_id: str,
        role: str = "member",
        warning_count: int = 0,
    ) -> None:
        """Инициализация членства в группе."""
        self.membership_id = membership_id
        self.group_id = group_id
        self.user_id = user_id
        self.role = role
        self.warning_count = warning_count

    def warn_member(self) -> int:
        """Выносит предупреждение участнику за нарушение регламента группы."""
        self.warning_count += 1
        return self.warning_count

    def change_role(self, new_role: str, admin: UserAccount) -> None:
        """Изменяет статус участника администратором группы."""
        if not admin.is_active:
            raise InsufficientPrivilegesException("Администратор не активен")
        if new_role in ("member", "moderator", "admin"):
            self.role = new_role

    def is_moderator(self) -> bool:
        """Проверяет наличие прав модератора в группе."""
        return self.role in ("moderator", "admin")
