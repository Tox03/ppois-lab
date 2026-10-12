"""Контактные данные сотрудников и контрагентов завода."""

from __future__ import annotations

class ContactInfo:
    """Хранит электронные и телефонные каналы связи персонала и внешних партнеров."""

    def __init__(self, email: str, phone_number: str, department: str) -> None:
        # Корпоративная электронная почта
        self.email = email
        # Телефон внутренней или внешней связи
        self.phone_number = phone_number
        # Отдел или подразделение (например, ОТК, ОГТ, Цех №1)
        self.department = department

    def validate_contact(self) -> bool:
        """Выполняет проверку корректности формата email и длины телефонного номера."""
        has_at = "@" in self.email and "." in self.email
        has_valid_phone = len(self.phone_number.replace(" ", "").replace("-", "")) >= 7
        return has_at and has_valid_phone

    def format_vcard(self) -> str:
        """Формирует строковое представление визитной карточки подразделения."""
        return f"Отдел: {self.department} | Тел: {self.phone_number} | Email: {self.email}"
