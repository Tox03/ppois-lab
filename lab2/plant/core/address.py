"""Юридический и физический адрес производственных и логистических объектов."""

from __future__ import annotations

class Address:
    """Хранит адресные реквизиты цехов завода, поставщиков сырья и дилерских центров."""

    def __init__(self, country: str, city: str, street: str, postal_code: str) -> None:
        # Страна расположения
        self.country = country
        # Город
        self.city = city
        # Улица, дом, корпус/строение
        self.street = street
        # Почтовый индекс
        self.postal_code = postal_code

    def format_full_address(self) -> str:
        """Возвращает единую форматированную строку адреса для накладных и путевых листов."""
        return f"{self.postal_code}, {self.country}, г. {self.city}, {self.street}"

    def is_domestic(self, base_country: str = "Беларусь") -> bool:
        """Определяет, является ли поставка/адрес внутренним относительно страны завода."""
        return self.country.strip().lower() == base_country.strip().lower()
