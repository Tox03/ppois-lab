# Лабораторная работа №2. Крупный ООП-проект
## Предметная область: Завод по изготовлению автомобильных деталей

### Описание проекта
Данный проект представляет собой высокодетализированную объектно-ориентированную модель крупного машиностроительного предприятия по производству автокомпонентов и автомобильных узлов (поршни ДВС, тормозные диски, амортизаторы, валы трансмиссий, топливные форсунки, рычаги подвески, выпускные коллекторы и др.). Архитектура охватывает складское хозяйство, раскрой и литье сырья, станочный парк (прессы, ЧПУ-центры, сварочные роботы, лазерные комплексы, закалочные печи), метрологическую службу ОТК, персонал, производственное планирование, управление качеством по стандарту IATF 16949 и логистику.

### Структура проекта и архитектурные правила
- Язык программирования: **Python 3**.
- **Строго 1 класс на 1 файл**: каждый класс доменной модели и каждое исключение вынесены в индивидуальный `.py`-файл.
- Все комментарии, документация и docstring выполнены на **русском языке**.
- Никаких сторонних внешних библиотек (запуск тестов через стандартный `unittest`).

## Таблица классов предметной области

Формат строки: `Класс | число полей | число методов | связанные классы`.

| Класс | Поля | Методы | Ассоциации (связанные классы) |
|---|---|---|---|
| Address | 4 | 2 | — |
| AlloyIngot | 5 | 3 | RawMaterial |
| AutoPart | 6 | 3 | Dimension, QualityCheckFailedException, SerialNumber, TechnicalSpecification |
| AutomotivePlant | 6 | 5 | MaterialWarehouse, PlantDirector, ProductionLine, ProductionOrder |
| BrakeDisc | 5 | 3 | AutoPart |
| CalibrationTool | 5 | 3 | CalibrationExpiredException |
| ChemicalCoolant | 4 | 3 | — |
| CmmScanner | 4 | 3 | AutoPart, CalibrationExpiredException, CalibrationTool |
| CncMillingMachine | 5 | 3 | CuttingTool, Machine, MachineMalfunctionException |
| ContactInfo | 3 | 2 | — |
| ControlArm | 5 | 3 | AutoPart |
| Customer | 5 | 3 | Address, ContactInfo |
| CustomerOrder | 5 | 3 | Customer |
| CuttingTool | 5 | 3 | ToolWearExceededException |
| DefectReport | 5 | 3 | AutoPart, QualityInspector |
| DeliveryVehicle | 5 | 3 | — |
| Dimension | 4 | 3 | Dimension |
| DispatchOrder | 5 | 3 | CustomerOrder, DeliveryVehicle |
| Employee | 5 | 3 | ContactInfo |
| EnergyMeter | 3 | 3 | — |
| EnginePiston | 5 | 3 | AutoPart |
| EquipmentSensor | 5 | 3 | Machine |
| ExhaustManifold | 5 | 3 | AutoPart |
| FuelInjector | 5 | 3 | AutoPart |
| GearboxShaft | 5 | 3 | AutoPart |
| HardnessTester | 4 | 3 | CalibrationExpiredException, CalibrationTool, GearboxShaft |
| HeatTreatmentFurnace | 5 | 3 | EquipmentOverheatException, Machine |
| InspectionReport | 5 | 3 | QualityInspector |
| LaserCutter | 5 | 3 | Machine, MachineMalfunctionException |
| Machine | 6 | 4 | EquipmentOverheatException, MachineMalfunctionException |
| MachineOperator | 4 | 3 | Employee, Machine, SafetyViolationException |
| MaintenanceEngineer | 4 | 3 | Employee, Machine |
| MaintenanceLog | 5 | 3 | Machine |
| ManufacturingProcess | 4 | 3 | — |
| MaterialBatch | 5 | 3 | RawMaterial, RawMaterialShortageException |
| MaterialSupplier | 4 | 3 | ContactInfo |
| MaterialWarehouse | 4 | 3 | Address, StorageBin |
| MetalSheet | 5 | 3 | RawMaterial |
| PaintingBooth | 5 | 3 | Machine, MachineMalfunctionException |
| PlantDirector | 4 | 3 | Employee |
| PlasticPellet | 4 | 3 | MaterialDefectException |
| ProductionLine | 6 | 4 | DefectThresholdExceededException, ProductionLineHaltException, WorkStation |
| ProductionOrder | 5 | 3 | OrderCapacityExceededException, ProductionPlan |
| ProductionPlan | 4 | 3 | — |
| QualityInspector | 4 | 3 | Employee |
| QualityStandard | 4 | 3 | — |
| RawMaterial | 4 | 2 | — |
| RubberCompound | 4 | 3 | — |
| SafetyOfficer | 4 | 3 | Employee, SafetyViolationException |
| ScrapRecord | 4 | 3 | — |
| SerialNumber | 4 | 3 | — |
| ShiftSupervisor | 4 | 3 | Employee, Machine, MachineOperator |
| ShippingPallet | 5 | 3 | AutoPart, StorageExhaustedException |
| ShockAbsorber | 5 | 3 | AutoPart |
| StampingPress | 5 | 3 | Machine, MachineMalfunctionException, ToolingFixture |
| StorageBin | 4 | 3 | StorageExhaustedException |
| TechnicalSpecification | 5 | 3 | InvalidSpecificationException |
| TensileTester | 4 | 3 | CalibrationExpiredException, CalibrationTool, TechnicalSpecification |
| ToolingFixture | 5 | 3 | ToolWearExceededException |
| Toolmaker | 4 | 3 | CuttingTool, Employee, ToolingFixture |
| WeldingRobot | 5 | 3 | Machine, MachineMalfunctionException |
| WorkShift | 4 | 3 | ShiftSupervisor |
| WorkStation | 4 | 3 | Machine, MachineOperator |

### Исключения (14)

- **CalibrationExpiredException** — Вызывается, если метрологический прибор или датчик не прошел периодическую поверку.
- **DefectThresholdExceededException** — Вызывается, если процент дефектных деталей на линии превысил допустимый порог стандарта IATF.
- **EquipmentOverheatException** — Вызывается при превышении максимально допустимой рабочей температуры станка или печи.
- **InvalidSpecificationException** — Вызывается при обнаружении недопустимых геометрических или прочностных параметров в КД.
- **MachineMalfunctionException** — Вызывается при аварийном сбое узлов станка, заклинивании или обрыве привода.
- **MaterialDefectException** — Вызывается при обнаружении несоответствия физико-химических свойств сырья.
- **OrderCapacityExceededException** — Вызывается при нехватке производственных мощностей цеха для выполнения заказа в срок.
- **PlantBaseException** — Базовый класс для всех исключений производственного цикла завода.
- **ProductionLineHaltException** — Вызывается при аварийном размыкании цепи безопасности или сбое конвейера.
- **QualityCheckFailedException** — Вызывается, если параметры готовой автодетали выходят за пределы допусков чертежа.
- **RawMaterialShortageException** — Вызывается, если остаток сырья на складе меньше требуемого для партии.
- **SafetyViolationException** — Вызывается при несоблюдении регламентов безопасности оператором или рабочим.
- **StorageExhaustedException** — Вызывается при попытке складирования материала в переполненную ячейку хранения.
- **ToolWearExceededException** — Вызывается при превышении предельно допустимого ресурса работы инструмента.

### Итоговая статистика проекта

| Показатель | Значение | Требование |
|---|---|---|
| Классы (всего) | 77 | не менее 50 |
| Доменные классы | 63 | — |
| Исключения | 14 | не менее 12 |
| Поля (суммарно) | 328 | не менее 150 |
| Поведения (методы) | 204 | не менее 100 |
| Ассоциации | 103 | не менее 30 |
| Файлов с >1 классом | 0 | 0 (запрещено) |

## Подробное описание подсистем завода

### Базовые метрологические сущности и реквизиты (`plant/core/`)

#### Класс `Dimension`
*Описывает габаритные размеры автомобильной детали и конструкторские допуски.*
- **Поля (4)**: `height_mm`, `length_mm`, `tolerance_mm`, `width_mm`
- **Методы (3)**: `calculate_volume_cm3()`, `is_within_tolerance()`, `scale()`
- **Ассоциации**: `Dimension`

#### Класс `TechnicalSpecification`
*Определяет прочностные и чистовые требования к изготовлению автодетали.*
- **Поля (5)**: `is_critical`, `max_allowed_roughness_ra`, `required_tensile_strength_mpa`, `spec_id`, `standard_code`
- **Методы (3)**: `validate_roughness()`, `verify_strength()`, `mark_as_critical()`
- **Ассоциации**: `InvalidSpecificationException`

#### Класс `SerialNumber`
*Генератор и валидатор заводской сквозной маркировки автокомпонентов.*
- **Поля (4)**: `is_active`, `prefix`, `sequence_id`, `year`
- **Методы (3)**: `generate_code()`, `validate_format()`, `deactivate()`

#### Класс `Address`
*Хранит адресные реквизиты цехов завода, поставщиков сырья и дилерских центров.*
- **Поля (4)**: `city`, `country`, `postal_code`, `street`
- **Методы (2)**: `format_full_address()`, `is_domestic()`

#### Класс `ContactInfo`
*Хранит электронные и телефонные каналы связи персонала и внешних партнеров.*
- **Поля (3)**: `department`, `email`, `phone_number`
- **Методы (2)**: `validate_contact()`, `format_vcard()`

### Сырье, материалы и складское хозяйство (`plant/materials/`)

#### Класс `RawMaterial`
*Описывает свойства базового сырья (сталь, алюминиевый сплав, полимер).*
- **Поля (4)**: `base_cost_per_kg`, `density_g_cm3`, `material_id`, `name`
- **Методы (2)**: `calculate_volume_cost()`, `estimate_mass_kg()`

#### Класс `MetalSheet`
*Описывает листовой прокат, используемый на операциях вырубки и вытяжки.*
- **Поля (5)**: `is_galvanized`, `raw_material`, `sheet_id`, `steel_grade`, `thickness_mm`
- **Методы (3)**: `calculate_sheet_mass()`, `check_formability()`, `apply_galvanizing()`
- **Ассоциации**: `RawMaterial`

#### Класс `AlloyIngot`
*Описывает чушку цветного или черного сплава для плавильной печи цеха литья.*
- **Поля (5)**: `alloy_composition`, `ingot_id`, `melting_temperature_c`, `raw_material`, `weight_kg`
- **Методы (3)**: `check_furnace_compatibility()`, `calculate_casting_yield()`, `is_high_temp_alloy()`
- **Ассоциации**: `RawMaterial`

#### Класс `RubberCompound`
*Описывает эластомерную смесь для производства сайлентблоков, уплотнений и пыльников.*
- **Поля (4)**: `compound_id`, `cure_time_minutes`, `is_vulcanized`, `shore_hardness`
- **Методы (3)**: `validate_hardness()`, `simulate_vulcanization()`, `is_ready_for_assembly()`

#### Класс `PlasticPellet`
*Описывает партию гранулированного пластика (PA66, POM, PP) для отливки бачков и коллекторов.*
- **Поля (4)**: `melt_flow_index`, `moisture_pct`, `pellet_id`, `polymer_type`
- **Методы (3)**: `requires_drying()`, `perform_drying()`, `is_suitable_for_injection()`
- **Ассоциации**: `MaterialDefectException`

#### Класс `ChemicalCoolant`
*Описывает эмульсию СОЖ для фрезерных и токарных центров ЧПУ.*
- **Поля (4)**: `concentration_pct`, `coolant_id`, `is_contaminated`, `ph_level`
- **Методы (3)**: `is_within_ph_limits()`, `dilute_with_water()`, `replace_fluid()`

#### Класс `MaterialBatch`
*Учитывает поступление и расходование сырья в рамках одной поставки.*
- **Поля (5)**: `batch_id`, `is_inspected`, `quantity_kg`, `raw_material`, `received_date`
- **Методы (3)**: `consume_material()`, `approve_inspection()`, `calculate_total_value()`
- **Ассоциации**: `RawMaterial`, `RawMaterialShortageException`

#### Класс `StorageBin`
*Описывает адресное место хранения (ячейку/бункер) на складе сырья завода.*
- **Поля (4)**: `bin_code`, `current_weight_kg`, `is_locked`, `max_weight_capacity_kg`
- **Методы (3)**: `deposit_material()`, `withdraw_material()`, `get_occupancy_ratio()`
- **Ассоциации**: `StorageExhaustedException`

#### Класс `MaterialWarehouse`
*Управляет складскими ячейками, емкостями и запасами сырья.*
- **Поля (4)**: `address`, `storage_bins`, `total_capacity_tons`, `warehouse_id`
- **Методы (3)**: `add_bin()`, `find_available_bin()`, `calculate_total_stored_weight()`
- **Ассоциации**: `Address`, `StorageBin`

#### Класс `MaterialSupplier`
*Описывает внешнего поставщика металлов, химикатов и полимеров.*
- **Поля (4)**: `company_name`, `contact_info`, `rating`, `supplier_id`
- **Методы (3)**: `update_rating()`, `is_certified_vendor()`, `send_quality_claim()`
- **Ассоциации**: `ContactInfo`

### Станочный парк и промышленное оборудование (`plant/equipment/`)

#### Класс `Machine`
*Базовый класс технологического оборудования (станки, роботы, прессы).*
- **Поля (6)**: `current_temperature`, `is_operational`, `machine_id`, `max_allowed_temp`, `model`, `operating_hours`
- **Методы (4)**: `start()`, `stop()`, `record_hours()`, `check_overheat()`
- **Ассоциации**: `EquipmentOverheatException`, `MachineMalfunctionException`

#### Класс `ToolingFixture`
*Описывает формообразующую оснастку для штамповки и литья.*
- **Поля (5)**: `cycles_used`, `fixture_id`, `fixture_type`, `is_worn_out`, `max_cycles_lifetime`
- **Методы (3)**: `increment_cycles()`, `refurbish()`, `get_wear_ratio()`
- **Ассоциации**: `ToolWearExceededException`

#### Класс `CuttingTool`
*Описывает инструмент для механической обработки деталей на станках ЧПУ.*
- **Поля (5)**: `flank_wear_mm`, `is_sharp`, `max_wear_limit_mm`, `tool_id`, `tool_material`
- **Методы (3)**: `apply_cut_wear()`, `regrind()`, `is_usable()`
- **Ассоциации**: `ToolWearExceededException`

#### Класс `StampingPress`
*Управляет прессовым оборудованием и штамповой оснасткой для формовки деталей.*
- **Поля (5)**: `machine`, `parts_stamped`, `press_tonnage`, `stroke_length_mm`, `tooling_fixture`
- **Методы (3)**: `install_die()`, `execute_stroke()`, `calibrate_pressure()`
- **Ассоциации**: `Machine`, `MachineMalfunctionException`, `ToolingFixture`

#### Класс `CncMillingMachine`
*Осуществляет высокоточную фрезерную обработку корпусных автодеталей по G-коду.*
- **Поля (5)**: `active_tool`, `axis_count`, `coolant_pump_active`, `machine`, `spindle_rpm`
- **Методы (3)**: `mount_tool()`, `mill_contour()`, `set_spindle_speed()`
- **Ассоциации**: `CuttingTool`, `Machine`, `MachineMalfunctionException`

#### Класс `WeldingRobot`
*Осуществляет автоматическую сварку рычагов подвески, рам и подрамников.*
- **Поля (5)**: `arc_ignited`, `current_amperage`, `gas_flow_rate_lpm`, `machine`, `welding_wire_type`
- **Методы (3)**: `ignite_arc()`, `extinguish_arc()`, `perform_seam_weld()`
- **Ассоциации**: `Machine`, `MachineMalfunctionException`

#### Класс `PaintingBooth`
*Обеспечивает нанесение антикоррозийных и декоративных лакокрасочных покрытий.*
- **Поля (5)**: `airflow_speed_mps`, `chamber_humidity_pct`, `electrostatic_charge_kv`, `machine`, `paint_type`
- **Методы (3)**: `apply_powder_coat()`, `bake_paint()`, `ventilate()`
- **Ассоциации**: `Machine`, `MachineMalfunctionException`

#### Класс `HeatTreatmentFurnace`
*Управляет термообработкой валов, шестерен и тормозных дисков.*
- **Поля (5)**: `holding_time_minutes`, `is_heating`, `machine`, `quench_medium`, `target_temp_celsius`
- **Методы (3)**: `heat_to_target()`, `quench()`, `perform_hardening_cycle()`
- **Ассоциации**: `EquipmentOverheatException`, `Machine`

#### Класс `LaserCutter`
*Осуществляет прецизионную контурную резку листовых заготовок.*
- **Поля (5)**: `assist_gas`, `beam_focused`, `cutting_speed_m_per_min`, `laser_power_watts`, `machine`
- **Методы (3)**: `focus_beam()`, `cut_sheet_profile()`, `set_power()`
- **Ассоциации**: `Machine`, `MachineMalfunctionException`

#### Класс `EquipmentSensor`
*Измеряет вибрацию, температуру, давление масла или ток шпинделя станка.*
- **Поля (5)**: `alert_threshold`, `last_reading`, `machine`, `metric_name`, `sensor_id`
- **Методы (3)**: `read_value()`, `is_threshold_exceeded()`, `calibrate_offset()`
- **Ассоциации**: `Machine`

#### Класс `MaintenanceLog`
*Фиксирует регламентные работы, замену расходников и аварийные ремонты станка.*
- **Поля (5)**: `description`, `log_id`, `machine`, `maintenance_date`, `technician_name`
- **Методы (3)**: `log_service_event()`, `is_recent_service()`, `format_entry()`
- **Ассоциации**: `Machine`

### Персонал и управление сменами (`plant/personnel/`)

#### Класс `Employee`
*Описывает штатную единицу завода, систему оплаты труда и контактные реквизиты.*
- **Поля (5)**: `contact_info`, `employee_id`, `full_name`, `position`, `salary`
- **Методы (3)**: `calculate_annual_bonus()`, `promote()`, `is_management()`
- **Ассоциации**: `ContactInfo`

#### Класс `MachineOperator`
*Управляет закрепленным станком, производит заготовки и соблюдает охрану труда.*
- **Поля (4)**: `assigned_machine`, `employee`, `qualification_rank`, `safety_certified`
- **Методы (3)**: `assign_machine()`, `pass_safety_exam()`, `produce_units()`
- **Ассоциации**: `Employee`, `Machine`, `SafetyViolationException`

#### Класс `QualityInspector`
*Выполняет входной, операционный и выходной контроль качества продукции.*
- **Поля (4)**: `certified_standards`, `employee`, `inspections_count`, `inspector_badge_id`
- **Методы (3)**: `inspect_part()`, `add_certification()`, `get_rejection_rate()`
- **Ассоциации**: `Employee`

#### Класс `MaintenanceEngineer`
*Обеспечивает безаварийную эксплуатацию, ремонт и калибровку производственных линий.*
- **Поля (4)**: `active_repair_machine`, `certification_level`, `employee`, `repairs_performed`
- **Методы (3)**: `perform_preventive_maintenance()`, `repair_breakdown()`, `is_expert()`
- **Ассоциации**: `Employee`, `Machine`

#### Класс `Toolmaker`
*Изготавливает и доводит высокоточную оснастку, штампы и режущий инструмент.*
- **Поля (4)**: `employee`, `precision_tolerance_mm`, `refurbished_tools_count`, `specialty`
- **Методы (3)**: `regrind_cutting_tool()`, `refurbish_die()`, `verify_die_precision()`
- **Ассоциации**: `CuttingTool`, `Employee`, `ToolingFixture`

#### Класс `SafetyOfficer`
*Контролирует соблюдение требований техники безопасности и пожарной безопасности.*
- **Поля (4)**: `employee`, `inspections_conducted`, `safety_policy_version`, `violations_reported`
- **Методы (3)**: `conduct_line_audit()`, `issue_violation()`, `update_policy()`
- **Ассоциации**: `Employee`, `SafetyViolationException`

#### Класс `ShiftSupervisor`
*Руководит бригадой операторов цеха, координирует выпуск сменного задания.*
- **Поля (4)**: `active_shift_running`, `employee`, `shift_code`, `team_size`
- **Методы (3)**: `start_shift()`, `end_shift()`, `reassign_operator()`
- **Ассоциации**: `Employee`, `Machine`, `MachineOperator`

#### Класс `PlantDirector`
*Осуществляет общее стратегическое и финансовое руководство предприятием.*
- **Поля (4)**: `annual_budget`, `approved_projects`, `employee`, `strategic_plan_name`
- **Методы (3)**: `approve_budget_expense()`, `authorize_line_expansion()`, `sign_annual_report()`
- **Ассоциации**: `Employee`

### Производственный цикл и оперативное планирование (`plant/production/`)

#### Класс `WorkStation`
*Объединяет станок, оснастку и закрепленного оператора в единую рабочую ячейку.*
- **Поля (4)**: `is_active`, `machine`, `operator`, `station_id`
- **Методы (3)**: `assign_operator()`, `release_station()`, `process_part_cycle()`
- **Ассоциации**: `Machine`, `MachineOperator`

#### Класс `ManufacturingProcess`
*Определяет параметры техпроцесса: время штучной обработки, энергопотребление и режим.*
- **Поля (4)**: `duration_minutes`, `energy_consumption_kwh`, `process_name`, `required_temperature`
- **Методы (3)**: `calculate_power_cost()`, `optimize_duration()`, `is_thermal_process()`

#### Класс `ProductionLine`
*Управляет последовательностью рабочих постов цеха и мониторит качество.*
- **Поля (6)**: `is_running`, `line_id`, `line_name`, `max_allowed_scrap_pct`, `scrap_rate`, `stations`
- **Методы (4)**: `add_station()`, `start_line()`, `emergency_halt()`, `record_scrap()`
- **Ассоциации**: `DefectThresholdExceededException`, `ProductionLineHaltException`, `WorkStation`

#### Класс `WorkShift`
*Учитывает выработку за 8-часовую или 12-часовую рабочую смену.*
- **Поля (4)**: `hours_duration`, `shift_id`, `shift_type`, `supervisor`
- **Методы (3)**: `record_shift_output()`, `calculate_hourly_productivity()`, `is_night_shift()`
- **Ассоциации**: `ShiftSupervisor`

#### Класс `ProductionPlan`
*Определяет целевой объем производства компонентов к установленному сроку.*
- **Поля (4)**: `completed_quantity`, `deadline_date`, `plan_id`, `planned_quantity`
- **Методы (3)**: `register_output()`, `calculate_fulfillment_percentage()`, `is_plan_fulfilled()`

#### Класс `ProductionOrder`
*Оформляет запуск серии автодеталей в производственный процесс.*
- **Поля (5)**: `order_id`, `production_plan`, `quantity`, `status`, `target_part_type`
- **Методы (3)**: `link_plan()`, `start_production()`, `complete_order()`
- **Ассоциации**: `OrderCapacityExceededException`, `ProductionPlan`

#### Класс `EnergyMeter`
*Осуществляет коммерческий и технический учет расхода электроэнергии цехом.*
- **Поля (3)**: `meter_id`, `tariff_per_kwh`, `total_kwh`
- **Методы (3)**: `record_consumption()`, `calculate_energy_bill()`, `reset_monthly_counter()`

#### Класс `ScrapRecord`
*Учитывает факты технологического и неисправимого брака в цехах завода.*
- **Поля (4)**: `defect_reason`, `record_id`, `registered_date`, `scrapped_quantity`
- **Методы (3)**: `calculate_financial_loss()`, `is_critical_scrap()`, `format_summary()`

### Автомобильные детали и компоненты (`plant/parts/`)

#### Класс `AutoPart`
*Описывает базовые свойства автомобильной запчасти (геометрия, паспорт, ТУ).*
- **Поля (6)**: `dimension`, `is_defect_free`, `part_name`, `part_number`, `serial_number`, `spec`
- **Методы (3)**: `verify_dimensions()`, `mark_as_defective()`, `get_part_label()`
- **Ассоциации**: `Dimension`, `QualityCheckFailedException`, `SerialNumber`, `TechnicalSpecification`

#### Класс `EnginePiston`
*Описывает поршень цилиндропоршневой группы ДВС с юбкой и канавками колец.*
- **Поля (5)**: `auto_part`, `coating_type`, `compression_height_mm`, `piston_diameter_mm`, `ring_groove_count`
- **Методы (3)**: `check_bore_clearance()`, `calculate_thermal_expansion()`, `is_forged()`
- **Ассоциации**: `AutoPart`

#### Класс `BrakeDisc`
*Описывает тормозной диск с контролем толщины полотна и торцевого биения.*
- **Поля (5)**: `auto_part`, `disc_thickness_mm`, `is_ventilated`, `min_thickness_limit_mm`, `runout_microns`
- **Методы (3)**: `check_wear_limit()`, `verify_axial_runout()`, `simulate_braking_cycle()`
- **Ассоциации**: `AutoPart`

#### Класс `ShockAbsorber`
*Описывает стойку подвески или амортизатор с характеристиками демпфирования.*
- **Поля (5)**: `auto_part`, `damping_force_n`, `gas_pressure_bar`, `is_pressurized`, `stroke_length_mm`
- **Методы (3)**: `test_damping_performance()`, `recharge_gas()`, `is_leak_free()`
- **Ассоциации**: `AutoPart`

#### Класс `GearboxShaft`
*Описывает зубчатый шлицевой вал трансмиссии высокой твердости.*
- **Поля (5)**: `auto_part`, `gear_teeth_count`, `is_hardened`, `spline_count`, `surface_hardness_hrc`
- **Методы (3)**: `validate_hardness()`, `calculate_gear_ratio()`, `verify_spline_mesh()`
- **Ассоциации**: `AutoPart`

#### Класс `FuelInjector`
*Описывает прецизионный распылитель бензина или дизельного топлива.*
- **Поля (5)**: `auto_part`, `flow_rate_cc_min`, `nozzle_holes_count`, `operating_pressure_bar`, `spray_angle_deg`
- **Методы (3)**: `test_spray_pattern()`, `calculate_fuel_delivery()`, `is_high_pressure_gdi()`
- **Ассоциации**: `AutoPart`

#### Класс `ControlArm`
*Описывает штампованный или кованый рычаг подвески в сборе с сайлентблоками.*
- **Поля (5)**: `auto_part`, `ball_joint_fitted`, `bushing_count`, `is_aluminum`, `load_rating_kn`
- **Методы (3)**: `test_structural_strength()`, `install_ball_joint()`, `is_complete_subassembly()`
- **Ассоциации**: `AutoPart`

#### Класс `ExhaustManifold`
*Описывает многоканальный коллектор отвода отработавших газов.*
- **Поля (5)**: `auto_part`, `is_leak_tested`, `max_operating_temp_c`, `runner_count`, `wall_thickness_mm`
- **Методы (3)**: `perform_pressure_leak_test()`, `verify_thermal_resistance()`, `is_equal_length_runner()`
- **Ассоциации**: `AutoPart`

### Контроль качества, лаборатория ОТК и метрология (`plant/quality/`)

#### Класс `QualityStandard`
*Описывает требования IATF 16949 / ISO 9001 к допускам и прочности автодеталей.*
- **Поля (4)**: `max_tolerance_deviation`, `min_tensile_threshold`, `standard_name`, `version`
- **Методы (3)**: `audit_dimension()`, `audit_strength()`, `is_automotive_certified()`

#### Класс `CalibrationTool`
*Управляет интервалами поверки метрологического оборудования лаборатории ОТК.*
- **Поля (5)**: `calibration_interval_days`, `is_calibrated`, `last_calibration_date`, `tool_id`, `tool_name`
- **Методы (3)**: `check_calibration_validity()`, `recalibrate()`, `format_calibration_tag()`
- **Ассоциации**: `CalibrationExpiredException`

#### Класс `CmmScanner`
*Осуществляет оптическое и контактное 3D-сканирование готовых автокомпонентов.*
- **Поля (4)**: `calibration_tool`, `points_scanned`, `precision_microns`, `scanner_id`
- **Методы (3)**: `calibrate()`, `scan_part_cloud()`, `is_high_accuracy()`
- **Ассоциации**: `AutoPart`, `CalibrationExpiredException`, `CalibrationTool`

#### Класс `TensileTester`
*Проводит механические испытания образцов на предел прочности и текучести.*
- **Поля (4)**: `calibration_tool`, `max_force_kn`, `tester_id`, `tests_executed`
- **Методы (3)**: `calibrate()`, `execute_pull_test()`, `get_utilization()`
- **Ассоциации**: `CalibrationExpiredException`, `CalibrationTool`, `TechnicalSpecification`

#### Класс `HardnessTester`
*Измеряет поверхностную твердость деталей после термообработки индентором.*
- **Поля (4)**: `calibration_tool`, `measurements_count`, `method_type`, `tester_id`
- **Методы (3)**: `calibrate()`, `measure_hardness()`, `is_rockwell_method()`
- **Ассоциации**: `CalibrationExpiredException`, `CalibrationTool`, `GearboxShaft`

#### Класс `DefectReport`
*Фиксирует причину выбраковки конкретного экземпляра детали контролером ОТК.*
- **Поля (5)**: `auto_part`, `defect_description`, `inspector`, `report_id`, `severity_level`
- **Методы (3)**: `classify_disposition()`, `is_scrap()`, `format_ticket()`
- **Ассоциации**: `AutoPart`, `QualityInspector`

#### Класс `InspectionReport`
*Оформляет результаты сплошного или выборочного контроля партии автодеталей.*
- **Поля (5)**: `batch_id`, `inspector`, `passed_items`, `rejected_items`, `report_id`
- **Методы (3)**: `calculate_yield_rate()`, `sign_report()`, `is_batch_acceptable()`
- **Ассоциации**: `QualityInspector`

### Транспорт, логистика и клиентский сервис (`plant/logistics/`)

#### Класс `ShippingPallet`
*Обеспечивает формирование транспортного пакета деталей для автопогрузчика.*
- **Поля (5)**: `current_weight_kg`, `loaded_parts`, `max_capacity_parts`, `max_weight_kg`, `pallet_id`
- **Методы (3)**: `load_part()`, `unload_all()`, `is_full()`
- **Ассоциации**: `AutoPart`, `StorageExhaustedException`

#### Класс `Customer`
*Описывает покупателя автокомпонентов: автозаводы (OEM), дистрибьюторов автозапчастей.*
- **Поля (5)**: `address`, `company_name`, `contact_info`, `customer_id`, `discount_rate`
- **Методы (3)**: `apply_loyalty_discount()`, `format_customer_card()`, `is_major_automaker()`
- **Ассоциации**: `Address`, `ContactInfo`

#### Класс `CustomerOrder`
*Оформляет спецификацию поставки партии автокомпонентов заказчику.*
- **Поля (5)**: `customer`, `is_dispatched`, `order_id`, `requested_parts`, `total_price`
- **Методы (3)**: `add_part_order()`, `dispatch()`, `calculate_final_price()`
- **Ассоциации**: `Customer`

#### Класс `DeliveryVehicle`
*Обеспечивает межзаводскую транспортировку паллет с готовыми деталями.*
- **Поля (5)**: `carrying_capacity_tons`, `current_load_tons`, `is_ready`, `pallets_count`, `vehicle_plate`
- **Методы (3)**: `load_pallet()`, `depart_for_delivery()`, `get_load_factor()`

#### Класс `DispatchOrder`
*Связывает коммерческий заказ с транспортом доставки и маршрутным листом.*
- **Поля (5)**: `customer_order`, `delivery_vehicle`, `departure_date`, `dispatch_id`, `is_delivered`
- **Методы (3)**: `confirm_delivery()`, `calculate_transport_cost()`, `generate_waybill()`
- **Ассоциации**: `CustomerOrder`, `DeliveryVehicle`

### Главная управляющая система завода (`plant/`)

#### Класс `AutomotivePlant`
*Центральный управляющий класс производственного комплекса автокомпонентов.*
- **Поля (6)**: `active_orders`, `director`, `plant_name`, `production_lines`, `total_parts_produced`, `warehouses`
- **Методы (5)**: `register_warehouse()`, `add_production_line()`, `receive_production_order()`, `execute_daily_production()`, `emergency_plant_shutdown()`
- **Ассоциации**: `MaterialWarehouse`, `PlantDirector`, `ProductionLine`, `ProductionOrder`

## Запуск тестов и валидатора метрик

### Запуск модульных тестов:
```bash
cd lab2
python -m unittest discover -s tests -p "test_*.py" -v
```

### Запуск интерактивного консольного интерфейса (CLI):
```bash
python lab2\main.py
```

Интерактивное меню программы поддерживает управление полным жизненным циклом завода:
1. **Запуск суточного производства** — симуляция производственных смен на линии с учетом выработки.
2. **Создание наряда-заказа** — интерактивный ввод типа детали, объема партии и срока сдачи.
3. **Сдача (завершение) наряда-заказа** — выбор наряда из активных, фиксация выпуска и перевод в статус `ВЫПОЛНЕН`.
4. **Управление и обновление остатков склада** — интерактивное пополнение ячейки сырьем (приемка) или списание в цех.
5. **Оформление заказа клиента и отгрузка (ТТН)** — спецификация коммерческой поставки, расчет скидок и ТТН.
6. **Сдача заказа клиенту (подтверждение доставки)** — подписание акта приема-передачи и освобождение автотранспорта.
7. **Обновление параметров оборудования и обслуживание** — настройка оборотов шпинделя ЧПУ, плановое ТО / охлаждение, заточка инструмента.
8. **Обновление данных персонала и бюджета** — пополнение годового фонда завода, индексация окладов, повышение должности и квалификационного разряда.
9. **Контроль качества ОТК** — замеры геометрических размеров поршня с расчетом допуска и оформлением акта.
10. **Симуляция нештатной ситуации** — аварийный перегрев и экстренный останов линий предприятия.
11. **Сводный паспорт завода** — детализированный отчет о состоянии всех складов, нарядов, отгрузок и оборудования.

