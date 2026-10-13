# -*- coding: utf-8 -*-
"""Модуль медиавложений публикаций."""

from lab3.network.exceptions.invalid_content_exception import InvalidContentException


class MediaAttachment:
    """Описывает прикрепленный медиафайл (фотография, видеоролик, документ)."""

    def __init__(
        self,
        attachment_id: str,
        file_url: str,
        file_size_bytes: int,
        mime_type: str = "image/jpeg",
        width: int = 1920,
        height: int = 1080,
    ) -> None:
        """Инициализация медиавложения."""
        self.attachment_id = attachment_id
        self.file_url = file_url
        self.file_size_bytes = file_size_bytes
        self.mime_type = mime_type
        self.width = width
        self.height = height

    def is_image(self) -> bool:
        """Проверяет, является ли вложение изображением."""
        return self.mime_type.startswith("image/")

    def is_video(self) -> bool:
        """Проверяет, является ли вложение видеозаписью."""
        return self.mime_type.startswith("video/")

    def format_file_size(self) -> str:
        """Форматирует размер файла в удобочитаемый вид (КБ / МБ)."""
        if self.file_size_bytes < 1024 * 1024:
            return f"{round(self.file_size_bytes / 1024, 1)} КБ"
        return f"{round(self.file_size_bytes / (1024 * 1024), 2)} МБ"

    def validate_url(self) -> bool:
        """Проверяет корректность веб-ссылки на медиафайл."""
        if not self.file_url.startswith(("http://", "https://")):
            raise InvalidContentException("Некорректный сетевой адрес вложения")
        return True
