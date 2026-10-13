"""Тесты для материалов, складов и сырьевых партий."""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plant.core.address import Address
from plant.core.contact_info import ContactInfo
from plant.materials.raw_material import RawMaterial
from plant.materials.metal_sheet import MetalSheet
from plant.materials.alloy_ingot import AlloyIngot
from plant.materials.rubber_compound import RubberCompound
from plant.materials.plastic_pellet import PlasticPellet
from plant.materials.chemical_coolant import ChemicalCoolant
from plant.materials.material_batch import MaterialBatch
from plant.materials.storage_bin import StorageBin
from plant.materials.material_warehouse import MaterialWarehouse
from plant.materials.material_supplier import MaterialSupplier
from plant.exceptions.raw_material_shortage_exception import RawMaterialShortageException
from plant.exceptions.storage_exhausted_exception import StorageExhaustedException
from plant.exceptions.material_defect_exception import MaterialDefectException

class TestMaterialsSuite(unittest.TestCase):
    """Тестирует классы сырья, партий, складских ячеек и поставщиков."""

    def setUp(self):
        self.steel = RawMaterial("МАТ-СТ08", "Сталь 08Ю", 7.85, 1.20)
        self.aluminum = RawMaterial("МАТ-АЛ9", "Сплав АК9ч", 2.70, 3.50)

    def test_raw_material_calculations(self):
        mass = self.steel.estimate_mass_kg(1000.0)  # 1000 см³ * 7.85 г/см³ = 7850 г = 7.85 кг
        self.assertEqual(mass, 7.85)
        cost = self.steel.calculate_volume_cost(1000.0)
        self.assertEqual(cost, round(7.85 * 1.20, 2))

    def test_metal_sheet(self):
        sheet = MetalSheet("ЛИСТ-01", 1.2, "08Ю", False, self.steel)
        mass = sheet.calculate_sheet_mass(2.0)
        self.assertGreater(mass, 0)
        self.assertTrue(sheet.check_formability())
        sheet.apply_galvanizing()
        self.assertTrue(sheet.is_galvanized)

    def test_alloy_ingot(self):
        ingot = AlloyIngot("СЛИТОК-55", "Al-Si9-Cu3", 650.0, 15.0, self.aluminum)
        self.assertTrue(ingot.check_furnace_compatibility(750.0))
        self.assertFalse(ingot.check_furnace_compatibility(680.0))
        self.assertEqual(ingot.calculate_casting_yield(0.1), 13.5)

    def test_rubber_and_plastic(self):
        rubber = RubberCompound("РЕЗ-01", 65, 15.0)
        self.assertTrue(rubber.validate_hardness(68, tolerance=5))
        self.assertTrue(rubber.simulate_vulcanization(160.0))
        self.assertTrue(rubber.is_ready_for_assembly())

        plastic = PlasticPellet("ПЛ-10", "PA66-GF30", 12.0, 0.25)
        self.assertTrue(plastic.requires_drying(0.15))
        plastic.perform_drying(2.0)
        self.assertTrue(plastic.is_suitable_for_injection())

        bad_plastic = PlasticPellet("ПЛ-99", "PP", 10.0, 0.8)
        with self.assertRaises(MaterialDefectException):
            bad_plastic.is_suitable_for_injection()

    def test_chemical_coolant(self):
        coolant = ChemicalCoolant("СОЖ-01", 7.5, 9.2)
        self.assertTrue(coolant.is_within_ph_limits())
        coolant.dilute_with_water(50.0, 100.0)
        self.assertLess(coolant.concentration_pct, 7.5)
        coolant.replace_fluid()
        self.assertEqual(coolant.concentration_pct, 7.0)

    def test_material_batch_and_shortage(self):
        batch = MaterialBatch("ПАРТИЯ-01", self.steel, 500.0, "2026-10-10")
        batch.consume_material(200.0)
        self.assertEqual(batch.quantity_kg, 300.0)
        batch.approve_inspection()
        self.assertTrue(batch.is_inspected)
        with self.assertRaises(RawMaterialShortageException):
            batch.consume_material(500.0)

    def test_storage_bin_and_warehouse(self):
        bin_box = StorageBin("ЯЧ-A1", 1000.0)
        bin_box.deposit_material(400.0)
        self.assertEqual(bin_box.current_weight_kg, 400.0)
        self.assertEqual(bin_box.get_occupancy_ratio(), 0.4)
        bin_box.withdraw_material(150.0)
        self.assertEqual(bin_box.current_weight_kg, 250.0)

        with self.assertRaises(StorageExhaustedException):
            bin_box.deposit_material(900.0)

        locked_bin = StorageBin("ЯЧ-БЛОК", 500.0, is_locked=True)
        with self.assertRaises(RuntimeError):
            locked_bin.deposit_material(10.0)

        with self.assertRaises(ValueError):
            bin_box.deposit_material(-10.0)
        with self.assertRaises(ValueError):
            bin_box.withdraw_material(-5.0)
        with self.assertRaises(ValueError):
            bin_box.withdraw_material(10000.0)

        zero_bin = StorageBin("ЯЧ-НОЛЬ", 0.0)
        self.assertEqual(zero_bin.get_occupancy_ratio(), 1.0)

        addr = Address("РБ", "Минск", "Заводская, 1", "220000")
        wh = MaterialWarehouse("СКЛАД-01", addr, 50.0)
        wh.add_bin(bin_box)
        found = wh.find_available_bin(500.0)
        self.assertIsNotNone(found)
        self.assertEqual(wh.calculate_total_stored_weight(), 0.25)

    def test_material_supplier(self):
        contact = ContactInfo("sales@metal.by", "+375-29-111-22-33", "Сбыт")
        supplier = MaterialSupplier("ПОСТ-01", "БелМеталл", 4.5, contact)
        self.assertTrue(supplier.is_certified_vendor())
        new_rating = supplier.update_rating(3.0)
        self.assertGreater(new_rating, 0)
        claim = supplier.send_quality_claim("Брак в партии листов")
        self.assertIn("ПРЕТЕНЗИЯ", claim)

if __name__ == "__main__":
    unittest.main()
