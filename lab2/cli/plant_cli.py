"""Интерактивный консольный интерфейс (CLI) завода по изготовлению автомобильных деталей."""

from __future__ import annotations
import json
import os
from typing import Optional, List, Iterator, Dict, Any

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
from plant.personnel.maintenance_engineer import MaintenanceEngineer
from plant.personnel.safety_officer import SafetyOfficer
from plant.personnel.toolmaker import Toolmaker
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

    STATE_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "plant_state.json")

    def __init__(self) -> None:
        self._input_gen: Optional[Iterator[str]] = None
        self.active_dispatches: List[DispatchOrder] = []
        self.employees: List[Employee] = []
        self._init_plant_and_storage()
        self._init_equipment_and_lines()
        self._init_partners_and_logistics()

    def _init_plant_and_storage(self) -> None:
        """Инициализирует дирекцию, склад, запасы сырья и начальные наряды."""
        director_contact = ContactInfo("director@autoplant.by", "+375-17-299-00-01", "Дирекция")
        self.director_emp = Employee("EMP-001", "Ковалев Алексей Сергеевич", "Генеральный директор", 12000.0, director_contact)
        self.director = PlantDirector(self.director_emp, annual_budget=5000000.0, strategic_plan_name="Стратегия-2026")
        self.plant = AutomotivePlant("Минский завод автокомпонентов", self.director)
        self.employees.append(self.director_emp)

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
        self.employees.append(op_emp)

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
        self.employees.append(qc_emp)

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

    def _prompt_int(
        self,
        message: str,
        default: int,
        min_val: Optional[int] = None,
        max_val: Optional[int] = None
    ) -> int:
        """Запрашивает целочисленное значение с валидацией границ."""
        raw = self._prompt(message, str(default))
        try:
            val = int(raw)
            if min_val is not None and val < min_val:
                print(f"Предупреждение: число должно быть не менее {min_val} (введено {val}). Применено значение {default}.")
                return default
            if max_val is not None and val > max_val:
                print(f"Предупреждение: число должно быть не более {max_val} (введено {val}). Применено значение {default}.")
                return default
            return val
        except ValueError:
            print(f"Предупреждение: некорректное число '{raw}', применено значение по умолчанию {default}.")
            return default

    def _prompt_float(
        self,
        message: str,
        default: float,
        min_val: Optional[float] = None,
        max_val: Optional[float] = None
    ) -> float:
        """Запрашивает вещественное значение с валидацией границ."""
        raw = self._prompt(message, str(default))
        try:
            val = float(raw)
            if min_val is not None and val < min_val:
                print(f"Предупреждение: число должно быть не менее {min_val} (введено {val}). Применено значение {default}.")
                return default
            if max_val is not None and val > max_val:
                print(f"Предупреждение: число должно быть не более {max_val} (введено {val}). Применено значение {default}.")
                return default
            return val
        except ValueError:
            print(f"Предупреждение: некорректное число '{raw}', применено значение по умолчанию {default}.")
            return default

    def print_menu(self) -> None:
        """Отображает главное интерактивное меню."""
        print("\n" + "=" * 74)
        print(f"   СИСТЕМА УПРАВЛЕНИЯ ПРЕДПРИЯТИЕМ: {self.plant.plant_name}")
        print("=" * 74)
        print(" 1. Запуск суточного производственного цикла линии")
        print(" 2. Управление производственными линиями (статус, пуск, перезапуск/сброс аварии)")
        print(" 3. Создание наряда-заказа на производство деталей")
        print(" 4. Сдать (завершить) наряд-заказ на склад готовой продукции")
        print(" 5. Пополнение и списание сырья со склада (обновление остатков)")
        print(" 6. Оформление коммерческого заказа и отгрузка клиенту (ТТН)")
        print(" 7. Сдать заказ клиенту (подтверждение доставки и акт приемки)")
        print(" 8. Обновление параметров оборудования и обслуживание (ЧПУ/ТО/заточка)")
        print(" 9. Персонал и бюджет (найм новых сотрудников, штатное расписание, оклады)")
        print("10. Контроль качества ОТК (проверка детали и акт)")
        print("11. Симуляция нештатной ситуации (аварийный останов линии)")
        print("12. Сводный паспорт предприятия и состояние всех заказов")
        print("13. Сохранение и загрузка состояния завода (JSON)")
        print(" 0. Выход")
        print("=" * 74)

    def action_daily_production(self) -> None:
        """Запуск производственного цикла линии с выбором количества смен."""
        print("\n--- [1] Запуск суточного производства ---")
        shifts = self._prompt_int("Количество рабочих смен для запуска", 1)
        if shifts <= 0:
            print(f"Предупреждение: количество смен должно быть положительным числом (> 0, введено {shifts}).")
            print("Производственный цикл не запускался. Выпущено деталей: 0 шт.")
            return

        # Проверка готовности линий к производству
        halted_count = 0
        for line in self.plant.production_lines:
            if not line.is_running and not line.start_line():
                halted_count += 1
                print(f"ВНИМАНИЕ: Линия '{line.line_name}' [{line.line_id}] остановлена или станки не готовы.")
        if halted_count > 0:
            print("Для пуска/перезапуска линий используйте пункт 2 меню ('Управление линиями').")

        total_cycle = 0
        for _ in range(shifts):
            total_cycle += self.plant.execute_daily_production()

        print(f"Отработано рабочих смен: {shifts}.")
        print(f"Выпущено за цикл: {total_cycle} шт. автодеталей.")
        print(f"Всего произведено предприятием: {self.plant.total_parts_produced} шт.")

    def action_manage_production_lines(self) -> None:
        """Управление линиями цеха: просмотр статуса, пуск, плановый останов и перезапуск после аварии."""
        print("\n--- [2] Управление производственными линиями ---")
        if not self.plant.production_lines:
            print("На предприятии нет зарегистрированных производственных линий.")
            return

        print("Действующие линии завода:")
        for idx, line in enumerate(self.plant.production_lines, start=1):
            status = "РАБОТАЕТ (ЗАПУЩЕНА)" if line.is_running else "ОСТАНОВЛЕНА / ТРЕБУЕТСЯ ПУСК"
            print(f"  [{idx}] {line.line_id} | '{line.line_name}' | Постов: {len(line.stations)} | Статус: {status}")
            for st_idx, st in enumerate(line.stations, start=1):
                op_name = st.operator.employee.full_name if st.operator else "НЕТ ОПЕРАТОРА"
                m_stat = f"{st.machine.current_temperature:.1f}°C, исправен: {st.machine.is_operational}"
                print(f"       Пост {st_idx} ({st.station_id}): Станок {st.machine.machine_id} [{m_stat}] | Оператор: {op_name}")

        print("\nОперации: 1 - Перезапустить / возобновить работу линии (сброс аварий), 2 - Плановый останов линии, 3 - Добавить пост")
        choice = self._prompt("Выберите операцию", "1")

        if choice == "1":
            choice_idx_str = self._prompt("Номер линии для запуска / перезапуска", "1")
            try:
                line_idx = int(choice_idx_str) - 1
                if 0 <= line_idx < len(self.plant.production_lines):
                    target_line = self.plant.production_lines[line_idx]
                    success = target_line.resume_line()
                    if success:
                        print(f"УСПЕХ: Линия '{target_line.line_name}' успешно перезапущена и введена в строй!")
                        print("Станки охлаждены, неисправности устранены, операторы на постах готовы к работе.")
                    else:
                        print(f"ОШИБКА: Не удалось запустить линию '{target_line.line_name}'. Проверьте укомплектованность постов.")
                else:
                    print("Указан некорректный номер линии.")
            except Exception as err:
                print(f"Ошибка при перезапуске линии: {err}")
        elif choice == "2":
            choice_idx_str = self._prompt("Номер линии для останова", "1")
            try:
                line_idx = int(choice_idx_str) - 1
                if 0 <= line_idx < len(self.plant.production_lines):
                    target_line = self.plant.production_lines[line_idx]
                    target_line.stop_line()
                    print(f"Линия '{target_line.line_name}' переведена в режим планового останова.")
                else:
                    print("Указан некорректный номер линии.")
            except Exception as err:
                print(f"Ошибка при останове линии: {err}")
        elif choice == "3":
            new_st_id = f"СТ-{len(self.prod_line.stations) + 1:02d}"
            new_machine = Machine(f"СТАНОК-{new_st_id}", "HAAS-ST20", operating_hours=0.0, current_temperature=22.0)
            new_ws = WorkStation(new_st_id, new_machine)
            new_ws.assign_operator(self.operator)
            self.prod_line.add_station(new_ws)
            print(f"УСПЕХ: На линию '{self.prod_line.line_name}' добавлен технологический пост {new_st_id} ({new_machine.model}).")
        else:
            print("Неизвестная операция управления линиями.")

    def action_create_order(self) -> None:
        """Оформление нового производственного наряда-заказа с пользовательскими параметрами."""
        print("\n--- [3] Оформление наряда-заказа ---")
        order_num = len(self.plant.active_orders) + 1
        default_id = f"НАРЯД-{order_num:03d}"
        order_id = self._prompt("Номер наряда-заказа", default_id)
        part_name = self._prompt("Наименование автодетали", "Поршень ДВС 2112")
        qty = self._prompt_int("Количество деталей в партии (шт.)", 500, max_val=100000)
        if qty <= 0:
            print("Ошибка: объем партии деталей должен быть больше нуля. Наряд не создан.")
            return
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
        print("\n--- [4] Сдача / завершение наряда-заказа ---")
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
        print("\n--- [5] Управление и обновление остатков склада ---")
        pct = self.bin_a1.get_occupancy_ratio() * 100.0
        bin_weight_str = f"{self.bin_a1.current_weight_kg:.1f} / {self.bin_a1.max_weight_capacity_kg:.1f} кг"
        print(f"Ячейка {self.bin_a1.bin_code}: остаток {bin_weight_str} ({pct:.1f}%)")
        print(f"Партия сырья {self.steel_batch.batch_id} ({self.raw_steel.name}): доступно {self.steel_batch.quantity_kg:.1f} кг")
        print("Операции: 1 - Пополнить склад сырьем (приемка), 2 - Списать сырье в цех, 3 - Добавить новую ячейку")
        op_choice = self._prompt("Выберите операцию", "1")

        if op_choice == "1":
            qty = self._prompt_float("Масса сырья для пополнения (кг)", 250.0)
            if qty <= 0:
                print("Ошибка: масса пополнения должна быть больше нуля.")
                return
            try:
                self.bin_a1.deposit_material(qty)
                self.steel_batch.quantity_kg = round(self.steel_batch.quantity_kg + qty, 2)
                print(f"УСПЕХ: Данные склада обновлены! Загружено {qty:.1f} кг.")
                print(f"Текущий остаток в ячейке {self.bin_a1.bin_code}: {self.bin_a1.current_weight_kg:.1f} кг.")
            except Exception as err:
                print(f"Ошибка при пополнении склада: {err}")
        elif op_choice == "2":
            qty = self._prompt_float("Масса сырья для списания (кг)", 120.0)
            if qty <= 0:
                print("Ошибка: масса списания должна быть больше нуля.")
                return
            try:
                self.bin_a1.withdraw_material(qty)
                self.steel_batch.consume_material(qty)
                print(f"УСПЕХ: Сырье списано! Отгружено в цех {qty:.1f} кг.")
                print(f"Остаток в ячейке {self.bin_a1.bin_code}: {self.bin_a1.current_weight_kg:.1f} кг.")
            except Exception as err:
                print(f"Ошибка при списании сырья: {err}")
        elif op_choice == "3":
            code = self._prompt("Код новой ячейки хранения", f"B-{len(self.warehouse.storage_bins) + 1:02d}")
            cap = self._prompt_float("Предельная грузоподъемность (кг)", 3000.0, min_val=10.0)
            new_bin = StorageBin(code, max_weight_capacity_kg=cap)
            self.warehouse.add_bin(new_bin)
            print(f"УСПЕХ: На складе {self.warehouse.warehouse_id} зарегистрирована новая ячейка {code} (вместимость {cap:.1f} кг).")
        else:
            print("Неизвестная операция со складом.")

    def action_dispatch_customer_order(self) -> None:
        """Оформление коммерческого контракта и отгрузка партии автодеталей (ТТН)."""
        print("\n--- [6] Оформление коммерческого заказа и отгрузка (ТТН) ---")
        client_order_id = self._prompt("Номер контракта / заказа", f"ДОГОВОР-{len(self.active_dispatches) + 1:03d}")
        part_name = self._prompt("Наименование автодетали для поставки", "Поршень ДВС в сборе")
        qty = self._prompt_int("Объем поставки (шт.)", 400)
        if qty <= 0:
            print("Ошибка: объем поставки должен быть больше нуля.")
            return
        unit_price = self._prompt_float("Цена за единицу (у.е.)", 45.0)
        if unit_price <= 0:
            print("Ошибка: цена за единицу должна быть положительной.")
            return

        try:
            order = CustomerOrder(client_order_id, self.customer)
            order.add_part_order(part_name, quantity=qty, unit_price=unit_price)
            self.customer.apply_loyalty_discount(volume_bought_units=50000)
            final_sum = order.calculate_final_price()
            order.dispatch()

            pallet_weight = round(qty * 0.003, 2)
            self.truck.load_pallet(pallet_weight_tons=pallet_weight)
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
        print("\n--- [7] Сдача заказа клиенту (подтверждение доставки) ---")
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
        print("\n--- [8] Обновление параметров оборудования и обслуживание ---")
        temp_str = f"Скорость: {self.cnc_station.spindle_rpm} об/мин | Темп: {self.machine_cnc.current_temperature:.1f}°C"
        print(f"ЧПУ: {self.machine_cnc.machine_id} ({self.machine_cnc.model}) | {temp_str} | Исправен: {self.machine_cnc.is_operational}")
        wear_str = f"Износ: {self.cutter.flank_wear_mm:.3f} мм (лимит {self.cutter.max_wear_limit_mm} мм) | Острый: {self.cutter.is_usable()}"
        print(f"Инструмент: {self.cutter.tool_id} | {wear_str}")
        print("Операции: 1 - Задать обороты шпинделя ЧПУ, 2 - Провести ТО/охлаждение станка, 3 - Переточить инструмент, 4 - Зарегистрировать станок")
        sub_choice = self._prompt("Выберите операцию", "1")

        if sub_choice == "1":
            new_rpm = self._prompt_int("Новая частота вращения шпинделя (об/мин)", 7200, min_val=500, max_val=24000)
            try:
                self.cnc_station.set_spindle_speed(new_rpm)
                print(f"УСПЕХ: Параметры ЧПУ обновлены! Установлены обороты: {self.cnc_station.spindle_rpm} об/мин.")
            except Exception as err:
                print(f"Ошибка обновления скорости: {err}")
        elif sub_choice == "2":
            self.machine_cnc.service(target_temperature=25.0)
            print(f"УСПЕХ: Техническое обслуживание завершено. Станок {self.machine_cnc.machine_id} охлажден до 25.0°C и готов к работе.")
        elif sub_choice == "3":
            self.cutter.regrind()
            print(f"УСПЕХ: Инструмент {self.cutter.tool_id} переточен! Износ: {self.cutter.flank_wear_mm} мм, лезвие острое.")
        elif sub_choice == "4":
            mid = self._prompt("Инвентарный номер станка", "СТАНОК-02")
            model = self._prompt("Модель оборудования", "DMG MORI CTX 310")
            new_m = Machine(mid, model, operating_hours=0.0, current_temperature=22.0)
            print(f"УСПЕХ: Станок {new_m.machine_id} ({new_m.model}) зарегистрирован в базе оборудования.")
        else:
            print("Неизвестная операция с оборудованием.")

    def action_update_personnel_and_budget(self) -> None:
        """Обновление данных сотрудников, наем нового персонала и управление бюджетом завода."""
        print("\n--- [9] Персонал и бюджет предприятия ---")
        print(f"Директор: {self.director.employee.full_name} | Бюджет: {self.director.annual_budget:,.2f} у.е.")
        print(f"Всего сотрудников в штате: {len(self.employees)}")

        print("\nОперации:")
        print(" 1 - Пополнить бюджет предприятия")
        print(" 2 - Нанять нового сотрудника (добавление в штат)")
        print(" 3 - Просмотреть штатное расписание (список всех сотрудников)")
        print(" 4 - Повысить сотрудника / изменить оклад")
        print(" 5 - Изменить квалификационный разряд оператора")
        sub_choice = self._prompt("Выберите операцию", "1")

        if sub_choice == "1":
            add_budget = self._prompt_float("Сумма пополнения бюджета (у.е.)", 500000.0)
            if add_budget <= 0:
                print("Ошибка: сумма пополнения должна быть больше нуля.")
                return
            self.director.annual_budget = round(self.director.annual_budget + add_budget, 2)
            print(f"УСПЕХ: Бюджет обновлен! Текущий годовой фонд: {self.director.annual_budget:,.2f} у.е.")
        elif sub_choice == "2":
            # Наем нового сотрудника
            print("\n--- Найм нового сотрудника ---")
            emp_id = f"EMP-{len(self.employees) + 101:03d}"
            name = self._prompt("ФИО сотрудника", "Васильев Андрей Петрович")
            print("Должности: 1 - Оператор станков с ЧПУ, 2 - Контролер ОТК, 3 - Инженер по ТО, 4 - Инспектор по ТБ, 5 - Слесарь-инструментальщик")
            role_choice = self._prompt("Выберите роль", "1")
            roles_map = {
                "1": ("Оператор станков с ЧПУ", 2700.0, "Цех мехобработки"),
                "2": ("Контролер качества ОТК", 2400.0, "Отдел технического контроля"),
                "3": ("Инженер по техобслуживанию", 3200.0, "Служба главного механика"),
                "4": ("Инспектор по технике безопасности", 2500.0, "Отдел охраны труда"),
                "5": ("Слесарь-инструментальщик", 2600.0, "Инструментальный участок"),
            }
            default_pos, default_sal, dept = roles_map.get(role_choice, ("Специалист производства", 2500.0, "Производство"))
            pos = self._prompt("Должность", default_pos)
            sal = self._prompt_float("Месячный оклад (у.е.)", default_sal, min_val=500.0)
            phone = self._prompt("Контактный телефон", "+375-29-555-01-02")
            email = self._prompt("Электронная почта", f"emp{len(self.employees) + 1}@autoplant.by")

            contact = ContactInfo(email, phone, dept)
            new_emp = Employee(emp_id, name, pos, sal, contact)
            self.employees.append(new_emp)

            if role_choice == "1":
                _ = MachineOperator(new_emp, qualification_rank=4, safety_certified=True)
                print(f"УСПЕХ: Новый оператор {name} успешно принят на работу (Разряд 4, {pos})!")
            elif role_choice == "2":
                insp = QualityInspector(new_emp, inspector_badge_id=f"ОТК-{len(self.employees) + 50}")
                print(f"УСПЕХ: Новый контролер ОТК {name} принят на работу (Жетон {insp.inspector_badge_id})!")
            elif role_choice == "3":
                eng = MaintenanceEngineer(new_emp, certification_level="Высшая категория")
                print(f"УСПЕХ: Новый инженер по ТО {name} принят на работу ({eng.certification_level})!")
            elif role_choice == "4":
                _ = SafetyOfficer(new_emp, safety_policy_version=f"ISO-45001-rev{len(self.employees)}")
                print(f"УСПЕХ: Инспектор по ТБ {name} принят на работу!")
            elif role_choice == "5":
                _ = Toolmaker(new_emp, specialty="Штампы и пресс-формы", precision_tolerance_mm=0.005)
                print(f"УСПЕХ: Слесарь-инструментальщик {name} принят на работу!")
            else:
                print(f"УСПЕХ: Сотрудник {name} добавлен в штатное расписание предприятия!")
        elif sub_choice == "3":
            print("\n--- Штатное расписание завода ---")
            for idx, emp in enumerate(self.employees, start=1):
                info_str = f"Оклад: {emp.salary:,.2f} у.е. | Тел: {emp.contact_info.phone_number}"
                print(f"  [{idx}] {emp.employee_id} | {emp.full_name} | {emp.position} | {info_str}")
        elif sub_choice == "4":
            print("Список сотрудников для повышения:")
            for idx, emp in enumerate(self.employees, start=1):
                print(f"  [{idx}] {emp.full_name} ({emp.position}) — текущий оклад: {emp.salary:,.2f} у.е.")
            emp_idx_str = self._prompt("Выберите номер сотрудника", "2")
            try:
                emp_idx = int(emp_idx_str) - 1
                if 0 <= emp_idx < len(self.employees):
                    target_emp = self.employees[emp_idx]
                    new_pos = self._prompt("Новая должность сотрудника", target_emp.position)
                    raise_pct = self._prompt_float("Процент индексации оклада (%)", 15.0, min_val=0.0, max_val=200.0)
                    target_emp.promote(new_pos, raise_pct)
                    print(f"УСПЕХ: Сотрудник обновлен! Должность: {target_emp.position}, оклад: {target_emp.salary:,.2f} у.е.")
                else:
                    print("Указан некорректный номер сотрудника.")
            except Exception as err:
                print(f"Ошибка обновления данных сотрудника: {err}")
        elif sub_choice == "5":
            new_rank = self._prompt_int("Новый квалификационный разряд оператора (1-6)", 6, min_val=1, max_val=6)
            self.operator.qualification_rank = new_rank
            print(f"УСПЕХ: Квалификационный разряд обновлен! Текущий разряд оператора: {self.operator.qualification_rank}.")
        else:
            print("Неизвестная операция с персоналом.")

    def action_quality_inspection(self) -> None:
        """Сценарий проверки качества и приемки партии деталей (ОТК)."""
        print("\n--- [10] Контроль качества ОТК ---")
        nominal = 82.46
        tol = 0.03
        dia = self._prompt_float(f"Измеренный диаметр поршня в мм (номинал {nominal}±{tol})", nominal, min_val=1.0)
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
        print("\n--- [11] Симуляция нештатной ситуации ---")
        try:
            print("Симуляция: критический перегрев шпиндельного узла оборудования...")
            self.machine_cnc.current_temperature = 95.0
            self.machine_cnc.check_overheat()
        except PlantBaseException as err:
            print(f"Сработала аварийная защита: {err.get_details()}")
            self.plant.emergency_plant_shutdown("Аварийный перегрев станка ЧПУ-01")
            print("Производственные линии переведены в безопасный аварийный останов.")
            print("Для возобновления работы выполните ТО оборудования (пункт 8) и перезапустите линию (пункт 2).")

    def action_show_plant_status(self) -> None:
        """Сценарий вывода сводного статуса предприятия."""
        print("\n--- [12] Сводный отчет о состоянии завода ---")
        print(f"Предприятие: {self.plant.plant_name}")
        print(f"Директор: {self.director.employee.full_name}")
        print(f"Остаток бюджета развития: {self.director.annual_budget:,.2f} у.е.")
        print(f"Штат сотрудников: {len(self.employees)} чел.")
        print(f"Складских комплексов: {len(self.plant.warehouses)}")
        stored_str = f"{self.bin_a1.current_weight_kg:.1f} кг (макс. {self.bin_a1.max_weight_capacity_kg:.1f} кг)"
        print(f"Хранится сырья в ячейке {self.bin_a1.bin_code}: {stored_str}")
        print(f"Действующих линий: {len(self.plant.production_lines)}")
        for line in self.plant.production_lines:
            st = "РАБОТАЕТ" if line.is_running else "ОСТАНОВЛЕНА"
            print(f"   * {line.line_id}: '{line.line_name}' [{st}], брака: {line.scrap_rate}%")
        print(f"Всего произведено деталей: {self.plant.total_parts_produced} шт.")
        print(f"Производственных нарядов: {len(self.plant.active_orders)}")
        for order in self.plant.active_orders:
            print(f"   * {order.order_id}: {order.target_part_type} ({order.quantity} шт.) — [{order.status}]")
        print(f"Коммерческих отгрузок / ТТН: {len(self.active_dispatches)}")
        for disp in self.active_dispatches:
            deliv_status = "СДАН (ВРУЧЕН)" if disp.is_delivered else "В ПУТИ"
            print(f"   * {disp.dispatch_id} ({disp.customer_order.customer.company_name}) — [{deliv_status}]")

    def save_to_json(self, filepath: Optional[str] = None) -> bool:
        """Сохраняет полное состояние завода в файл JSON."""
        path = filepath or self.STATE_FILE_PATH
        try:
            data: Dict[str, Any] = {
                "plant_name": self.plant.plant_name,
                "total_parts_produced": self.plant.total_parts_produced,
                "annual_budget": self.director.annual_budget,
                "director": {
                    "emp_id": self.director_emp.employee_id,
                    "name": self.director_emp.full_name,
                    "position": self.director_emp.position,
                    "salary": self.director_emp.salary,
                },
                "employees": [
                    {
                        "emp_id": emp.employee_id,
                        "name": emp.full_name,
                        "position": emp.position,
                        "salary": emp.salary,
                        "phone": emp.contact_info.phone_number,
                        "email": emp.contact_info.email,
                        "department": emp.contact_info.department,
                    }
                    for emp in self.employees
                ],
                "warehouse": {
                    "warehouse_id": self.warehouse.warehouse_id,
                    "bin_a1": {
                        "bin_code": self.bin_a1.bin_code,
                        "max_weight_capacity_kg": self.bin_a1.max_weight_capacity_kg,
                        "current_weight_kg": self.bin_a1.current_weight_kg,
                    },
                    "steel_batch": {
                        "batch_id": self.steel_batch.batch_id,
                        "material_name": self.raw_steel.name,
                        "quantity_kg": self.steel_batch.quantity_kg,
                    },
                },
                "equipment": {
                    "cnc_machine": {
                        "machine_id": self.machine_cnc.machine_id,
                        "model": self.machine_cnc.model,
                        "operating_hours": self.machine_cnc.operating_hours,
                        "current_temperature": self.machine_cnc.current_temperature,
                        "is_operational": self.machine_cnc.is_operational,
                    },
                    "spindle_rpm": self.cnc_station.spindle_rpm,
                    "cutter": {
                        "tool_id": self.cutter.tool_id,
                        "flank_wear_mm": self.cutter.flank_wear_mm,
                    },
                },
                "production_lines": [
                    {
                        "line_id": line.line_id,
                        "line_name": line.line_name,
                        "is_running": line.is_running,
                        "scrap_rate": line.scrap_rate,
                    }
                    for line in self.plant.production_lines
                ],
                "active_orders": [
                    {
                        "order_id": o.order_id,
                        "target_part_type": o.target_part_type,
                        "quantity": o.quantity,
                        "status": o.status,
                    }
                    for o in self.plant.active_orders
                ],
                "dispatches": [
                    {
                        "dispatch_id": d.dispatch_id,
                        "customer_name": d.customer_order.customer.company_name,
                        "is_delivered": d.is_delivered,
                        "vehicle_plate": d.delivery_vehicle.vehicle_plate,
                    }
                    for d in self.active_dispatches
                ],
            }
            os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as err:
            print(f"Ошибка сохранения состояния: {err}")
            return False

    def load_from_json(self, filepath: Optional[str] = None) -> bool:
        """Загружает состояние завода из файла JSON."""
        path = filepath or self.STATE_FILE_PATH
        if not os.path.exists(path):
            print(f"Файл состояния '{path}' не найден.")
            return False
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.plant.plant_name = data.get("plant_name", self.plant.plant_name)
            self.plant.total_parts_produced = data.get("total_parts_produced", self.plant.total_parts_produced)
            self.director.annual_budget = data.get("annual_budget", self.director.annual_budget)

            # Восстановление сотрудников
            emp_data_list = data.get("employees", [])
            if emp_data_list:
                self.employees = []
                for ed in emp_data_list:
                    contact = ContactInfo(ed.get("email", ""), ed.get("phone", ""), ed.get("department", "Производство"))
                    emp = Employee(ed["emp_id"], ed["name"], ed["position"], float(ed["salary"]), contact)
                    self.employees.append(emp)
                    if ed["emp_id"] == "EMP-001":
                        self.director.employee = emp
                    elif ed["emp_id"] == "EMP-102":
                        self.operator.employee = emp
                    elif ed["emp_id"] == "EMP-201":
                        self.inspector.employee = emp

            # Восстановление склада
            wh_data = data.get("warehouse", {})
            bin_data = wh_data.get("bin_a1", {})
            if bin_data:
                self.bin_a1.current_weight_kg = float(bin_data.get("current_weight_kg", self.bin_a1.current_weight_kg))
            batch_data = wh_data.get("steel_batch", {})
            if batch_data:
                self.steel_batch.quantity_kg = float(batch_data.get("quantity_kg", self.steel_batch.quantity_kg))

            # Восстановление оборудования
            eq_data = data.get("equipment", {})
            cnc_data = eq_data.get("cnc_machine", {})
            if cnc_data:
                self.machine_cnc.operating_hours = float(cnc_data.get("operating_hours", self.machine_cnc.operating_hours))
                self.machine_cnc.current_temperature = float(cnc_data.get("current_temperature", self.machine_cnc.current_temperature))
                self.machine_cnc.is_operational = bool(cnc_data.get("is_operational", True))
            if "spindle_rpm" in eq_data:
                self.cnc_station.spindle_rpm = int(eq_data["spindle_rpm"])
            cutter_data = eq_data.get("cutter", {})
            if cutter_data:
                self.cutter.flank_wear_mm = float(cutter_data.get("flank_wear_mm", self.cutter.flank_wear_mm))

            # Восстановление линий
            lines_data = data.get("production_lines", [])
            for ld in lines_data:
                for line in self.plant.production_lines:
                    if line.line_id == ld.get("line_id"):
                        line.is_running = bool(ld.get("is_running", False))
                        line.scrap_rate = float(ld.get("scrap_rate", 0.0))

            # Восстановление нарядов
            orders_data = data.get("active_orders", [])
            if orders_data:
                self.plant.active_orders = []
                for od in orders_data:
                    plan = ProductionPlan(f"ПЛАН-{od['order_id']}", planned_quantity=od["quantity"], deadline_date="2026-10-30")
                    ord_obj = ProductionOrder(od["order_id"], od["target_part_type"], od["quantity"], plan)
                    ord_obj.status = od.get("status", "СОЗДАН")
                    self.plant.receive_production_order(ord_obj)

            # Восстановление накладных
            disp_data = data.get("dispatches", [])
            for dd in disp_data:
                for d in self.active_dispatches:
                    if d.dispatch_id == dd.get("dispatch_id"):
                        d.is_delivered = bool(dd.get("is_delivered", False))

            return True
        except Exception as err:
            print(f"Ошибка загрузки состояния: {err}")
            return False

    def action_save_load_state(self) -> None:
        """Меню сохранения, загрузки и сброса состояния завода."""
        print("\n--- [13] Сохранение и загрузка состояния завода (JSON) ---")
        print(f"Текущий файл сохранения: {self.STATE_FILE_PATH}")
        print("Операции: 1 - Сохранить состояние в JSON, 2 - Загрузить состояние из JSON, 3 - Сбросить к исходным настройкам")
        choice = self._prompt("Выберите операцию", "1")

        if choice == "1":
            if self.save_to_json():
                print(f"УСПЕХ: Состояние завода успешно сохранено в '{self.STATE_FILE_PATH}'!")
            else:
                print("Не удалось сохранить состояние.")
        elif choice == "2":
            if self.load_from_json():
                print(f"УСПЕХ: Состояние завода успешно восстановлено из '{self.STATE_FILE_PATH}'!")
            else:
                print("Не удалось загрузить состояние.")
        elif choice == "3":
            self.active_dispatches = []
            self.employees = []
            self._init_plant_and_storage()
            self._init_equipment_and_lines()
            self._init_partners_and_logistics()
            print("УСПЕХ: Параметры завода сброшены к начальным значениям по умолчанию.")
        else:
            print("Неизвестная операция.")

    def _execute_command(self, choice: str) -> bool:
        """Выполняет выбранную команду меню. Возвращает False для завершения работы."""
        actions = {
            "1": self.action_daily_production,
            "2": self.action_manage_production_lines,
            "3": self.action_create_order,
            "4": self.action_complete_order,
            "5": self.action_warehouse_management,
            "6": self.action_dispatch_customer_order,
            "7": self.action_confirm_delivery,
            "8": self.action_update_equipment,
            "9": self.action_update_personnel_and_budget,
            "10": self.action_quality_inspection,
            "11": self.action_simulate_emergency,
            "12": self.action_show_plant_status,
            "13": self.action_save_load_state,
        }
        if choice == "0":
            save_on_exit = self._prompt("Сохранить текущее состояние перед выходом? (да/нет)", "нет").lower()
            if save_on_exit in ("да", "д", "yes", "y"):
                self.save_to_json()
                print("Состояние завода сохранено.")
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
        if os.path.exists(self.STATE_FILE_PATH) and auto_input is None:
            print(f"[Информация] Файл сохраненного состояния: '{self.STATE_FILE_PATH}' (загрузка через пункт 13).")

        while True:
            self.print_menu()
            choice = self._prompt("Выберите пункт меню (0-13)", "0")
            if not self._execute_command(choice):
                break
