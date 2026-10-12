"""Тесты для деталей автомобиля (поршни, диски, амортизаторы, валы и др.)."""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plant.core.dimension import Dimension
from plant.core.technical_specification import TechnicalSpecification
from plant.core.serial_number import SerialNumber
from plant.parts.auto_part import AutoPart
from plant.parts.engine_piston import EnginePiston
from plant.parts.brake_disc import BrakeDisc
from plant.parts.shock_absorber import ShockAbsorber
from plant.parts.gearbox_shaft import GearboxShaft
from plant.parts.fuel_injector import FuelInjector
from plant.parts.control_arm import ControlArm
from plant.parts.exhaust_manifold import ExhaustManifold
from plant.exceptions.quality_check_failed_exception import QualityCheckFailedException

class TestAutoPartsSuite(unittest.TestCase):
    """Тестирует классы автодеталей и их специфическую предметную логику."""

    def setUp(self):
        self.dim = Dimension(100.0, 100.0, 50.0, tolerance_mm=0.05)
        self.spec = TechnicalSpecification("ТУ-201", "ISO-16949", 600.0, 1.6)
        self.sn = SerialNumber("PRT", 2026, 1)
        self.base_part = AutoPart("2112-1004015", self.sn, "Базовая деталь", self.dim, self.spec)

    def test_auto_part_verification(self):
        good_meas = Dimension(100.02, 99.98, 50.01)
        self.assertTrue(self.base_part.verify_dimensions(good_meas))

        bad_meas = Dimension(100.20, 100.0, 50.0)
        with self.assertRaises(QualityCheckFailedException):
            self.base_part.verify_dimensions(bad_meas)
        self.assertFalse(self.base_part.is_defect_free)

    def test_engine_piston(self):
        piston = EnginePiston(self.base_part, piston_diameter_mm=82.46, compression_height_mm=38.3)
        clearance = piston.check_bore_clearance(82.50)
        self.assertAlmostEqual(clearance, 0.04, places=4)
        expansion = piston.calculate_thermal_expansion(100.0)
        self.assertGreater(expansion, 0)

    def test_brake_disc(self):
        disc = BrakeDisc(self.base_part, disc_thickness_mm=22.0, min_thickness_limit_mm=20.0)
        self.assertTrue(disc.check_wear_limit())
        self.assertTrue(disc.verify_axial_runout(max_allowed_microns=30.0))
        new_th = disc.simulate_braking_cycle(0.5)
        self.assertEqual(new_th, 21.5)

    def test_shock_absorber(self):
        shock = ShockAbsorber(self.base_part, damping_force_n=1500.0, stroke_length_mm=180.0, gas_pressure_bar=20.0)
        self.assertTrue(shock.is_leak_free())
        force = shock.test_damping_performance(1.0)
        self.assertEqual(force, 1500.0)
        shock.recharge_gas(25.0)
        self.assertEqual(shock.gas_pressure_bar, 25.0)

    def test_gearbox_shaft(self):
        shaft = GearboxShaft(self.base_part, gear_teeth_count=20, surface_hardness_hrc=61.0, spline_count=24)
        self.assertTrue(shaft.validate_hardness(58.0))
        ratio = shaft.calculate_gear_ratio(matching_gear_teeth=40)
        self.assertEqual(ratio, 2.0)
        self.assertTrue(shaft.verify_spline_mesh(24))

    def test_fuel_injector(self):
        inj = FuelInjector(self.base_part, flow_rate_cc_min=250.0, spray_angle_deg=22.0, operating_pressure_bar=200.0)
        self.assertTrue(inj.test_spray_pattern(0.95))
        delivery = inj.calculate_fuel_delivery(pulse_width_ms=2.5)
        self.assertGreater(delivery, 0)
        self.assertTrue(inj.is_high_pressure_gdi())

    def test_control_arm(self):
        arm = ControlArm(self.base_part, bushing_count=2, ball_joint_fitted=False, load_rating_kn=45.0)
        self.assertTrue(arm.test_structural_strength(30.0))
        arm.install_ball_joint()
        self.assertTrue(arm.is_complete_subassembly())

    def test_exhaust_manifold(self):
        man = ExhaustManifold(self.base_part, runner_count=4, max_operating_temp_c=950.0)
        self.assertTrue(man.perform_pressure_leak_test(2.5))
        self.assertTrue(man.verify_thermal_resistance(850.0))

if __name__ == "__main__":
    unittest.main()
