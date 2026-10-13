# -*- coding: utf-8 -*-
"""Модуль голосового аудиосообщения."""

from lab3.network.exceptions.invalid_content_exception import InvalidContentException


class AudioMessage:
    """Представляет голосовое сообщение с расшифровкой речи в текст."""

    def __init__(
        self,
        audio_id: str,
        duration_seconds: int,
        audio_url: str,
        transcription: str = "",
        waveform_samples: int = 64,
    ) -> None:
        """Инициализация аудиосообщения."""
        self.audio_id = audio_id
        self.duration_seconds = duration_seconds
        self.audio_url = audio_url
        self.transcription = transcription
        self.waveform_samples = waveform_samples

    def transcribe(self, text: str) -> str:
        """Записывает распознанный текст голосового сообщения."""
        if not text:
            raise InvalidContentException("Расшифровка аудио не может быть пустой")
        self.transcription = text
        return self.transcription

    def is_long_audio(self) -> bool:
        """Определяет, превышает ли аудиозапись 2 минуты."""
        return self.duration_seconds > 120

    def format_duration(self) -> str:
        """Форматирует длительность трека в вид ММ:СС."""
        minutes = self.duration_seconds // 60
        seconds = self.duration_seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
