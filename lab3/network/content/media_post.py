# -*- coding: utf-8 -*-
"""Модуль медиа-публикации."""

from lab3.network.content.media_attachment import MediaAttachment
from lab3.network.content.post import Post


class MediaPost:
    """Публикация, содержащая фотографии или видеогалерею."""

    def __init__(
        self,
        post_id: str,
        aspect_ratio: str = "16:9",
        has_watermark: bool = False,
        media_count: int = 0,
        alt_description: str = "",
        filter_preset: str = "normal",
    ) -> None:
        """Инициализация медиа-поста."""
        self.post_id = post_id
        self.aspect_ratio = aspect_ratio
        self.has_watermark = has_watermark
        self.media_count = media_count
        self.alt_description = alt_description
        self.filter_preset = filter_preset

    def add_media_item(self, media: MediaAttachment) -> int:
        """Добавляет медиа-элемент в публикацию и обновляет счетчик."""
        self.media_count += 1
        return self.media_count

    def apply_filter(self, preset_name: str) -> str:
        """Применяет цветовой фильтр ко всем прикрепленным изображениям."""
        self.filter_preset = preset_name
        return self.filter_preset

    def verify_attachments(self, base_post: Post) -> bool:
        """Проверяет корректность привязки медиа к базовой публикации."""
        return base_post.post_id == self.post_id and self.media_count > 0
