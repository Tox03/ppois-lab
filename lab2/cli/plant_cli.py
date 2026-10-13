"""Интерактивный консольный интерфейс (CLI) завода по изготовлению автомобильных деталей."""

from __future__ import annotations
from typing import Optional, List, Iterator

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
    """Консольное меню для интерактивного управления и сценариев автомобильного завода."""

    def __init__(self) -> None:
        self._input_gen: Optional[Iterator[str]] = None
        self.active_dispatches: List[DispatchOrder] = []
        self._init_plant_and_storage()
        self._init_equipment_and_lines()
        self._init_partners_and_logistics()

    def _init_plant_and_storage(self) -> None:
        """Инициализирует дирекцию, склад, запасы сырья и начальные наряды."""
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

        # Начальный активный производственный наряд
        init_plan = ProductionPlan("ПЛАН-001", planned_quantity=300, deadline_date="2026-10-25")
        init_order = ProductionOrder("НАРЯД-001", target_part_type="Поршень ДВС 2112", quantity=300, production_plan=init_plan)
        init_order.start_production(max_capacity=5000)
        self.plant.receive_production_order(init_order)

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

        # Начальный активный заказ и накладная
        init_order = CustomerOrder("ДОГОВОР-BELGEE-2026", self.customer)
        init_order.add_part_order("Поршень ДВС в сборе", quantity=200, unit_price=45.0)
        init_order.dispatch()
        init_dispatch = DispatchOrder("ТТН-9901", init_order, self.truck, departure_date="2026-10-12")
        self.active_dispatches.append(init_dispatch)

    def _prompt(self, message: str, default: str = "") -> str:
        """Запрашивает строковый ввод пользователя с поддержкой значения по умолчанию."""
        prompt_str = f"{message} [{default}]: " if default else f"{message}: "
        if self._input_gen is not None:
            try:
                val = next(self._input_gen)
                val_str = str(val).strip()
                return val_str if val_str else default
            except StopIteration:
                return default
        try:
            val = input(prompt_str).strip()
            return val if val else default
        except (EOFError, KeyboardInterrupt):
            return default

    def _prompt_int(self, message: str, default: int) -> int:
        """Запрашивает целочисленное значение с валидацией."""
        raw = self._prompt(message, str(default))
        try:
            return int(raw)
        except ValueError:
            print(f"Предупреждение: некорректное число '{raw}', применено значение по умолчанию {default}.")
            return default

    def _prompt_float(self, message: str, default: float) -> float:
        """Запрашивает вещественное значение с валидацией."""
        raw = self._prompt(message, str(default))
        try:
            return float(raw)
        except ValueError:
            print(f"Предупреждение: некорректное число '{raw}', применено значение по умолчанию {default}.")
            return default

    def print_menu(self) -> None:
        """Отображает главное интерактивное меню."""
        print("\n" + "=" * 70)
        print(f"   СИСТЕМА УПРАВЛЕНИЯ ПРЕДПРИЯТИЕМ: {self.plant.plant_name}")
        print("=" * 70)
        print(" 1. Запуск суточного производственного цикла линии")
        print(" 2. Создание наряда-заказа на производство деталей")
        print(" 3. Сдать (завершить) наряд-заказ на производство")
        print(" 4. Пополнение и списание сырья со склада (обновление остатков)")
        print(" 5. Оформление коммерческого заказа и отгрузка клиенту (ТТН)")
        print(" 6. Сдать заказ клиенту (подтверждение доставки и акт приемки)")
        print(" 7. Обновление параметров оборудования и обслуживание (ЧПУ/ТО)")
        print(" 8. Обновление данных персонала и бюджета предприятия")
        print(" 9. Контроль качества ОТК (проверка детали и акт)")
        print("10. Симуляция нештатной ситуации (аварийный останов линии)")
        print("11. Сводный паспорт предприятия и состояние всех заказов")
        print(" 0. Выход")
        print("=" * 70)

    def action_daily_production(self) -> None:
        """Запуск производственного цикла линии с выбором количества смен."""
        print("\n--- [1] Запуск суточного производства ---")
        shifts = self._prompt_int("Количество рабочих смен для запуска", 1)
        total_cycle = 0
        for _ in range(max(1, shifts)):
            total_cycle += self.plant.execute_daily_production()
        print(f"Линия '{self.prod_line.line_name}' отработала {shifts} см.")
        print(f"Выпущено за цикл: {total_cycle} шт. автодеталей.")
        print(f"Всего произведено предприятием: {self.plant.total_parts_produced} шт.")

    def action_create_order(self) -> None:
        """Оформление нового производственного наряда-заказа с пользовательскими параметрами."""
        print("\n--- [2] Оформление наряда-заказа ---")
        order_num = len(self.plant.active_orders) + 1
        default_id = f"НАРЯД-{order_num:03d}"
        order_id = self._prompt("Номер наряда-заказа", default_id)
        part_name = self._prompt("Наименование автодетали", "Поршень ДВС 2112")
        qty = self._prompt_int("Количество деталей в партии (шт.)", 500)
        deadline = self._prompt("Плановый срок исполнения (ГГГГ-ММ-ДД)", "2026-10-30")

        try:
            plan = ProductionPlan(f"ПЛАН-{order_id}", planned_quantity=qty, deadline_date=deadline)
            order = ProductionOrder(order_id, target_part_type=part_name, quantity=qty, production_plan=plan)
            order.start_production(max_capacity=50000)
            self.plant.receive_production_order(order)
            print(f"УСПЕХ: Наряд-заказ {order.order_id} сформирован и запущен в производство.")
            print(f"Деталь: {order.target_part_type}, Партия: {order.quantity} шт., Срок: {deadline}")
            print(f"Статус: {order.status}")
        except Exception as err:
            print(f"Ошибка при создании наряда: {err}")

    def action_complete_order(self) -> None:
        """Сдача выполненного производственного наряда-заказа на склад готовой продукции."""
        print("\n--- [3] Сдача / завершение наряда-заказа ---")
        if not self.plant.active_orders:
            print("Нет зарегистрированных производственных нарядов.")
            return

        print("Список нарядов-заказов завода:")
        for idx, order in enumerate(self.plant.active_orders, start=1):
            print(f"  [{idx}] {order.order_id} | {order.target_part_type} | {order.quantity} шт. | Статус: {order.status}")

        choice_idx_str = self._prompt("Выберите номер наряда для сдачи", "1")
        try:
            choice_idx = int(choice_idx_str) - 1
            if choice_idx < 0 or choice_idx >= len(self.plant.active_orders):
                print("Указан некорректный номер наряда.")
                return
            target_order = self.plant.active_orders[choice_idx]
            if target_order.status == "ВЫПОЛНЕН":
                print(f"Наряд {target_order.order_id} уже был сдан ранее.")
                return
            if target_order.status != "В_ПРОИЗВОДСТВЕ":
                target_order.start_production()
            target_order.complete_order()
            print(f"УСПЕХ: Наряд-заказ {target_order.order_id} успешно сдан!")
            print(f"Продукция ({target_order.quantity} шт. '{target_order.target_part_type}') передана в отдел сбыта.")
        except Exception as err:
            print(f"Ошибка при сдаче наряда: {err}")

    def action_warehouse_management(self) -> None:
        """Пополнение или списание сырья со склада (обновление данных складских остатков)."""
        print("\n--- [4] Управление и обновление остатков склада ---")
        pct = self.bin_a1.get_occupancy_ratio() * 100.0
        bin_weight_str = f"{self.bin_a1.current_weight_kg:.1f} / {self.bin_a1.max_weight_capacity_kg:.1f} кг"
        print(f"Ячейка {self.bin_a1.bin_code}: остаток {bin_weight_str} ({pct:.1f}%)")
        print(f"Партия сырья {self.steel_batch.batch_id} ({self.raw_steel.name}): доступно {self.steel_batch.quantity_kg:.1f} кг")
        print("Операции: 1 - Пополнить склад сырьем (приемка), 2 - Списать сырье в цех")
        op_choice = self._prompt("Выберите операцию", "1")
        if op_choice == "1":
            qty = self._prompt_float("Масса сырья для пополнения (кг)", 250.0)
            try:
                self.bin_a1.deposit_material(qty)
                self.steel_batch.quantity_kg = round(self.steel_batch.quantity_kg + qty, 2)
                print(f"УСПЕХ: Данные склада обновлены! Загружено {qty:.1f} кг.")
                print(f"Текущий остаток в ячейке {self.bin_a1.bin_code}: {self.bin_a1.current_weight_kg:.1f} кг.")
            except Exception as err:
                print(f"Ошибка при пополнении склада: {err}")
        elif op_choice == "2":
            qty = self._prompt_float("Масса сырья для списания (кг)", 120.0)
            try:
                self.bin_a1.withdraw_material(qty)
                self.steel_batch.consume_material(qty)
                print(f"УСПЕХ: Сырье списано! Отгружено в цех {qty:.1f} кг.")
                print(f"Остаток в ячейке {self.bin_a1.bin_code}: {self.bin_a1.current_weight_kg:.1f} кг.")
            except Exception as err:
                print(f"Ошибка при списании сырья: {err}")
        else:
            print("Неизвестная операция со складом.")

    def action_dispatch_customer_order(self) -> None:
        """Оформление коммерческого контракта и отгрузка партии автодеталей (ТТН)."""
        print("\n--- [5] Оформление коммерческого заказа и отгрузка (ТТН) ---")
        client_order_id = self._prompt("Номер контракта / заказа", f"ДОГОВОР-{len(self.active_dispatches) + 1:03d}")
        part_name = self._prompt("Наименование автодетали для поставки", "Поршень ДВС в сборе")
        qty = self._prompt_int("Объем поставки (шт.)", 400)
        unit_price = self._prompt_float("Цена за единицу (у.е.)", 45.0)

        try:
            order = CustomerOrder(client_order_id, self.customer)
            order.add_part_order(part_name, quantity=qty, unit_price=unit_price)
            self.customer.apply_loyalty_discount(volume_bought_units=50000)
            final_sum = order.calculate_final_price()
            order.dispatch()

            self.truck.load_pallet(pallet_weight_tons=round(qty * 0.003, 2))
            disp_id = f"ТТН-{len(self.active_dispatches) + 9901:04d}"
            dispatch = DispatchOrder(disp_id, order, self.truck, departure_date="2026-10-13")
            self.active_dispatches.append(dispatch)

            print(dispatch.generate_waybill())
            cost = dispatch.calculate_transport_cost(distance_km=75.0, rate_per_km=2.2)
            print(f"УСПЕХ: Отгрузка оформлена! Сумма контракта со скидкой: {final_sum:,.2f} у.е.")
            print(f"Расчетные транспортные затраты: {cost:,.2f} у.е.")
            print(f"Номер ТТН для сдачи груза клиенту: {dispatch.dispatch_id}")
        except Exception as err:
            print(f"Ошибка при оформлении отгрузки: {err}")

    def action_confirm_delivery(self) -> None:
        """Подтверждение вручения и сдача коммерческого заказа автосборочному предприятию."""
        print("\n--- [6] Сдача заказа клиенту (подтверждение доставки) ---")
        if not self.active_dispatches:
            print("Нет оформленных товарно-транспортных накладных (ТТН).")
            return

        print("Список рейсов и ТТН завода:")
        for idx, disp in enumerate(self.active_dispatches, start=1):
            status = "ВРУЧЕН (СДАН)" if disp.is_delivered else "В ПУТИ (ОЖИДАЕТ СДАЧИ)"
            client = disp.customer_order.customer.company_name
            print(f"  [{idx}] {disp.dispatch_id} | Клиент: {client} | Авто: {disp.delivery_vehicle.vehicle_plate} | {status}")

        choice_idx_str = self._prompt("Выберите номер ТТН для сдачи заказчику", "1")
        try:
            choice_idx = int(choice_idx_str) - 1
            if choice_idx < 0 or choice_idx >= len(self.active_dispatches):
                print("Указан некорректный номер ТТН.")
                return
            target_disp = self.active_dispatches[choice_idx]
            if target_disp.is_delivered:
                print(f"Груз по накладной {target_disp.dispatch_id} уже сдан клиенту ранее.")
                return
            target_disp.confirm_delivery()
            print(f"УСПЕХ: Груз по накладной {target_disp.dispatch_id} успешно сдан заказчику '{target_disp.customer_order.customer.company_name}'!")
            print(f"Акт приема-передачи подписан. Автомобиль {target_disp.delivery_vehicle.vehicle_plate} разгружен и готов к рейсу.")
        except Exception as err:
            print(f"Ошибка при подтверждении сдачи заказа: {err}")

    def action_update_equipment(self) -> None:
        """Обновление технологических параметров станков и инструментов."""
        print("\n--- [7] Обновление параметров оборудования и обслуживание ---")
        temp_str = f"Скорость: {self.cnc_station.spindle_rpm} об/мин | Темп: {self.machine_cnc.current_temperature:.1f}°C"
        print(f"ЧПУ: {self.machine_cnc.machine_id} ({self.machine_cnc.model}) | {temp_str}")
        wear_str = f"Износ: {self.cutter.flank_wear_mm:.3f} мм (лимит {self.cutter.max_wear_limit_mm} мм) | Острый: {self.cutter.is_usable()}"
        print(f"Инструмент: {self.cutter.tool_id} | {wear_str}")
        print("Операции: 1 - Задать обороты шпинделя ЧПУ, 2 - Провести ТО/охлаждение станка, 3 - Переточить инструмент")
        sub_choice = self._prompt("Выберите операцию", "1")
        if sub_choice == "1":
            new_rpm = self._prompt_int("Новая частота вращения шпинделя (об/мин)", 7200)
            try:
                self.cnc_station.set_spindle_speed(new_rpm)
                print(f"УСПЕХ: Параметры ЧПУ обновлены! Установлены обороты: {self.cnc_station.spindle_rpm} об/мин.")
            except Exception as err:
                print(f"Ошибка обновления скорости: {err}")
        elif sub_choice == "2":
            self.machine_cnc.stop()
            self.machine_cnc.current_temperature = 25.0
            self.machine_cnc.is_operational = True
            print(f"УСПЕХ: Техническое обслуживание завершено. Станок {self.machine_cnc.machine_id} охлажден до 25.0°C и готов к работе.")
        elif sub_choice == "3":
            self.cutter.regrind()
            print(f"УСПЕХ: Инструмент {self.cutter.tool_id} переточен! Износ: {self.cutter.flank_wear_mm} мм, лезвие острое.")
        else:
            print("Неизвестная операция с оборудованием.")

    def action_update_personnel_and_budget(self) -> None:
        """Обновление данных сотрудников, окладов и бюджета завода."""
        print("\n--- [8] Обновление данных персонала и бюджета предприятия ---")
        print(f"Директор: {self.director.employee.full_name} | Бюджет: {self.director.annual_budget:,.2f} у.е.")
        emp = self.operator.employee
        print(f"Оператор: {emp.full_name} | Должность: {emp.position} | Оклад: {emp.salary:,.2f} у.е. | Разряд: {self.operator.qualification_rank}")
        print("Операции: 1 - Пополнить бюджет завода, 2 - Повысить сотрудника / оклад, 3 - Изменить квалификационный разряд")
        sub_choice = self._prompt("Выберите операцию", "1")
        if sub_choice == "1":
            add_budget = self._prompt_float("Сумма пополнения бюджета (у.е.)", 500000.0)
            self.director.annual_budget = round(self.director.annual_budget + add_budget, 2)
            print(f"УСПЕХ: Бюджет обновлен! Текущий годовой фонд: {self.director.annual_budget:,.2f} у.е.")
        elif sub_choice == "2":
            new_pos = self._prompt("Новая должность сотрудника", "Ведущий наладчик ЧПУ")
            raise_pct = self._prompt_float("Процент индексации оклада (%)", 15.0)
            try:
                self.operator.employee.promote(new_pos, raise_pct)
                msg = f"УСПЕХ: Сотрудник обновлен! Должность: {emp.position}, оклад: {emp.salary:,.2f} у.е."
                print(msg)
            except Exception as err:
                print(f"Ошибка обновления данных сотрудника: {err}")
        elif sub_choice == "3":
            new_rank = self._prompt_int("Новый квалификационный разряд оператора (1-6)", 6)
            self.operator.qualification_rank = new_rank
            print(f"УСПЕХ: Квалификационный разряд обновлен! Текущий разряд: {self.operator.qualification_rank}.")
        else:
            print("Неизвестная операция обновления.")

    def action_quality_inspection(self) -> None:
        """Сценарий проверки качества и приемки партии деталей (ОТК)."""
        print("\n--- [9] Контроль качества ОТК ---")
        nominal = 82.46
        tol = 0.03
        dia = self._prompt_float(f"Измеренный диаметр поршня в мм (номинал {nominal}±{tol})", nominal)
        dim = Dimension(dia, dia, 68.0, tolerance_mm=tol)
        spec = TechnicalSpecification("ТУ-ПОРШЕНЬ-01", "IATF 16949", required_tensile_strength_mpa=450.0, max_allowed_roughness_ra=1.2)
        sn = SerialNumber("PST", 2026, len(self.plant.active_orders) + 100)
        is_ok = abs(dia - nominal) <= tol
        part = AutoPart("2112-1004015", sn, "Поршень ДВС", dim, spec, is_defect_free=is_ok)
        piston = EnginePiston(part, piston_diameter_mm=dia, compression_height_mm=38.3)

        verdict = self.inspector.inspect_part(is_ok=part.is_defect_free)
        print(f"Проверена деталь: {part.get_part_label()} (D={piston.piston_diameter_mm:.3f} мм)")
        print(f"Вердикт контролера {self.inspector.inspector_badge_id}: {verdict}")

        passed = 495 if is_ok else 450
        rejected = 5 if is_ok else 50
        report = InspectionReport(f"АКТ-ОТК-{sn.sequence_id}", "ПАРТИЯ-100", self.inspector, passed_items=passed, rejected_items=rejected)
        print(report.sign_report())

    def action_simulate_emergency(self) -> None:
        """Сценарий симуляции нештатной ситуации и экстренного останова."""
        print("\n--- [10] Симуляция нештатной ситуации ---")
        try:
            print("Симуляция: критический перегрев шпиндельного узла...")
            self.machine_cnc.current_temperature = 95.0
            self.machine_cnc.check_overheat()
        except PlantBaseException as err:
            print(f"Сработала аварийная защита: {err.get_details()}")
            self.plant.emergency_plant_shutdown("Аварийный перегрев станка ЧПУ-01")
            print("Производственные линии переведены в безопасный аварийный останов.")

    def action_show_plant_status(self) -> None:
        """Сценарий вывода сводного статуса предприятия."""
        print("\n--- [11] Сводный отчет о состоянии завода ---")
        print(f"Предприятие: {self.plant.plant_name}")
        print(f"Директор: {self.director.employee.full_name}")
        print(f"Остаток бюджета развития: {self.director.annual_budget:,.2f} у.е.")
        print(f"Складских комплексов: {len(self.plant.warehouses)}")
        stored_str = f"{self.bin_a1.current_weight_kg:.1f} кг (макс. {self.bin_a1.max_weight_capacity_kg:.1f} кг)"
        print(f"Хранится сырья в ячейке {self.bin_a1.bin_code}: {stored_str}")
        print(f"Действующих линий: {len(self.plant.production_lines)}")
        print(f"Всего произведено деталей: {self.plant.total_parts_produced} шт.")
        print(f"Производственных нарядов: {len(self.plant.active_orders)}")
        for order in self.plant.active_orders:
            print(f"   * {order.order_id}: {order.target_part_type} ({order.quantity} шт.) — [{order.status}]")
        print(f"Коммерческих отгрузок / ТТН: {len(self.active_dispatches)}")
        for disp in self.active_dispatches:
            deliv_status = "СДАН (ВРУЧЕН)" if disp.is_delivered else "В ПУТИ"
            print(f"   * {disp.dispatch_id} ({disp.customer_order.customer.company_name}) — [{deliv_status}]")

    def _execute_command(self, choice: str) -> bool:
        """Выполняет выбранную команду меню. Возвращает False для завершения работы."""
        actions = {
            "1": self.action_daily_production,
            "2": self.action_create_order,
            "3": self.action_complete_order,
            "4": self.action_warehouse_management,
            "5": self.action_dispatch_customer_order,
            "6": self.action_confirm_delivery,
            "7": self.action_update_equipment,
            "8": self.action_update_personnel_and_budget,
            "9": self.action_quality_inspection,
            "10": self.action_simulate_emergency,
            "11": self.action_show_plant_status,
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
        self._input_gen = iter(auto_input) if auto_input is not None else None
        while True:
            self.print_menu()
            choice = self._prompt("Выберите пункт меню (0-11)", "0")
            if not self._execute_command(choice):
                break
