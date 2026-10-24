# -*- coding: utf-8 -*-
"""Модуль сессии голосового или видеозвонка."""

from lab3.network.core.user_account import UserAccount


class CallSession:
    """Представляет сеанс аудио- или видеозвонка между пользователями."""

    def __init__(
        self,
        call_id: str,
        initiator_id: str,
        is_video: bool = False,
        duration_seconds: int = 0,
        status: str = "ringing",
        quality_score: float = 5.0,
    ) -> None:
        """Инициализация сеанса звонка."""
        self.call_id = call_id
        self.initiator_id = initiator_id
        self.is_video = is_video
        self.duration_seconds = duration_seconds
        self.status = status
        self.quality_score = quality_score

    def start_call(self, participant: UserAccount) -> bool:
        """Начинает голосовой вызов при подтверждении собеседника."""
        if participant.is_active:
            self.status = "connected"
            return True
        self.status = "rejected"
        return False

    def end_call(self, total_seconds: int) -> int:
        """Завершает звонок и фиксирует продолжительность разговора."""
        self.duration_seconds = max(0, total_seconds)
        self.status = "ended"
        return self.duration_seconds

    def rate_quality(self, score: float) -> float:
        """Сохраняет субъективную оценку качества связи пользователем."""
        self.quality_score = max(1.0, min(5.0, score))
        return self.quality_score
