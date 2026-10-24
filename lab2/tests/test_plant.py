"""Интеграционные тесты для центрального класса AutomotivePlant."""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plant.automotive_plant import AutomotivePlant
from plant.core.address import Address
from plant.core.contact_info import ContactInfo
from plant.personnel.employee import Employee
from plant.personnel.plant_director import PlantDirector
from plant.personnel.machine_operator import MachineOperator
from plant.equipment.machine import Machine
from plant.materials.material_warehouse import MaterialWarehouse
from plant.production.production_line import ProductionLine
from plant.production.production_order import ProductionOrder
from plant.production.work_station import WorkStation

class TestAutomotivePlantSuite(unittest.TestCase):
    """Интеграционные тесты завода по производству автомобильных деталей."""

    def setUp(self):
        self.ci = ContactInfo("director@plant.by", "+375-17-999-99-99", "Дирекция")
        self.emp = Employee("ТН-001", "Иванов И.И.", "Генеральный директор", 10000.0, self.ci)
        self.director = PlantDirector(self.emp, 2000000.0, "План-2026")
        self.plant = AutomotivePlant("БелАвтоКомпонент", self.director)

    def test_plant_infrastructure(self):
        addr = Address("Беларусь", "Минск", "ул. Промышленная, 5", "220075")
        warehouse = MaterialWarehouse("СКЛАД-ГЛАВНЫЙ", addr, 500.0)
        self.plant.register_warehouse(warehouse)
        self.assertEqual(len(self.plant.warehouses), 1)

        m = Machine("СТК-01", "ПРЕСС", 10.0, 30.0)
        op_emp = Employee("ТН-101", "Петров П.", "Оператор", 2500.0, self.ci)
        operator = MachineOperator(op_emp, 5, safety_certified=True)
        station = WorkStation("СТ-01", m)
        station.assign_operator(operator)

        line = ProductionLine("ЛИНИЯ-ШТАМП", "Штамповочная линия")
        line.add_station(station)
        self.plant.add_production_line(line)
        self.assertEqual(len(self.plant.production_lines), 1)

        order = ProductionOrder("ЗАКАЗ-01", "Тормозной диск", 200)
        self.plant.receive_production_order(order)
        self.assertEqual(len(self.plant.active_orders), 1)

        units = self.plant.execute_daily_production()
        self.assertEqual(units, 10)
        self.assertEqual(self.plant.total_parts_produced, 10)

        self.plant.emergency_plant_shutdown("Учебная тревога")
        self.assertFalse(line.is_running)
        restored = self.plant.restart_production_lines()
        self.assertEqual(restored, 1)
        self.assertTrue(line.is_running)
        line.stop_line()

        # Тест удаления производственной линии
        self.assertTrue(self.plant.remove_production_line("ЛИНИЯ-ШТАМП"))
        self.assertEqual(len(self.plant.production_lines), 0)
        self.assertFalse(self.plant.remove_production_line("НЕИЗВЕСТНАЯ-ЛИНИЯ"))
        self.assertFalse(line.is_running)

if __name__ == "__main__":
    unittest.main()
