# -*- coding: utf-8 -*-
"""Модуль фотоальбома пользователя."""

from lab3.network.content.media_attachment import MediaAttachment
from lab3.network.core.user_account import UserAccount


class Album:
    """Коллекция сохраненных фотографий и медиафайлов."""

    def __init__(
        self,
        album_id: str,
        owner_id: str,
        title: str,
        description: str = "",
        photos_count: int = 0,
        is_private: bool = False,
    ) -> None:
        """Инициализация фотоальбома."""
        self.album_id = album_id
        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.photos_count = photos_count
        self.is_private = is_private

    def add_photo(self, photo: MediaAttachment, owner: UserAccount) -> int:
        """Добавляет фотоснимок в альбом с проверкой владельца."""
        if owner.user_id == self.owner_id and photo.is_image():
            self.photos_count += 1
        return self.photos_count

    def remove_photo(self) -> int:
        """Уменьшает счетчик снимков в альбоме."""
        if self.photos_count > 0:
            self.photos_count -= 1
        return self.photos_count

    def toggle_privacy(self) -> bool:
        """Переключает видимость альбома (публичный/скрытый)."""
        self.is_private = not self.is_private
        return self.is_private
