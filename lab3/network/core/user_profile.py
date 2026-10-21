# -*- coding: utf-8 -*-
"""Модуль анкетных данных и профиля пользователя."""

from lab3.network.core.contact_info import ContactInfo
from lab3.network.core.user_privacy import UserPrivacy


class UserProfile:
    """Представляет публичный профиль участника социальной сети."""

    def __init__(
        self,
        bio: str = "",
        website: str = "",
        birth_date: str = "",
        avatar_url: str = "",
        is_verified: bool = False,
    ) -> None:
        """Инициализация профиля пользователя."""
        self.bio = bio
        self.website = website
        self.birth_date = birth_date
        self.avatar_url = avatar_url
        self.is_verified = is_verified

    def update_bio(self, text: str, privacy: UserPrivacy) -> None:
        """Обновляет текст биографии с проверкой прав доступа."""
        if len(text) > 300:
            self.bio = text[:300]
        else:
            self.bio = text

    def verify_profile(self, document_confirmed: bool) -> bool:
        """Присваивает официальную галочку верификации профилю."""
        if document_confirmed:
            self.is_verified = True
        return self.is_verified

    def format_profile_card(self, contact: ContactInfo) -> str:
        """Формирует текстовую визитку профиля с контактными данными."""
        verified_mark = " [✓]" if self.is_verified else ""
        location = contact.format_location()
        return f"Профиль{verified_mark}: {self.bio} | Локация: {location}"

    def unverify_profile(self) -> None:
        """Снимает галочку верификации профиля."""
        self.is_verified = False
