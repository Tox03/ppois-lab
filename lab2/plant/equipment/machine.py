"""Базовое промышленное оборудование завода."""

from __future__ import annotations
from plant.exceptions.equipment_overheat_exception import EquipmentOverheatException
from plant.exceptions.machine_malfunction_exception import MachineMalfunctionException

class Machine:
    """Базовый класс технологического оборудования (станки, роботы, прессы)."""

    def __init__(
        self,
        machine_id: str,
        model: str,
        operating_hours: float,
        current_temperature: float,
        max_allowed_temp: float = 85.0,
        is_operational: bool = True
    ) -> None:
        # Уникальный инвентарный номер станка
        self.machine_id = machine_id
        # Марка и модель оборудования
        self.model = model
        # Суммарная наработка оборудования в часах
        self.operating_hours = operating_hours
        # Текущая температура подшипников/шпинделя в °C
        self.current_temperature = current_temperature
        # Максимально допустимая рабочая температура
        self.max_allowed_temp = max_allowed_temp
        # Статус работоспособности станка
        self.is_operational = is_operational

    def start(self) -> None:
        """Включает оборудование в производственный цикл."""
        if not self.is_operational:
            raise MachineMalfunctionException(self.machine_id, "Попытка запуска неисправного оборудования")
        self.check_overheat()

    def stop(self) -> None:
        """Останавливает рабочий цикл станка."""
        # Плавное охлаждение после остановки
        self.current_temperature = max(20.0, self.current_temperature - 15.0)

    def record_hours(self, hours: float) -> float:
        """Учитывает наработку станка в часах за смену."""
        if hours < 0:
            raise ValueError("Наработка не может быть отрицательной")
        self.operating_hours = round(self.operating_hours + hours, 2)
        return self.operating_hours

    def check_overheat(self) -> None:
        """
        Проверяет температурный режим.
        Выбрасывает EquipmentOverheatException при перегреве.
        """
        if self.current_temperature > self.max_allowed_temp:
            self.is_operational = False
            raise EquipmentOverheatException(self.machine_id, self.current_temperature, self.max_allowed_temp)

    def service(self, target_temperature: float = 25.0) -> None:
        """Проводит сервисное обслуживание станка, устраняет неисправности и охлаждает узел."""
        self.is_operational = True
        self.current_temperature = target_temperature
