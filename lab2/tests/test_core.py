"""Тесты для базовых классов геометрии, ТУ и реквизитов."""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plant.core.dimension import Dimension
from plant.core.technical_specification import TechnicalSpecification
from plant.core.serial_number import SerialNumber
from plant.core.address import Address
from plant.core.contact_info import ContactInfo
from plant.exceptions.invalid_specification_exception import InvalidSpecificationException

class TestCoreEntitiesSuite(unittest.TestCase):
    """Тестирует геометрию, технические спецификации, маркировку и реквизиты."""

    def test_dimension_volume_and_tolerance(self):
        nominal = Dimension(100.0, 50.0, 20.0, tolerance_mm=0.1)
        self.assertEqual(nominal.calculate_volume_cm3(), 100.0)
        
        actual_good = Dimension(100.05, 49.95, 20.08, tolerance_mm=0.1)
        self.assertTrue(nominal.is_within_tolerance(actual_good))
        
        actual_bad = Dimension(100.25, 50.0, 20.0, tolerance_mm=0.1)
        self.assertFalse(nominal.is_within_tolerance(actual_bad))

    def test_dimension_scale(self):
        dim = Dimension(10.0, 20.0, 30.0)
        scaled = dim.scale(1.02)
        self.assertEqual(scaled.length_mm, 10.2)
        with self.assertRaises(ValueError):
            dim.scale(-1.0)

    def test_technical_specification(self):
        spec = TechnicalSpecification(
            spec_id="ТУ-101",
            standard_code="ISO-9001",
            required_tensile_strength_mpa=550.0,
            max_allowed_roughness_ra=1.6
        )
        self.assertTrue(spec.validate_roughness(1.2))
        self.assertFalse(spec.validate_roughness(2.5))
        self.assertTrue(spec.verify_strength(600.0))
        self.assertFalse(spec.verify_strength(500.0))
        spec.mark_as_critical("Ответственный узел рулевого управления")
        self.assertTrue(spec.is_critical)

        with self.assertRaises(InvalidSpecificationException):
            spec.validate_roughness(-0.5)
        with self.assertRaises(InvalidSpecificationException):
            spec.verify_strength(-10.0)

    def test_serial_number(self):
        sn = SerialNumber("PST", 2026, 42)
        code = sn.generate_code()
        self.assertEqual(code, "PST-2026-000042")
        self.assertTrue(sn.validate_format(code))
        self.assertFalse(sn.validate_format("BAD-CODE"))
        sn.deactivate()
        self.assertFalse(sn.is_active)

    def test_address_and_contacts(self):
        addr = Address("Беларусь", "Минск", "ул. Радиальная, 11", "220021")
        self.assertIn("220021", addr.format_full_address())
        self.assertTrue(addr.is_domestic("Беларусь"))
        self.assertFalse(addr.is_domestic("Германия"))

        contact = ContactInfo("qc@plant.by", "+375-17-200-11-22", "ОТК")
        self.assertTrue(contact.validate_contact())
        self.assertIn("ОТК", contact.format_vcard())

if __name__ == "__main__":
    unittest.main()
