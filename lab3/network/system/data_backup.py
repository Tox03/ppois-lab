# -*- coding: utf-8 -*-
"""Модуль резервного копирования данных."""


class DataBackup:
    """Управляет созданием и проверкой целостности бэкапов социальной сети."""

    def __init__(
        self,
        backup_id: str,
        file_path: str,
        size_mb: float = 0.0,
        status: str = "created",
        is_encrypted: bool = True,
        checksum: str = "sha256_mock_sum",
    ) -> None:
        """Инициализация архива резервной копии."""
        self.backup_id = backup_id
        self.file_path = file_path
        self.size_mb = size_mb
        self.status = status
        self.is_encrypted = is_encrypted
        self.checksum = checksum

    def create_snapshot(self, data_size_mb: float) -> str:
        """Формирует снимок данных и фиксирует его размер."""
        self.size_mb = round(data_size_mb, 2)
        self.status = "completed"
        return self.status

    def verify_checksum(self, expected_hash: str) -> bool:
        """Сверяет контрольную сумму снапшота для подтверждения целостности."""
        return self.checksum == expected_hash

    def mark_corrupted(self) -> None:
        """Помечает резервную копию как поврежденную."""
        self.status = "corrupted"

    def restore_snapshot(self) -> str:
        """Восстанавливает статус резервной копии как готовой к использованию."""
        self.status = "restored"
        return self.status
