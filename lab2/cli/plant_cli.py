"""Интерактивный консольный интерфейс (CLI) завода по изготовлению автомобильных деталей."""

from __future__ import annotations
from typing import Optional

from plant.automotive_plant import AutomotivePlant
from plant.core.address import Address
from plant.core.contact_info import ContactInfo
from plant.core.dimension import Dimension
from plant.core.technical_specification import TechnicalSpecification
from plant.core.serial_number import SerialNumber
from plant.materials.raw_material import RawMaterial
from plant.materials.material_batch import MaterialBatch
from plant.materials.storage_bin import StorageBin
from plant.materials.material_warehouse import MaterialWarehouse
from plant.equipment.machine import Machine
from plant.equipment.cutting_tool import CuttingTool
from plant.equipment.cnc_milling_machine import CncMillingMachine
from plant.personnel.employee import Employee
from plant.personnel.plant_director import PlantDirector
from plant.personnel.machine_operator import MachineOperator
from plant.personnel.quality_inspector import QualityInspector
from plant.production.work_station import WorkStation
from plant.production.production_line import ProductionLine
from plant.production.production_plan import ProductionPlan
from plant.production.production_order import ProductionOrder
from plant.parts.auto_part import AutoPart
from plant.parts.engine_piston import EnginePiston
from plant.quality.inspection_report import InspectionReport
from plant.logistics.customer import Customer
from plant.logistics.customer_order import CustomerOrder
from plant.logistics.delivery_vehicle import DeliveryVehicle
from plant.logistics.dispatch_order import DispatchOrder
from plant.exceptions.plant_base_exception import PlantBaseException

class PlantCli:
    """Консольное меню для демонстрации сценариев работы автомобильного завода."""

    def __init__(self) -> None:
        self._init_plant_and_storage()
        self._init_equipment_and_lines()
        self._init_partners_and_logistics()

    def _init_plant_and_storage(self) -> None:
        """Инициализирует дирекцию, склад и запасы сырья."""
        director_contact = ContactInfo("director@autoplant.by", "+375-17-299-00-01", "Дирекция")
        director_emp = Employee("EMP-001", "Ковалев Алексей Сергеевич", "Генеральный директор", 12000.0, director_contact)
        self.director = PlantDirector(director_emp, annual_budget=5000000.0, strategic_plan_name="Стратегия-2026")
        self.plant = AutomotivePlant("Минский завод автокомпонентов", self.director)

        wh_addr = Address("Беларусь", "Минск", "Партизанский пр-т, 8", "220033")
        self.warehouse = MaterialWarehouse("СКЛАД-01", wh_addr, total_capacity_tons=500.0)
        self.bin_a1 = StorageBin("A-01", max_weight_capacity_kg=2000.0)
        self.warehouse.add_bin(self.bin_a1)
        self.plant.register_warehouse(self.warehouse)

        self.raw_steel = RawMaterial("МАТ-СТ08", "Сталь 08Ю", density_g_cm3=7.85, base_cost_per_kg=1.45)
        self.steel_batch = MaterialBatch("ПАРТИЯ-СТ-100", self.raw_steel, quantity_kg=1500.0, received_date="2026-10-10")
        self.bin_a1.deposit_material(1500.0)

    def _init_equipment_and_lines(self) -> None:
        """Инициализирует станочный парк, оператора и производственную линию."""
        self.machine_cnc = Machine("ЧПУ-01", "HAAS-VF3", operating_hours=250.0, current_temperature=32.0, max_allowed_temp=80.0)
        self.cutter = CuttingTool("ФРЕЗА-D20", "Твердосплав ВК8", flank_wear_mm=0.05, max_wear_limit_mm=0.3)
        self.cnc_station = CncMillingMachine(axis_count=4, spindle_rpm=6000, machine=self.machine_cnc, active_tool=self.cutter)

        op_contact = ContactInfo("operator1@autoplant.by", "+375-29-111-22-33", "Цех мехобработки")
        op_emp = Employee("EMP-102", "Смирнов Денис Викторович", "Оператор станков с ЧПУ", 2600.0, op_contact)
        self.operator = MachineOperator(op_emp, qualification_rank=5, safety_certified=True)

        self.work_station = WorkStation("СТ-01", self.machine_cnc)
        self.work_station.assign_operator(self.operator)

        self.prod_line = ProductionLine("ЛИНИЯ-ПОРШНЕЙ", "Линия обработки поршней", max_allowed_scrap_pct=3.0)
        self.prod_line.add_station(self.work_station)
        self.plant.add_production_line(self.prod_line)

    def _init_partners_and_logistics(self) -> None:
        """Инициализирует отдел ОТК, автотранспорт и заказчика."""
        qc_contact = ContactInfo("qc@autoplant.by", "+375-17-299-00-55", "ОТК")
        qc_emp = Employee("EMP-201", "Морозов Игорь Владимирович", "Ведущий контролер ОТК", 2400.0, qc_contact)
        self.inspector = QualityInspector(qc_emp, inspector_badge_id="ОТК-42")

        cust_contact = ContactInfo("supply@belgee.by", "+375-17-700-11-22", "Отдел закупок")
        cust_addr = Address("Беларусь", "Жодино", "ул. Заводская, 2", "222160")
        self.customer = Customer("CUST-BELGEE", "СЗАО БелДжи", cust_contact, cust_addr)
        self.truck = DeliveryVehicle("AI-9090-7", carrying_capacity_tons=20.0)

    def print_menu(self) -> None:
        """Отображает главное консольное меню."""
        print("\n" + "=" * 65)
        print(f"   СИСТЕМА УПРАВЛЕНИЯ ПРЕДПРИЯТИЕМ: {self.plant.plant_name}")
        print("=" * 65)
        print("1. Запуск суточного производственного цикла линии")
        print("2. Создание и запуск наряда-заказа на производство деталей")
        print("3. Входной контроль сырья и списание в производство")
        print("4. Проведение приемочного контроля качества партии деталей (ОТК)")
        print("5. Оформление коммерческого заказа и отгрузка клиенту (ТТН)")
        print("6. Симуляция аварийной ситуации и остановки линии")
        print("7. Вывод сводного паспорта предприятия и складских остатков")
        print("0. Выход")
        print("=" * 65)

    def action_daily_production(self) -> None:
        """Сценарий запуска суточного производства."""
        print("\n--- [1] Запуск суточного производства ---")
        produced = self.plant.execute_daily_production()
        print(f"Линия '{self.prod_line.line_name}' запущена.")
        print(f"Выпущено за смену: {produced} шт. автодеталей.")
        print(f"Всего выпущено за историю завода: {self.plant.total_parts_produced} шт.")

    def action_create_order(self) -> None:
        """Сценарий создания производственного заказа."""
        print("\n--- [2] Оформление наряда-заказа ---")
        order_id = f"НАРЯД-{len(self.plant.active_orders) + 1:03d}"
        plan = ProductionPlan(f"ПЛАН-{order_id}", planned_quantity=500, deadline_date="2026-10-30")
        order = ProductionOrder(order_id, target_part_type="Поршень ДВС 2112", quantity=500, production_plan=plan)
        order.start_production(max_capacity=2000)
        self.plant.receive_production_order(order)
        print(f"Сформирован производственный заказ: {order.order_id}")
        print(f"Номенклатура: {order.target_part_type}, Партия: {order.quantity} шт.")
        print(f"Статус заказа: {order.status}")

    def action_material_consumption(self) -> None:
        """Сценарий списания сырья со склада."""
        print("\n--- [3] Расход материалов со склада ---")
        print(f"Текущий остаток партии {self.steel_batch.batch_id}: {self.steel_batch.quantity_kg} кг")
        consume_qty = 120.0
        remaining = self.steel_batch.consume_material(consume_qty)
        self.bin_a1.withdraw_material(consume_qty)
        print(f"Списано на штамповку: {consume_qty} кг стали '{self.raw_steel.name}'.")
        print(f"Остаток в ячейке {self.bin_a1.bin_code}: {remaining} кг.")

    def action_quality_inspection(self) -> None:
        """Сценарий проверки качества и приемки партии."""
        print("\n--- [4] Контроль качества ОТК ---")
        dim = Dimension(82.46, 82.46, 68.0, tolerance_mm=0.03)
        spec = TechnicalSpecification("ТУ-ПОРШЕНЬ-01", "IATF 16949", required_tensile_strength_mpa=450.0, max_allowed_roughness_ra=1.2)
        sn = SerialNumber("PST", 2026, 101)
        part = AutoPart("2112-1004015", sn, "Поршень ДВС", dim, spec)
        piston = EnginePiston(part, piston_diameter_mm=82.46, compression_height_mm=38.3)

        verdict = self.inspector.inspect_part(is_ok=part.is_defect_free)
        print(f"Проверена деталь: {part.get_part_label()} (D={piston.piston_diameter_mm} мм)")
        print(f"Вердикт контролера {self.inspector.inspector_badge_id}: {verdict}")

        report = InspectionReport("АКТ-ОТК-55", "ПАРТИЯ-100", self.inspector, passed_items=495, rejected_items=5)
        print(report.sign_report())

    def action_dispatch_customer_order(self) -> None:
        """Сценарий формирования отгрузки заказчику."""
        print("\n--- [5] Коммерческая отгрузка клиенту ---")
        order = CustomerOrder("ДОГОВОР-BELGEE-2026", self.customer)
        order.add_part_order("Поршень ДВС в сборе", quantity=400, unit_price=45.0)
        self.customer.apply_loyalty_discount(volume_bought_units=50000)
        final_sum = order.calculate_final_price()
        order.dispatch()

        self.truck.load_pallet(pallet_weight_tons=1.2)
        dispatch = DispatchOrder("ТТН-9901", order, self.truck, departure_date="2026-10-12")
        print(dispatch.generate_waybill())
        cost = dispatch.calculate_transport_cost(distance_km=75.0, rate_per_km=2.2)
        print(f"Сумма контракта с учетом скидки: {final_sum:.2f} у.е.")
        print(f"Транспортные расходы на доставку: {cost:.2f} у.е.")

    def action_simulate_emergency(self) -> None:
        """Сценарий симуляции аварийного останова оборудования."""
        print("\n--- [6] Симуляция нештатной ситуации ---")
        try:
            print("Симуляция: аварийный перегрев подшипникового узла...")
            self.machine_cnc.current_temperature = 95.0
            self.machine_cnc.check_overheat()
        except PlantBaseException as err:
            print(f"Сработала система безопасности: {err.get_details()}")
            self.plant.emergency_plant_shutdown("Авария станка ЧПУ-01")
            print("Производственные линии переведены в безопасный останов.")

    def action_show_plant_status(self) -> None:
        """Сценарий вывода сводного статуса предприятия."""
        print("\n--- [7] Сводный отчет о состоянии завода ---")
        print(f"Предприятие: {self.plant.plant_name}")
        print(f"Директор: {self.director.employee.full_name}")
        print(f"Остаток бюджета развития: {self.director.annual_budget:,.2f} у.е.")
        print(f"Складских комплексов: {len(self.plant.warehouses)}")
        print(f"Хранится сырья: {self.warehouse.calculate_total_stored_weight()} т")
        print(f"Действующих линий: {len(self.plant.production_lines)}")
        print(f"Всего произведено деталей: {self.plant.total_parts_produced} шт.")
        print(f"Активных нарядов в производстве: {len(self.plant.active_orders)}")

    def _execute_command(self, choice: str) -> bool:
        """Выполняет выбранную команду меню. Возвращает False для завершения работы."""
        actions = {
            "1": self.action_daily_production,
            "2": self.action_create_order,
            "3": self.action_material_consumption,
            "4": self.action_quality_inspection,
            "5": self.action_dispatch_customer_order,
            "6": self.action_simulate_emergency,
            "7": self.action_show_plant_status,
        }
        if choice == "0":
            print("\nРабота с системой завода завершена. До свидания!")
            return False
        action = actions.get(choice)
        if action is not None:
            action()
        else:
            print("\nНекорректный пункт меню. Попробуйте снова.")
        return True

    def run(self, auto_input: Optional[list] = None) -> None:
        """Основной цикл обработки команд интерфейса."""
        input_gen = iter(auto_input) if auto_input is not None else None
        while True:
            self.print_menu()
            try:
                choice = next(input_gen) if input_gen else input("Выберите пункт меню (0-7): ").strip()
            except (EOFError, StopIteration):
                break
            if not self._execute_command(choice):
                break
