# -*- coding: utf-8 -*-
"""Модуль сессионного токена авторизации."""

from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.authentication_exception import AuthenticationException


class SessionToken:
    """Управляет жизненным циклом токена веб-сессии пользователя."""

    def __init__(
        self,
        token_value: str,
        user_id: str,
        ip_address: str,
        device_info: str = "Chrome/Win",
        expires_in_hours: int = 24,
        is_active: bool = True,
    ) -> None:
        """Инициализация сессионного токена."""
        self.token_value = token_value
        self.user_id = user_id
        self.ip_address = ip_address
        self.device_info = device_info
        self.expires_in_hours = expires_in_hours
        self.is_active = is_active

    def validate(self, current_user: UserAccount) -> bool:
        """Проверяет валидность токена и активность связанного аккаунта."""
        if not self.is_active or not current_user.is_active:
            raise AuthenticationException("Токен авторизации недействителен или отозван")
        return current_user.user_id == self.user_id

    def revoke(self) -> None:
        """Осуществляет отзыв (выход из аккаунта) текущей сессии."""
        self.is_active = False

    def renew(self, extension_hours: int) -> int:
        """Продлевает срок жизни активной сессии."""
        if self.is_active:
            self.expires_in_hours += max(1, extension_hours)
        return self.expires_in_hours
