# -*- coding: utf-8 -*-
"""Модуль контактных данных пользователя."""

from lab3.network.exceptions.invalid_content_exception import InvalidContentException


class ContactInfo:
    """Хранит контактную информацию и геолокационные данные профиля."""

    def __init__(
        self,
        phone: str = "",
        city: str = "",
        country: str = "",
        telegram_handle: str = "",
        is_phone_confirmed: bool = False,
    ) -> None:
        """Инициализация контактных реквизитов пользователя."""
        self.phone = phone
        self.city = city
        self.country = country
        self.telegram_handle = telegram_handle
        self.is_phone_confirmed = is_phone_confirmed

    def confirm_phone(self, code: str) -> bool:
        """Подтверждает телефонный номер проверочным SMS-кодом."""
        if len(code) == 6 and code.isdigit():
            self.is_phone_confirmed = True
            return True
        return False

    def format_location(self) -> str:
        """Формирует текстовое представление местоположения пользователя."""
        if self.city and self.country:
            return f"{self.city}, {self.country}"
        return self.city or self.country or "Не указано"

    def update_phone(self, new_phone: str) -> None:
        """Обновляет телефонный номер с предварительной валидацией."""
        if not new_phone.startswith("+") or len(new_phone) < 8:
            raise InvalidContentException("Номер телефона должен начинаться с '+' и содержать не менее 8 цифр")
        self.phone = new_phone
        self.is_phone_confirmed = False
