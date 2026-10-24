"""Тесты для логистики, заказов клиентов и отгрузки."""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plant.core.address import Address
from plant.core.contact_info import ContactInfo
from plant.core.dimension import Dimension
from plant.core.technical_specification import TechnicalSpecification
from plant.core.serial_number import SerialNumber
from plant.parts.auto_part import AutoPart
from plant.logistics.shipping_pallet import ShippingPallet
from plant.logistics.customer import Customer
from plant.logistics.customer_order import CustomerOrder
from plant.logistics.delivery_vehicle import DeliveryVehicle
from plant.logistics.dispatch_order import DispatchOrder
from plant.exceptions.storage_exhausted_exception import StorageExhaustedException

class TestLogisticsSuite(unittest.TestCase):
    """Тестирует отгрузку паллет, обработку заказов клиентов и транспортные накладные."""

    def setUp(self):
        self.ci = ContactInfo("purchasing@belgee.by", "+375-17-700-00-00", "Закупки")
        self.addr = Address("Беларусь", "Жодино", "ул. Заводская, 2", "222160")
        self.customer = Customer("КЛ-01", "СЗАО БелДжи", self.ci, self.addr)
        self.dim = Dimension(50.0, 50.0, 50.0)
        self.spec = TechnicalSpecification("СПЕЦ-10", "ISO", 600.0, 1.0)
        self.sn = SerialNumber("PLT", 2026, 1)
        self.part = AutoPart("ДЕТ-1", self.sn, "Поршень", self.dim, self.spec)

    def test_shipping_pallet(self):
        pallet = ShippingPallet("ПАЛЛЕТ-1", max_capacity_parts=2, max_weight_kg=50.0)
        self.assertTrue(pallet.load_part(self.part, 10.0))
        self.assertFalse(pallet.is_full())

        bad_part = AutoPart("ДЕТ-БРАК", self.sn, "Поршень с браком", self.dim, self.spec, is_defect_free=False)
        with self.assertRaises(ValueError):
            pallet.load_part(bad_part, 5.0)

        with self.assertRaises(StorageExhaustedException):
            pallet.load_part(self.part, 100.0)
        
        sn2 = SerialNumber("PLT", 2026, 2)
        part2 = AutoPart("ДЕТ-2", sn2, "Поршень", self.dim, self.spec)
        self.assertTrue(pallet.load_part(part2, 10.0))
        self.assertTrue(pallet.is_full())

        sn3 = SerialNumber("PLT", 2026, 3)
        part3 = AutoPart("ДЕТ-3", sn3, "Поршень", self.dim, self.spec)
        with self.assertRaises(StorageExhaustedException):
            pallet.load_part(part3, 10.0)

        unloaded = pallet.unload_all()
        self.assertEqual(len(unloaded), 2)
        self.assertEqual(pallet.current_weight_kg, 0.0)

    def test_customer_and_order(self):
        self.assertTrue(self.customer.is_major_automaker())
        small_customer = Customer("КЛ-02", "ИП Ремонт", self.ci, self.addr)
        self.assertFalse(small_customer.is_major_automaker())

        self.assertEqual(self.customer.apply_loyalty_discount(150000), 0.15)
        self.assertEqual(self.customer.apply_loyalty_discount(50000), 0.08)
        self.assertEqual(self.customer.apply_loyalty_discount(5000), 0.02)
        self.assertIn("БелДжи", self.customer.format_customer_card())

        order = CustomerOrder("ДОГОВОР-101", self.customer)
        order.add_part_order("Поршень ДВС", 1000, 25.0)
        self.assertEqual(order.total_price, 25000.0)
        with self.assertRaises(ValueError):
            order.add_part_order("Брак", -10, 10.0)
        with self.assertRaises(ValueError):
            order.add_part_order("Брак", 10, -5.0)

        final_price = order.calculate_final_price()
        self.assertEqual(final_price, round(25000.0 * 0.98, 2))
        order.dispatch()
        self.assertTrue(order.is_dispatched)

        empty_order = CustomerOrder("ДОГОВОР-ПУСТОЙ", self.customer)
        with self.assertRaises(RuntimeError):
            empty_order.dispatch()

    def test_delivery_vehicle_and_dispatch_order(self):
        truck = DeliveryVehicle("AI-7777-7", carrying_capacity_tons=20.0)
        with self.assertRaises(RuntimeError):
            truck.depart_for_delivery()

        self.assertTrue(truck.load_pallet(1.5))
        self.assertEqual(truck.pallets_count, 1)
        self.assertAlmostEqual(truck.get_load_factor(), 0.075, places=3)
        self.assertFalse(truck.load_pallet(25.0))
        depart_msg = truck.depart_for_delivery()
        self.assertIn("убыл в рейс", depart_msg)
        with self.assertRaises(RuntimeError):
            truck.load_pallet(1.0)

        truck_zero = DeliveryVehicle("AI-0000-0", carrying_capacity_tons=0.0)
        self.assertEqual(truck_zero.get_load_factor(), 1.0)

        truck.is_ready = True
        order = CustomerOrder("ДОГОВОР-102", self.customer)
        order.add_part_order("Амортизатор", 200, 40.0)
        dispatch = DispatchOrder("5001", order, truck, "2026-10-15")
        self.assertIn("ТТН №5001", dispatch.generate_waybill())
        cost = dispatch.calculate_transport_cost(distance_km=60.0, rate_per_km=2.0)
        self.assertEqual(cost, 120.0)
        with self.assertRaises(ValueError):
            dispatch.calculate_transport_cost(-10.0)
        dispatch.confirm_delivery()
        self.assertTrue(dispatch.is_delivered)
        self.assertEqual(truck.current_load_tons, 0.0)

if __name__ == "__main__":
    unittest.main()
