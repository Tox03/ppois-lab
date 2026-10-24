"""Клиент автомобильного завода (автосборочный концерн или дилерская сеть)."""

from __future__ import annotations
from plant.core.contact_info import ContactInfo
from plant.core.address import Address

class Customer:
    """Описывает покупателя автокомпонентов: автозаводы (OEM), дистрибьюторов автозапчастей."""

    def __init__(
        self,
        customer_id: str,
        company_name: str,
        contact_info: ContactInfo,
        address: Address,
        discount_rate: float = 0.0
    ) -> None:
        # Регистрационный номер клиента
        self.customer_id = customer_id
        # Фирменное наименование клиента (например, БелДжи, АвтоВАЗ, КАМАЗ)
        self.company_name = company_name
        # Контактное лицо и канал связи (Ассоциация: ContactInfo)
        self.contact_info = contact_info
        # Юридический адрес контрагента (Ассоциация: Address)
        self.address = address
        # Персональная коммерческая скидка (от 0.0 до 0.3)
        self.discount_rate = discount_rate

    def apply_loyalty_discount(self, volume_bought_units: int) -> float:
        """Пересчитывает прогрессивную скидку в зависимости от годового объема закупок."""
        if volume_bought_units > 100000:
            self.discount_rate = 0.15
        elif volume_bought_units > 20000:
            self.discount_rate = 0.08
        else:
            self.discount_rate = 0.02
        return self.discount_rate

    def format_customer_card(self) -> str:
        """Формирует карточку клиента для CRM-системы коммерческого отдела."""
        return f"[{self.customer_id}] {self.company_name} | {self.address.city} | Скидка: {int(self.discount_rate * 100)}%"

    def is_major_automaker(self) -> bool:
        """Определяет стратегического заказчика первого уровня (Tier-1 OEM)."""
        oem_names = ["белджи", "автоваз", "камаз", "газ", "geely", "volkswagen", "toyota"]
        return any(oem in self.company_name.lower() for oem in oem_names)
