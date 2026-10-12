"""Главная управляющая система завода по изготовлению автомобильных деталей."""

from __future__ import annotations
from typing import List
from plant.personnel.plant_director import PlantDirector
from plant.materials.material_warehouse import MaterialWarehouse
from plant.production.production_line import ProductionLine
from plant.production.production_order import ProductionOrder

class AutomotivePlant:
    """Центральный управляющий класс производственного комплекса автокомпонентов."""

    def __init__(
        self,
        plant_name: str,
        director: PlantDirector
    ) -> None:
        # Полное наименование завода
        self.plant_name = plant_name
        # Генеральный директор завода (Ассоциация: PlantDirector)
        self.director = director
        # Склады сырья и комплектующих (Ассоциация: коллекция MaterialWarehouse)
        self.warehouses: List[MaterialWarehouse] = []
        # Действующие производственные линии (Ассоциация: коллекция ProductionLine)
        self.production_lines: List[ProductionLine] = []
        # Активные производственные заказы (Ассоциация: коллекция ProductionOrder)
        self.active_orders: List[ProductionOrder] = []
        # Суммарное количество выпущенных готовых автокомпонентов
        self.total_parts_produced: int = 0

    def register_warehouse(self, warehouse: MaterialWarehouse) -> None:
        """Регистрирует новый складской комплекс в инфраструктуре завода."""
        self.warehouses.append(warehouse)

    def add_production_line(self, line: ProductionLine) -> None:
        """Вводит в строй новую производственную линию цеха."""
        self.production_lines.append(line)

    def receive_production_order(self, order: ProductionOrder) -> None:
        """Принимает заказ в производственный портфель завода."""
        self.active_orders.append(order)

    def execute_daily_production(self) -> int:
        """Запускает суточный производственный цикл по всем линиям и заказам."""
        daily_units = 0
        for line in self.production_lines:
            if line.start_line():
                for station in line.stations:
                    if station.process_part_cycle():
                        daily_units += 10
        self.total_parts_produced += daily_units
        return daily_units

    def emergency_plant_shutdown(self, reason: str) -> None:
        """Производит экстренную остановку всех производственных линий предприятия при аварии."""
        for line in self.production_lines:
            try:
                line.emergency_halt(reason)
            except Exception:
                pass
