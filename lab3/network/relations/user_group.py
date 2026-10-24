# -*- coding: utf-8 -*-
"""Модуль тематического сообщества (группы)."""

from lab3.network.core.user_account import UserAccount
from lab3.network.relations.group_membership import GroupMembership


class UserGroup:
    """Представляет публичное или закрытое сообщество по интересам."""

    def __init__(
        self,
        group_id: str,
        name: str,
        description: str,
        owner_id: str,
        is_verified: bool = False,
        is_closed: bool = False,
    ) -> None:
        """Инициализация сообщества."""
        self.group_id = group_id
        self.name = name
        self.description = description
        self.owner_id = owner_id
        self.is_verified = is_verified
        self.is_closed = is_closed

    def verify_group(self) -> None:
        """Присваивает официальную отметку верификации сообществу."""
        self.is_verified = True

    def close_group(self, owner: UserAccount) -> bool:
        """Переводит группу в закрытый режим по решению владельца."""
        if owner.user_id == self.owner_id:
            self.is_closed = True
            return True
        return False

    def open_group(self) -> None:
        """Делает группу открытой для свободного вступления."""
        self.is_closed = False

    def update_info(self, new_name: str, new_desc: str) -> None:
        """Обновляет заголовок и описание страницы группы."""
        self.name = new_name
        self.description = new_desc

    def has_member(self, membership: GroupMembership) -> bool:
        """Проверяет принадлежность членства к данной группе."""
        return self.group_id == membership.group_id

    def unverify_group(self) -> None:
        """Снимает отметку официальной верификации сообщества."""
        self.is_verified = False
