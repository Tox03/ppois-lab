# Полный архитектурный справочник классов предметной области
## Лабораторная работа №2. «Завод по изготовлению автомобильных деталей»

В данном руководстве подробно разобран каждый из 77 классов системы: его файл, назначение, логика работы методов, поля и связи с другими классами.

---

## 1. Базовые метрологические сущности и реквизиты (`plant/core/`)

### 1.1. `Dimension`
* **Файл:** [`plant/core/Dimension.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/core/Dimension.py)
* **Что делает:** Описывает трехмерные геометрические размеры детали (длина, ширина, высота в миллиметрах) и конструкторский допуск.
* **Как работает:**
  * Поля: `length_mm`, `width_mm`, `height_mm`, `tolerance_mm`.
  * `calculate_volume_cm3()`: перемножает габариты и переводит кубические миллиметры в см³ делением на 1000.
  * `is_within_tolerance(target_dimension)`: сравнивает абсолютную разницу всех трех измерений с допустимой погрешностью `tolerance_mm`.
  * `scale(factor)`: возвращает новый объект `Dimension`, пропорционально смасштабированный на коэффициент.
* **Связи:** Ассоциирован с самим собой в методах сравнения; агрегируется базовой деталью [`AutoPart`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/AutoPart.py).

### 1.2. `TechnicalSpecification`
* **Файл:** [`plant/core/TechnicalSpecification.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/core/TechnicalSpecification.py)
* **Что делает:** Хранит конструкторско-технологические требования к автокомпоненту (прочность на разрыв, шероховатость поверхности Ra, стандарт ISO/ГОСТ).
* **Как работает:**
  * Поля: `spec_id`, `standard_code`, `required_tensile_strength_mpa`, `max_allowed_roughness_ra`, `is_critical`.
  * `validate_roughness(actual_ra)`: проверяет, не превышает ли фактическая чистота поверхности допустимый предел шероховатости. При отрицательном значении выбрасывает [`InvalidSpecificationException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/InvalidSpecificationException.py).
  * `verify_strength(actual_mpa)`: проверяет, выдерживает ли деталь требуемый предел прочности.
  * `mark_as_critical()`: выставляет признак детали повышенной ответственности (влияющей на безопасность автомобиля).
* **Связи:** Используется в [`AutoPart`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/AutoPart.py) и испытательном стенде [`TensileTester`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/quality/TensileTester.py). Выбрасывает [`InvalidSpecificationException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/InvalidSpecificationException.py).

### 1.3. `SerialNumber`
* **Файл:** [`plant/core/SerialNumber.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/core/SerialNumber.py)
* **Что делает:** Генерирует и валидирует уникальный сквозной заводской VIN-подобный идентификатор детали.
* **Как работает:**
  * Поля: `prefix`, `year`, `sequence_id`, `is_active`.
  * `generate_code()`: формирует строковый штрих-код вида `PST-2026-000042`.
  * `validate_format(code)`: проверяет соответствие кода маске префикса и года выпуска.
  * `deactivate()`: выводит серийный номер из оборота (например, при утилизации или браке).
* **Связи:** Входит в состав каждого экземпляра [`AutoPart`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/AutoPart.py).

### 1.4. `Address`
* **Файл:** [`plant/core/Address.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/core/Address.py)
* **Что делает:** Хранит почтовые и географические реквизиты объектов (завода, складов, дилеров).
* **Как работает:**
  * Поля: `country`, `city`, `street`, `postal_code`.
  * `format_full_address()`: формирует единую строку адреса для товаросопроводительных документов.
  * `is_domestic(home_country)`: проверяет, является ли контрагент внутренним или экспортным.
* **Связи:** Используется складами [`MaterialWarehouse`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/MaterialWarehouse.py) и клиентами [`Customer`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/logistics/Customer.py).

### 1.5. `ContactInfo`
* **Файл:** [`plant/core/ContactInfo.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/core/ContactInfo.py)
* **Что делает:** Инкапсулирует каналы связи сотрудника или юридического лица.
* **Как работает:**
  * Поля: `email`, `phone_number`, `department`.
  * `validate_contact()`: проверяет наличие символов `@` и длину телефона.
  * `format_vcard()`: экспортирует визитную карточку.
* **Связи:** Агрегируется классами [`Employee`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/Employee.py), [`MaterialSupplier`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/MaterialSupplier.py), [`Customer`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/logistics/Customer.py).

### 1.6. `QualityStandard`
* **Файл:** [`plant/core/QualityStandard.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/core/QualityStandard.py)
* **Что делает:** Описывает нормативные требования отраслевого стандарта (например, IATF 16949 или ISO 9001).
* **Как работает:**
  * Поля: `standard_name`, `version`, `max_tolerance_deviation`, `min_tensile_threshold`.
  * `audit_dimension(dev)`: сверяет фактическое отклонение размера с порогом стандарта.
  * `audit_strength(strength)`: контролирует соответствие прочностным нормам автопрома.
  * `is_automotive_certified()`: подтверждает принадлежность стандарта к автомобильной индустрии.
* **Связи:** Нормативный базис для ОТК и спецификаций.

### 1.7. `ManufacturingProcess`
* **Файл:** [`plant/core/ManufacturingProcess.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/core/ManufacturingProcess.py)
* **Что делает:** Моделирует технологическую операцию (мехобработка, штамповка, закалка, покраска).
* **Как работает:**
  * Поля: `process_name`, `duration_minutes`, `energy_consumption_kwh`, `required_temperature`.
  * `calculate_power_cost(tariff)`: рассчитывает затраты на электроэнергию по тарифу за кВт·ч.
  * `optimize_duration(pct)`: снижает время такта при внедрении бережливого производства.
  * `is_thermal_process()`: проверяет, требует ли операция нагрева свыше 100 °C.
* **Связи:** Назначается рабочим постам [`WorkStation`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/production/WorkStation.py).

### 1.8. `EnergyMeter`
* **Файл:** [`plant/core/EnergyMeter.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/core/EnergyMeter.py)
* **Что делает:** Учитывает расход электрической энергии на технологических участках завода.
* **Как работает:**
  * Поля: `meter_id`, `total_kwh`, `tariff_per_kwh`.
  * `record_consumption(kwh)`: накапливает суммарное энергопотребление оборудования.
  * `calculate_energy_bill()`: возвращает денежную сумму за потребленные киловатт-часы.
  * `reset_monthly_counter()`: сбрасывает счетчик в начале нового расчетного периода.
* **Связи:** Интегрирован в производственные цеха и линии завода.

---

## 2. Сырье, материалы и складское хозяйство (`plant/materials/`)

### 2.1. `RawMaterial`
* **Файл:** [`plant/materials/RawMaterial.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/RawMaterial.py)
* **Что делает:** Базовый класс для видов промышленного сырья (металл, пластик, резина, химикаты).
* **Как работает:**
  * Поля: `material_id`, `name`, `density_g_cm3`, `base_cost_per_kg`.
  * `estimate_mass_kg(volume_cm3)`: вычисляет вес заготовки по ее объему и плотности.
  * `calculate_volume_cost(volume_cm3)`: определяет себестоимость материала на одну деталь.
* **Связи:** Служит основой для слитков [`AlloyIngot`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/AlloyIngot.py), листов [`MetalSheet`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/MetalSheet.py) и партий [`MaterialBatch`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/MaterialBatch.py).

### 2.2. `MetalSheet`
* **Файл:** [`plant/materials/MetalSheet.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/MetalSheet.py)
* **Что делает:** Листовой прокат для вырубки кузовных элементов и штампованных рычагов подвески.
* **Как работает:**
  * Поля: `sheet_id`, `steel_grade`, `thickness_mm`, `is_galvanized`, `raw_material`.
  * `calculate_sheet_mass(area_m2)`: вычисляет массу листа заданной площади.
  * `check_formability()`: определяет возможность глубокой вытяжки на прессе.
  * `apply_galvanizing()`: наносит защитный слой цинкования против коррозии.
* **Связи:** Агрегирует [`RawMaterial`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/RawMaterial.py); подается в штамповочные прессы [`StampingPress`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/StampingPress.py).

### 2.3. `AlloyIngot`
* **Файл:** [`plant/materials/AlloyIngot.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/AlloyIngot.py)
* **Что делает:** Чушка алюминиевого или чугунного сплава для литья поршней ДВС и тормозных дисков.
* **Как работает:**
  * Поля: `ingot_id`, `alloy_composition`, `weight_kg`, `melting_temperature_c`, `raw_material`.
  * `check_furnace_compatibility(max_temp)`: проверяет, способна ли плавильная печь расплавить данный сплав.
  * `calculate_casting_yield(loss_pct)`: рассчитывает чистый выход годного литья с учетом угара.
  * `is_high_temp_alloy()`: проверяет, относится ли сплав к жаропрочным (>1000 °C).
* **Связи:** Агрегирует [`RawMaterial`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/RawMaterial.py); плавится в печах [`HeatTreatmentFurnace`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/HeatTreatmentFurnace.py).

### 2.4. `RubberCompound`
* **Файл:** [`plant/materials/RubberCompound.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/RubberCompound.py)
* **Что делает:** Сырая резиновая смесь для вулканизации сайлентблоков подвески, пыльников и уплотнителей.
* **Как работает:**
  * Поля: `compound_id`, `shore_hardness`, `cure_time_minutes`, `is_vulcanized`.
  * `validate_hardness(min_val, max_val)`: проверяет твердость по Шору А.
  * `simulate_vulcanization(temp_c)`: симулирует процесс горячей вулканизации при температуре $\ge 140$ °C.
  * `is_ready_for_assembly()`: проверяет готовность резинометаллического шарнира к запрессовке в рычаг.
* **Связи:** Комплектует рычаги подвески [`ControlArm`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/ControlArm.py).

### 2.5. `PlasticPellet`
* **Файл:** [`plant/materials/PlasticPellet.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/PlasticPellet.py)
* **Что делает:** Полимерные гранулы (полиамид PA66, полипропилен) для термопластавтоматов и коллекторов.
* **Как работает:**
  * Поля: `pellet_id`, `polymer_type`, `melt_flow_index`, `moisture_pct`.
  * `requires_drying()`: определяет, превышает ли влажность сырья технологический норматив (0.2%).
  * `perform_drying(hours)`: сушит гранулят в бункере; при нарушении регламента выбрасывает [`MaterialDefectException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/MaterialDefectException.py).
  * `is_suitable_for_injection()`: оценивает показатель текучести расплава (ПТР/MFI).
* **Связи:** Выбрасывает [`MaterialDefectException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/MaterialDefectException.py).

### 2.6. `ChemicalCoolant`
* **Файл:** [`plant/materials/ChemicalCoolant.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/ChemicalCoolant.py)
* **Что делает:** Смазочно-охлаждающая жидкость (СОЖ) для фрезерных центров ЧПУ.
* **Как работает:**
  * Поля: `coolant_id`, `concentration_pct`, `ph_level`, `is_contaminated`.
  * `is_within_ph_limits()`: контролирует кислотно-щелочной баланс (норма pH 8.5–9.5) против коррозии станка.
  * `dilute_with_water(liters)`: корректирует концентрацию эмульсии.
  * `replace_fluid()`: сливает отработанную СОЖ и сбрасывает флаг загрязнения.
* **Связи:** Заливается в контур охлаждения фрезерного станка [`CncMillingMachine`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/CncMillingMachine.py).

### 2.7. `MaterialBatch`
* **Файл:** [`plant/materials/MaterialBatch.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/MaterialBatch.py)
* **Что делает:** Управляет партией сырья одного наименования, поступившей на завод по накладной.
* **Как работает:**
  * Поля: `batch_id`, `raw_material`, `quantity_kg`, `received_date`, `is_inspected`.
  * `consume_material(amount_kg)`: списывает металл на производство. При нехватке выбрасывает [`RawMaterialShortageException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/RawMaterialShortageException.py).
  * `approve_inspection()`: ставит отметку о прохождении входного контроля лаборатории.
  * `calculate_total_value()`: перемножает остаток массы на удельную стоимость килограмма.
* **Связи:** Агрегирует [`RawMaterial`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/RawMaterial.py); выбрасывает [`RawMaterialShortageException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/RawMaterialShortageException.py).

### 2.8. `StorageBin`
* **Файл:** [`plant/materials/StorageBin.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/StorageBin.py)
* **Что делает:** Адресная ячейка стеллажа или складской напольный бункер.
* **Как работает:**
  * Поля: `bin_code`, `max_weight_capacity_kg`, `current_weight_kg`, `is_locked`.
  * `deposit_material(weight_kg)`: загружает сырье. При превышении грузоподъемности ячейки выбрасывает [`StorageExhaustedException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/StorageExhaustedException.py).
  * `withdraw_material(weight_kg)`: выдает сырье на рабочий пост.
  * `get_occupancy_ratio()`: возвращает процент текущего заполнения ячейки.
* **Связи:** Входит в состав [`MaterialWarehouse`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/MaterialWarehouse.py); выбрасывает [`StorageExhaustedException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/StorageExhaustedException.py).

### 2.9. `MaterialWarehouse`
* **Файл:** [`plant/materials/MaterialWarehouse.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/MaterialWarehouse.py)
* **Что делает:** Центральный склад металлов, полимеров и комплектующих завода.
* **Как работает:**
  * Поля: `warehouse_id`, `address`, `total_capacity_tons`, `storage_bins`.
  * `add_bin(bin_obj)`: регистрирует новую адресную ячейку хранения.
  * `find_available_bin(required_kg)`: ищет незаблокированную ячейку с достаточным запасом грузоподъемности.
  * `calculate_total_stored_weight()`: суммирует фактическую массу всех хранящихся материалов.
* **Связи:** Агрегирует [`Address`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/core/Address.py) и список [`StorageBin`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/StorageBin.py); подчиняется комплексу [`AutomotivePlant`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/enterprise/AutomotivePlant.py).

### 2.10. `MaterialSupplier`
* **Файл:** [`plant/materials/MaterialSupplier.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/MaterialSupplier.py)
* **Что делает:** Внешний поставщик сырья (металлургический комбинат, нефтехимический завод).
* **Как работает:**
  * Поля: `supplier_id`, `company_name`, `contact_info`, `rating`.
  * `update_rating(delta)`: корректирует индекс надежности поставщика по результатам поставок.
  * `is_certified_vendor()`: проверяет, превышает ли рейтинг планку допуска к конвейеру (рейтинг $\ge 4.0$).
  * `send_quality_claim(description)`: формирует официальную претензию по качеству бракованного сырья.
* **Связи:** Агрегирует [`ContactInfo`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/core/ContactInfo.py).

---

## 3. Станочный парк и промышленное оборудование (`plant/equipment/`)

### 3.1. `Machine`
* **Файл:** [`plant/equipment/Machine.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/Machine.py)
* **Что делает:** Базовый класс технологического оборудования цеха.
* **Как работает:**
  * Поля: `machine_id`, `model`, `operating_hours`, `is_operational`, `current_temperature`, `max_allowed_temp`.
  * `start()` / `stop()`: переключает рабочий статус станка.
  * `record_hours(hours)`: накапливает наработку моточасов и повышает рабочую температуру.
  * `check_overheat()`: контролирует тепловой режим; при перегреве выбрасывает [`EquipmentOverheatException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/EquipmentOverheatException.py).
* **Связи:** Базовый класс для прессов, ЧПУ, печей, роботов; выбрасывает [`EquipmentOverheatException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/EquipmentOverheatException.py) и [`MachineMalfunctionException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/MachineMalfunctionException.py).

### 3.2. `ToolingFixture`
* **Файл:** [`plant/equipment/ToolingFixture.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/ToolingFixture.py)
* **Что делает:** Формообразующая оснастка: штампы вырубки, пресс-формы литья под давлением.
* **Как работает:**
  * Поля: `fixture_id`, `fixture_type`, `max_cycles_lifetime`, `cycles_used`, `is_worn_out`.
  * `increment_cycles(count)`: считает количество выполненных ударов/смыканий. При исчерпании ресурса выбрасывает [`ToolWearExceededException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/ToolWearExceededException.py).
  * `refurbish()`: отправляет штамп инструментальщику на перешлифовку и восстанавливает счетчик.
  * `get_wear_ratio()`: возвращает процент выработанного ресурса матрицы.
* **Связи:** Устанавливается на [`StampingPress`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/StampingPress.py); обслуживается [`Toolmaker`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/Toolmaker.py); выбрасывает [`ToolWearExceededException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/ToolWearExceededException.py).

### 3.3. `CuttingTool`
* **Файл:** [`plant/equipment/CuttingTool.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/CuttingTool.py)
* **Что делает:** Металлорежущий инструмент: твердосплавные фрезы, резцы, сверла для ЧПУ.
* **Как работает:**
  * Поля: `tool_id`, `tool_material`, `flank_wear_mm`, `max_wear_limit_mm`, `is_sharp`.
  * `apply_cut_wear(wear_mm)`: прибавляет износ по задней грани резца; при превышении лимита притупляет инструмент и выбрасывает [`ToolWearExceededException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/ToolWearExceededException.py).
  * `regrind()`: производит переточку лезвия на заточном станке.
  * `is_usable()`: проверяет остроту режущей кромки.
* **Связи:** Закрепляется в шпинделе [`CncMillingMachine`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/CncMillingMachine.py); затачивается [`Toolmaker`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/Toolmaker.py).

### 3.4. `StampingPress`
* **Файл:** [`plant/equipment/StampingPress.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/StampingPress.py)
* **Что делает:** Кривошипный или гидравлический пресс для холодной и горячей штамповки автодеталей.
* **Как работает:**
  * Поля: `machine`, `press_tonnage`, `stroke_length_mm`, `tooling_fixture`, `parts_stamped`.
  * `install_die(fixture)`: устанавливает штамповую оснастку в рабочую зону.
  * `execute_stroke()`: совершает рабочий ход ползуна с деформацией заготовки. При отказе станка выбрасывает [`MachineMalfunctionException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/MachineMalfunctionException.py).
  * `calibrate_pressure(target_tons)`: настраивает усилие смыкания плит.
* **Связи:** Композирует [`Machine`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/Machine.py), агрегирует [`ToolingFixture`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/ToolingFixture.py).

### 3.5. `CncMillingMachine`
* **Файл:** [`plant/equipment/CncMillingMachine.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/CncMillingMachine.py)
* **Что делает:** Высокоточный 5-осевой фрезерный обрабатывающий центр с ЧПУ.
* **Как работает:**
  * Поля: `machine`, `axis_count`, `spindle_rpm`, `active_tool`, `coolant_pump_active`.
  * `mount_tool(tool)`: устанавливает инструмент из магазина в шпиндель.
  * `mill_contour(depth_mm)`: выполняет выборку металла по управляющей программе G-кода; увеличивает износ фрезы.
  * `set_spindle_speed(rpm)`: регулирует обороты шпинделя (до 24 000 об/мин).
* **Связи:** Агрегирует [`Machine`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/Machine.py) и [`CuttingTool`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/CuttingTool.py).

### 3.6. `WeldingRobot`
* **Файл:** [`plant/equipment/WeldingRobot.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/WeldingRobot.py)
* **Что делает:** Промышленный робот-манипулятор для дуговой и точечной сварки узлов шасси и кузова.
* **Как работает:**
  * Поля: `machine`, `welding_wire_type`, `gas_flow_rate_lpm`, `current_amperage`, `arc_ignited`.
  * `ignite_arc()`: зажигает сварочную дугу в среде защитного газа (Ar/CO2).
  * `extinguish_arc()`: гасит дугу с продувкой шва газом.
  * `perform_seam_weld(length_cm)`: накладывает неразъемный сварочный шов заданной длины.
* **Связи:** Композирует [`Machine`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/Machine.py); сваривает элементы [`ControlArm`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/ControlArm.py).

### 3.7. `PaintingBooth`
* **Файл:** [`plant/equipment/PaintingBooth.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/PaintingBooth.py)
* **Что делает:** Окрасочно-сушильная камера с электростатическим распылением катафорезных грунтов и эмалей.
* **Как работает:**
  * Поля: `machine`, `paint_type`, `chamber_humidity_pct`, `airflow_speed_mps`, `electrostatic_charge_kv`.
  * `apply_powder_coat(microns)`: наносит равномерный порошковый слой на металл.
  * `bake_paint(temp_c, minutes)`: запускает полимеризацию лакокрасочного покрытия при температуре 180 °C.
  * `ventilate()`: очищает воздух камеры мощными приточно-вытяжными фильтрами.
* **Связи:** Композирует [`Machine`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/Machine.py).

### 3.8. `HeatTreatmentFurnace`
* **Файл:** [`plant/equipment/HeatTreatmentFurnace.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/HeatTreatmentFurnace.py)
* **Что делает:** Термическая печь для закалки, цементации и нормализации валов трансмиссии и шестерен.
* **Как работает:**
  * Поля: `machine`, `target_temp_celsius`, `quench_medium`, `holding_time_minutes`, `is_heating`.
  * `heat_to_target(temp)`: разогревает рабочее пространство печи (до 1100 °C).
  * `quench()`: производит резкое охлаждение садки в масле, воде или полимере.
  * `perform_hardening_cycle()`: выполняет полный термоцикл закалки и отпуска для придания твердости.
* **Связи:** Композирует [`Machine`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/Machine.py); упрочняет валы [`GearboxShaft`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/GearboxShaft.py).

### 3.9. `LaserCutter`
* **Файл:** [`plant/equipment/LaserCutter.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/LaserCutter.py)
* **Что делает:** Оптоволоконный лазерный комплекс для прецизионного фигурного раскроя листового проката.
* **Как работает:**
  * Поля: `machine`, `laser_power_watts`, `assist_gas`, `cutting_speed_m_per_min`, `beam_focused`.
  * `focus_beam()`: производит юстировку оптической линзы в фокусное пятно.
  * `cut_sheet_profile(contour_length_m)`: выполняет лазерный раскрой заготовки по вектору.
  * `set_power(watts)`: настраивает излучаемую мощность лазерного генератора.
* **Связи:** Композирует [`Machine`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/Machine.py); кроит [`MetalSheet`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/MetalSheet.py).

### 3.10. `EquipmentSensor`
* **Файл:** [`plant/equipment/EquipmentSensor.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/EquipmentSensor.py)
* **Что делает:** Телеметрический датчик вибродиагностики, давления масла или температуры подшипников станка.
* **Как работает:**
  * Поля: `sensor_id`, `machine`, `metric_name`, `alert_threshold`, `last_reading`.
  * `read_value()`: опрашивает аналоговый сигнал с контроллера оборудования.
  * `is_threshold_exceeded()`: детектирует выход параметров за аварийные границы (предаварийное состояние).
  * `calibrate_offset(offset)`: корректирует нуль шкалы измерения датчика.
* **Связи:** Устанавливается на агрегаты [`Machine`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/Machine.py).

### 3.11. `MaintenanceLog`
* **Файл:** [`plant/equipment/MaintenanceLog.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/MaintenanceLog.py)
* **Что делает:** Электронный журнал технического обслуживания, замены масла и аварийных ремонтов оборудования.
* **Как работает:**
  * Поля: `log_id`, `machine`, `technician_name`, `description`, `maintenance_date`.
  * `log_service_event(entry)`: добавляет новую сервисную запись в карту станка.
  * `is_recent_service(days_limit)`: проверяет свежесть проведения последнего планового ТО.
  * `format_entry()`: выгружает форматированную запись для аудиторов стандарта IATF.
* **Связи:** Привязан к конкретному станку [`Machine`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/Machine.py).

---

## 4. Персонал и управление сменами (`plant/personnel/`)

### 4.1. `Employee`
* **Файл:** [`plant/personnel/Employee.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/Employee.py)
* **Что делает:** Базовая штатная единица завода (табельный номер, ФИО, должность, базовый оклад).
* **Как работает:**
  * Поля: `employee_id`, `full_name`, `position`, `salary`, `contact_info`.
  * `calculate_annual_bonus(kpi)`: начисляет годовую премию пропорционально коэффициенту трудового участия.
  * `promote(new_position, salary_raise)`: переводит сотрудника на новую должность с повышением оклада.
  * `is_management()`: определяет принадлежность сотрудника к руководящему звену цеха или завода.
* **Связи:** Агрегирует [`ContactInfo`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/core/ContactInfo.py); композируется всеми рабочими и инженерными специальностями.

### 4.2. `MachineOperator`
* **Файл:** [`plant/personnel/MachineOperator.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/MachineOperator.py)
* **Что делает:** Станочник/оператор технологического оборудования с квалификационным разрядом.
* **Как работает:**
  * Поля: `employee`, `qualification_rank`, `safety_certified`, `assigned_machine`.
  * `assign_machine(machine)`: закрепляет оператора за конкретным станком.
  * `pass_safety_exam()`: подтверждает прохождение ежегодного инструктажа по ТБ.
  * `produce_units(count)`: выполняет операцию выпуска партии; при отсутствии допуска по ТБ выбрасывает [`SafetyViolationException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/SafetyViolationException.py).
* **Связи:** Композирует [`Employee`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/Employee.py), управляет [`Machine`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/Machine.py); выбрасывает [`SafetyViolationException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/SafetyViolationException.py).

### 4.3. `QualityInspector`
* **Файл:** [`plant/personnel/QualityInspector.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/QualityInspector.py)
* **Что делает:** Контролер отдела технического контроля (ОТК), аттестованный по методикам неразрушающего контроля.
* **Как работает:**
  * Поля: `employee`, `inspector_badge_id`, `certified_standards`, `inspections_count`.
  * `inspect_part(part)`: проверяет соответствие детали геометрическим и прочностным допускам.
  * `add_certification(standard)`: добавляет открытый допуск на проверку ответственных узлов (например, тормозов).
  * `get_rejection_rate(total_rejected)`: вычисляет персональный процент выявленного инспектором брака.
* **Связи:** Композирует [`Employee`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/Employee.py); подписывает отчеты [`InspectionReport`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/quality/InspectionReport.py) и [`DefectReport`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/quality/DefectReport.py).

### 4.4. `MaintenanceEngineer`
* **Файл:** [`plant/personnel/MaintenanceEngineer.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/MaintenanceEngineer.py)
* **Что делает:** Инженер-механик/электроник службы главного механика цеха.
* **Как работает:**
  * Поля: `employee`, `certification_level`, `repairs_performed`, `active_repair_machine`.
  * `perform_preventive_maintenance(machine)`: проводит планово-предупредительный ремонт (ППР) станка.
  * `repair_breakdown(machine)`: устраняет поломку оборудования и возвращает статус работоспособности `is_operational = True`.
  * `is_expert()`: подтверждает высшую категорию допуска к наладке сложных станков ЧПУ.
* **Связи:** Композирует [`Employee`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/Employee.py), чинит агрегаты [`Machine`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/Machine.py).

### 4.5. `Toolmaker`
* **Файл:** [`plant/personnel/Toolmaker.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/Toolmaker.py)
* **Что делает:** Высококвалифицированный слесарь-инструментальщик инструментального цеха.
* **Как работает:**
  * Поля: `employee`, `specialty`, `refurbished_tools_count`, `precision_tolerance_mm`.
  * `regrind_cutting_tool(tool)`: восстанавливает режущие кромки изношенных резцов и фрез.
  * `refurbish_die(fixture)`: производит подгонку, полировку и доводку штампов пресса.
  * `verify_die_precision(fixture)`: замеряет зазоры между пуансоном и матрицей штампа.
* **Связи:** Композирует [`Employee`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/Employee.py); взаимодействует с [`CuttingTool`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/CuttingTool.py) и [`ToolingFixture`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/ToolingFixture.py).

### 4.6. `SafetyOfficer`
* **Файл:** [`plant/personnel/SafetyOfficer.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/SafetyOfficer.py)
* **Что делает:** Инженер по охране труда, промышленной и пожарной безопасности завода.
* **Как работает:**
  * Поля: `employee`, `inspections_conducted`, `violations_reported`, `safety_policy_version`.
  * `conduct_line_audit(line)`: инспектирует производственную линию на предмет наличия защитных экранов и исправности концевиков.
  * `issue_violation(violator_name, reason)`: фиксирует нарушение регламентов безопасности; может выбросить [`SafetyViolationException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/SafetyViolationException.py).
  * `update_policy(new_version)`: утверждает актуализированные инструкции по ТБ.
* **Связи:** Композирует [`Employee`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/Employee.py); выбрасывает [`SafetyViolationException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/SafetyViolationException.py).

### 4.7. `ShiftSupervisor`
* **Файл:** [`plant/personnel/ShiftSupervisor.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/ShiftSupervisor.py)
* **Что делает:** Сменный мастер цеха, распределяющий рабочих по станкам и отвечающий за сменное задание.
* **Как работает:**
  * Поля: `employee`, `shift_code`, `team_size`, `active_shift_running`.
  * `start_shift()` / `end_shift()`: открывает и закрывает смену, контролируя явку рабочих.
  * `reassign_operator(operator, machine)`: оперативно переставляет оператора на другой пост при аврале или замене.
* **Связи:** Композирует [`Employee`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/Employee.py); руководит операторами [`MachineOperator`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/MachineOperator.py) и станками [`Machine`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/Machine.py).

### 4.8. `PlantDirector`
* **Файл:** [`plant/personnel/PlantDirector.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/PlantDirector.py)
* **Что делает:** Генеральный директор предприятия, распорядитель инвестиционного бюджета и подписи.
* **Как работает:**
  * Поля: `employee`, `annual_budget`, `approved_projects`, `strategic_plan_name`.
  * `approve_budget_expense(amount)`: списывает денежные средства на закупку оборудования и сырья из годового бюджета.
  * `authorize_line_expansion(line_name)`: подписывает приказ о запуске новой производственной ветки завода.
  * `sign_annual_report()`: утверждает годовой финансово-производственный отчет завода.
* **Связи:** Композирует [`Employee`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/Employee.py); руководит предприятием [`AutomotivePlant`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/enterprise/AutomotivePlant.py).

---

## 5. Производственный цикл и оперативное планирование (`plant/production/`)

### 5.1. `WorkStation`
* **Файл:** [`plant/production/WorkStation.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/production/WorkStation.py)
* **Что делает:** Первичная производственная ячейка: станок + прикрепленный аттестованный оператор.
* **Как работает:**
  * Поля: `station_id`, `machine`, `operator`, `is_active`.
  * `assign_operator(operator)`: ставит станочника на пост и активирует рабочее место (`is_active = True`).
  * `release_station()`: снимает оператора со смены, деактивируя пост.
  * `process_part_cycle()`: выполняет один цикл изготовления детали; возвращает `False`, если станок сломан или оператор отсутствует.
* **Связи:** Связывает [`Machine`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/Machine.py) и [`MachineOperator`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/MachineOperator.py); входит в состав [`ProductionLine`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/production/ProductionLine.py).

### 5.2. `ProductionLine`
* **Файл:** [`plant/production/ProductionLine.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/production/ProductionLine.py)
* **Что делает:** Непрерывная конвейерная линия, объединяющая последовательность постов в единый поток.
* **Как работает:**
  * Поля: `line_id`, `line_name`, `stations`, `is_running`, `max_allowed_scrap_pct`, `scrap_rate`.
  * `add_station(station)` / `remove_station(station_id)`: конфигурирует посты на линии.
  * `start_line()` / `stop_line()`: пуск/останов линии; при попытке запуска неисправного оборудования выбрасывает [`ProductionLineHaltException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/ProductionLineHaltException.py).
  * `resume_line()`: сбрасывает флаг аварии и перезапускает линию.
  * `emergency_halt(reason)`: экстренное торможение конвейера защитной автоматикой.
  * `record_scrap(scrapped, total)`: регистрирует процент брака; при превышении нормы стандарта выбрасывает [`DefectThresholdExceededException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/DefectThresholdExceededException.py).
* **Связи:** Агрегирует список [`WorkStation`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/production/WorkStation.py); выбрасывает [`ProductionLineHaltException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/ProductionLineHaltException.py) и [`DefectThresholdExceededException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/DefectThresholdExceededException.py).

### 5.3. `WorkShift`
* **Файл:** [`plant/production/WorkShift.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/production/WorkShift.py)
* **Что делает:** Моделирует производственную рабочую смену (дневная, вечерняя, ночная).
* **Как работает:**
  * Поля: `shift_id`, `shift_type`, `supervisor`, `hours_duration`.
  * `record_shift_output(parts_count)`: фиксирует валовый выпуск готовых изделий за смену.
  * `calculate_hourly_productivity(total_parts)`: вычисляет часовую производительность труда смены.
  * `is_night_shift()`: проверяет, является ли смена ночной (для начисления надбавок).
* **Связи:** Руководится сменным мастером [`ShiftSupervisor`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/ShiftSupervisor.py).

### 5.4. `ProductionPlan`
* **Файл:** [`plant/production/ProductionPlan.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/production/ProductionPlan.py)
* **Что делает:** Оперативно-календарный план выпуска партии деталей на месяц/квартал.
* **Как работает:**
  * Поля: `plan_id`, `planned_quantity`, `completed_quantity`, `deadline_date`.
  * `register_output(count)`: прибавляет выпущенные детали к прогрессу плана.
  * `calculate_fulfillment_percentage()`: рассчитывает текущий процент выполнения плана.
  * `is_plan_fulfilled()`: возвращает `True`, когда факт выпуска сравнялся или превысил план.
* **Связи:** Включается в производственный наряд [`ProductionOrder`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/production/ProductionOrder.py).

### 5.5. `ProductionOrder`
* **Файл:** [`plant/production/ProductionOrder.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/production/ProductionOrder.py)
* **Что делает:** Заводской наряд-заказ цеху на изготовление номенклатурной партии деталей.
* **Как работает:**
  * Поля: `order_id`, `target_part_type`, `quantity`, `status`, `production_plan`.
  * `link_plan(plan)`: связывает наряд с утвержденным планом; при превышении производственных лимитов цеха выбрасывает [`OrderCapacityExceededException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/OrderCapacityExceededException.py).
  * `start_production()`: переводит наряд в статус `В ПРОИЗВОДСТВЕ`.
  * `complete_order()`: переводит наряд в статус `ВЫПОЛНЕН` и сдает партию на склад.
* **Связи:** Агрегирует [`ProductionPlan`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/production/ProductionPlan.py); выбрасывает [`OrderCapacityExceededException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/OrderCapacityExceededException.py).

### 5.6. `ScrapRecord`
* **Файл:** [`plant/production/ScrapRecord.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/production/ScrapRecord.py)
* **Что делает:** Ведомость списания технологического брака (неисправимый брак литья, бой штамповки).
* **Как работает:**
  * Поля: `record_id`, `scrapped_quantity`, `defect_reason`, `registered_date`.
  * `calculate_financial_loss(unit_cost)`: подсчитывает прямые финансовые убытки от брака.
  * `is_critical_scrap(threshold)`: проверяет, не превысил ли единовременный брак допустимую критическую планку.
  * `format_summary()`: формирует строку бухгалтерского отчета о списании.
* **Связи:** Оформляется при отбраковке деталей на производственных линиях.

---

## 6. Автомобильные детали и компоненты (`plant/parts/`)

### 6.1. `AutoPart`
* **Файл:** [`plant/parts/AutoPart.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/AutoPart.py)
* **Что делает:** Базовая автомобильная запчасть: хранит размеры, серийный номер, технические условия и флаг годности.
* **Как работает:**
  * Поля: `part_number`, `part_name`, `dimension`, `spec`, `serial_number`, `is_defect_free`.
  * `verify_dimensions(reference_dim)`: сверяет геометрию детали с эталоном чертежа; при выходе из поля допуска помечает деталь бракованной и выбрасывает [`QualityCheckFailedException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/QualityCheckFailedException.py).
  * `mark_as_defective(reason)`: переводит флаг `is_defect_free` в `False`.
  * `get_part_label()`: возвращает читаемую бирку с названием, шифром и уникальным номером.
* **Связи:** Композирует [`Dimension`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/core/Dimension.py), [`TechnicalSpecification`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/core/TechnicalSpecification.py), [`SerialNumber`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/core/SerialNumber.py); выбрасывает [`QualityCheckFailedException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/QualityCheckFailedException.py); является базой для всех 7 конкретных автозапчастей.

### 6.2. `EnginePiston`
* **Файл:** [`plant/parts/EnginePiston.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/EnginePiston.py)
* **Что делает:** Поршень двигателя внутреннего сгорания с антифрикционной юбкой и канавками под кольца.
* **Как работает:**
  * Поля: `auto_part`, `piston_diameter_mm`, `compression_height_mm`, `ring_groove_count`, `coating_type`.
  * `check_bore_clearance(cylinder_bore)`: вычисляет тепловой монтажный зазор между юбкой поршня и гильзой цилиндра (норма 0.03–0.06 мм).
  * `calculate_thermal_expansion(temp_delta)`: моделирует тепловое расширение алюминиевого сплава при нагреве до 300 °C.
  * `is_forged()`: определяет технологию изготовления (кованый спортивный или литой серийный).
* **Связи:** Агрегирует базовый [`AutoPart`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/AutoPart.py).

### 6.3. `BrakeDisc`
* **Файл:** [`plant/parts/BrakeDisc.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/BrakeDisc.py)
* **Что делает:** Вентилируемый чугунный тормозной диск дисковой тормозной системы.
* **Как работает:**
  * Поля: `auto_part`, `disc_thickness_mm`, `min_thickness_limit_mm`, `runout_microns`, `is_ventilated`.
  * `check_wear_limit()`: сравнивает текущую толщину рабочего полотна с минимально допустимым порогом безопасности.
  * `verify_axial_runout(max_allowed_microns)`: контролирует торцевое биение диска (не более 30 микрон для исключения вибраций на педали).
  * `simulate_braking_cycle(friction_energy_kj)`: вычисляет нагрев диска при экстренном торможении с рассеиванием кинетической энергии.
* **Связи:** Агрегирует [`AutoPart`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/AutoPart.py).

### 6.4. `ShockAbsorber`
* **Файл:** [`plant/parts/ShockAbsorber.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/ShockAbsorber.py)
* **Что делает:** Гидравлическая или газонаполненная стойка амортизатора подвески автомобиля.
* **Как работает:**
  * Поля: `auto_part`, `stroke_length_mm`, `damping_force_n`, `gas_pressure_bar`, `is_pressurized`.
  * `test_damping_performance(compression_speed)`: рассчитывает динамическое усилие сопротивления отбоя и сжатия штока.
  * `recharge_gas(pressure_bar)`: закачивает азот в компенсационную камеру двухтрубного амортизатора.
  * `is_leak_free()`: проверяет герметичность штокового сальника высокого давления.
* **Связи:** Агрегирует [`AutoPart`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/AutoPart.py).

### 6.5. `GearboxShaft`
* **Файл:** [`plant/parts/GearboxShaft.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/GearboxShaft.py)
* **Что делает:** Первичный/вторичный шлицевой вал коробки передач с шестернями.
* **Как работает:**
  * Поля: `auto_part`, `gear_teeth_count`, `surface_hardness_hrc`, `spline_count`, `is_hardened`.
  * `validate_hardness(min_hrc)`: проверяет поверхностную твердость зубьев после ТВЧ-закалки (норма 58–62 HRC).
  * `calculate_gear_ratio(paired_teeth)`: вычисляет передаточное число зубчатой пары.
  * `verify_spline_mesh(mating_spline_count)`: контролирует совпадение числа шлицев при посадке на ведомую муфту.
* **Связи:** Агрегирует [`AutoPart`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/AutoPart.py); проверяется твердомером [`HardnessTester`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/quality/HardnessTester.py).

### 6.6. `FuelInjector`
* **Файл:** [`plant/parts/FuelInjector.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/FuelInjector.py)
* **Что делает:** Электромагнитная топливная форсунка непосредственного впрыска топлива высокого давления (GDI).
* **Как работает:**
  * Поля: `auto_part`, `flow_rate_cc_min`, `spray_angle_deg`, `operating_pressure_bar`, `nozzle_holes_count`.
  * `test_spray_pattern(expected_angle)`: проверяет геометрию факела распыла бензина/дизеля.
  * `calculate_fuel_delivery(pulse_width_ms)`: определяет миллиграммы топлива, поданные за один микросекундный импульс открытия иглы.
  * `is_high_pressure_gdi()`: определяет применимость для прямого впрыска в цилиндр (давление свыше 150 бар).
* **Связи:** Агрегирует [`AutoPart`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/AutoPart.py).

### 6.7. `ControlArm`
* **Файл:** [`plant/parts/ControlArm.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/ControlArm.py)
* **Что делает:** А-образный нижний рычаг независимой передней подвески типа МакФерсон.
* **Как работает:**
  * Поля: `auto_part`, `bushing_count`, `ball_joint_fitted`, `is_aluminum`, `load_rating_kn`.
  * `test_structural_strength(applied_kn)`: моделирует ударную нагрузку от ямы на дороге; проверяет запас прочности на изгиб.
  * `install_ball_joint()`: устанавливает запрессованную шаровую опору в поворотную проушину.
  * `is_complete_subassembly()`: проверяет полную комплектность узла (шаровая + 2 сайлентблока) перед отправкой на автосборочный конвейер.
* **Связи:** Агрегирует [`AutoPart`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/AutoPart.py); сваривается роботом [`WeldingRobot`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/equipment/WeldingRobot.py).

### 6.8. `ExhaustManifold`
* **Файл:** [`plant/parts/ExhaustManifold.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/ExhaustManifold.py)
* **Что делает:** Чугунный или стальной выпускной коллектор системы выпуска отработавших газов.
* **Как работает:**
  * Поля: `auto_part`, `runner_count`, `wall_thickness_mm`, `max_operating_temp_c`, `is_leak_tested`.
  * `perform_pressure_leak_test(test_bar)`: проводит опрессовку воздухом в ванне с водой на отсутствие микротрещин литья.
  * `verify_thermal_resistance(gas_temp_c)`: оценивает жаростойкость стенок коллектора при температуре выхлопа до 950 °C.
  * `is_equal_length_runner()`: проверяет равнодлинность выпускных каналов для снижения противодавления газов.
* **Связи:** Агрегирует [`AutoPart`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/AutoPart.py).

---

## 7. Контроль качества, лаборатория ОТК и метрология (`plant/quality/`)

### 7.1. `CalibrationTool`
* **Файл:** [`plant/quality/CalibrationTool.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/quality/CalibrationTool.py)
* **Что делает:** Управляет межповерочными интервалами и свидетельствами о поверке измерительных приборов.
* **Как работает:**
  * Поля: `tool_id`, `tool_name`, `last_calibration_date`, `calibration_interval_days`, `is_calibrated`.
  * `check_calibration_validity(days_elapsed)`: проверяет срок годности поверки; при просрочке выставляет `is_calibrated = False` и выбрасывает [`CalibrationExpiredException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/CalibrationExpiredException.py).
  * `recalibrate()`: ставит отметку о прохождении новой государственной поверки в центре стандартизации.
  * `format_calibration_tag()`: печатает метрологическую бирку для наклеивания на прибор.
* **Связи:** Входит в состав измерительных приборов; выбрасывает [`CalibrationExpiredException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/CalibrationExpiredException.py).

### 7.2. `CmmScanner`
* **Файл:** [`plant/quality/CmmScanner.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/quality/CmmScanner.py)
* **Что делает:** Координатно-измерительная машина (КИМ / CMM) для 3D-оцифровки геометрических параметров детали.
* **Как работает:**
  * Поля: `scanner_id`, `precision_microns`, `calibration_tool`, `points_scanned`.
  * `calibrate()`: проводит автоматическую калибровку рубинового щупа по эталонной сфере.
  * `scan_part_cloud(part)`: производит сканирование облака точек автодетали; при просроченной поверке блокирует сканирование через исключение.
  * `is_high_accuracy()`: проверяет субмикронную точность сенсора (< 2 микрон).
* **Связи:** Агрегирует [`CalibrationTool`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/quality/CalibrationTool.py), сканирует [`AutoPart`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/AutoPart.py), выбрасывает [`CalibrationExpiredException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/CalibrationExpiredException.py).

### 7.3. `TensileTester`
* **Файл:** [`plant/quality/TensileTester.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/quality/TensileTester.py)
* **Что делает:** Разрывная машина для определения пределов текучести и прочности образцов металла.
* **Как работает:**
  * Поля: `tester_id`, `max_force_kn`, `calibration_tool`, `tests_executed`.
  * `calibrate()`: калибрует динамометрический тензодатчик силы.
  * `execute_pull_test(spec, actual_force_kn)`: растягивает образец до разрушения и сопоставляет фактическое усилие с техническими условиями.
  * `get_utilization(target_monthly_tests)`: вычисляет коэффициент загрузки испытательного стенда лаборатории.
* **Связи:** Агрегирует [`CalibrationTool`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/quality/CalibrationTool.py) и [`TechnicalSpecification`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/core/TechnicalSpecification.py).

### 7.4. `HardnessTester`
* **Файл:** [`plant/quality/HardnessTester.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/quality/HardnessTester.py)
* **Что делает:** Стационарный твердомер Роквелла / Бринелля для замера твердости закаленных слоев металла.
* **Как работает:**
  * Поля: `tester_id`, `method_type`, `calibration_tool`, `measurements_count`.
  * `calibrate()`: проверяет точность вдавливания алмазного конуса по эталонным мерам твердости.
  * `measure_hardness(shaft)`: замеряет твердость зубьев вала [`GearboxShaft`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/GearboxShaft.py) и проверяет ее соответствие КД.
  * `is_rockwell_method()`: определяет метод испытания (шкала HRC).
* **Связи:** Агрегирует [`CalibrationTool`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/quality/CalibrationTool.py) и [`GearboxShaft`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/GearboxShaft.py).

### 7.5. `DefectReport`
* **Файл:** [`plant/quality/DefectReport.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/quality/DefectReport.py)
* **Что делает:** Акт о выявлении брака на конкретном экземпляре автодетали (причина, глубина дефекта, решение).
* **Как работает:**
  * Поля: `report_id`, `auto_part`, `inspector`, `defect_description`, `severity_level`.
  * `classify_disposition()`: определяет дальнейшую судьбу изделия (списание в утиль, исправимый брак на переточку или спецдопуск).
  * `is_scrap()`: проверяет, является ли дефект неустранимым браком.
  * `format_ticket()`: генерирует карточку несоответствия по форме 8D.
* **Связи:** Связывает забракованную деталь [`AutoPart`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/AutoPart.py) и инспектора [`QualityInspector`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/QualityInspector.py).

### 7.6. `InspectionReport`
* **Файл:** [`plant/quality/InspectionReport.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/quality/InspectionReport.py)
* **Что делает:** Сводный протокол выборочного или сплошного входного/выходного контроля партии деталей.
* **Как работает:**
  * Поля: `report_id`, `batch_id`, `inspector`, `passed_items`, `rejected_items`.
  * `calculate_yield_rate()`: рассчитывает выход годной продукции в процентах от партии ($PPM$).
  * `sign_report()`: заверяет протокол электронной подписью контролера.
  * `is_batch_acceptable(min_yield)`: определяет, допускается ли партия к передаче на отгрузку клиенту.
* **Связи:** Заверяется инспектором [`QualityInspector`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/QualityInspector.py).

---

## 8. Транспорт, логистика и клиентский сервис (`plant/logistics/`)

### 8.1. `ShippingPallet`
* **Файл:** [`plant/logistics/ShippingPallet.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/logistics/ShippingPallet.py)
* **Что делает:** Стандартизированная европаллета (1200х800 мм) с деревянной/металлической обвязкой для укладки деталей.
* **Как работает:**
  * Поля: `pallet_id`, `max_capacity_parts`, `max_weight_kg`, `current_weight_kg`, `loaded_parts`.
  * `load_part(part, weight_kg)`: укладывает деталь на поддон; при перевесе или превышении вместимости выбрасывает [`StorageExhaustedException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/StorageExhaustedException.py).
  * `unload_all()`: полностью освобождает паллету на складе заказчика.
  * `is_full()`: проверяет предельное заполнение паллеты.
* **Связи:** Содержит готовые детали [`AutoPart`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/parts/AutoPart.py); выбрасывает [`StorageExhaustedException`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/StorageExhaustedException.py).

### 8.2. `Customer`
* **Файл:** [`plant/logistics/Customer.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/logistics/Customer.py)
* **Что делает:** Заказчик продукции: автосборочный завод (OEM-концерн) или оптовый дистрибьютор запчастей.
* **Как работает:**
  * Поля: `customer_id`, `company_name`, `address`, `contact_info`, `discount_rate`.
  * `apply_loyalty_discount(volume_bonus)`: увеличивает персональную скидку клиента за объем заказов.
  * `format_customer_card()`: формирует карточку контрагента с юридическими реквизитами.
  * `is_major_automaker()`: подтверждает статус крупного автопроизводителя (скидка $\ge 15\%$).
* **Связи:** Агрегирует [`Address`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/core/Address.py) и [`ContactInfo`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/core/ContactInfo.py).

### 8.3. `CustomerOrder`
* **Файл:** [`plant/logistics/CustomerOrder.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/logistics/CustomerOrder.py)
* **Что делает:** Коммерческий договор/заказ на поставку специфицированной партии компонентов клиенту.
* **Как работает:**
  * Поля: `order_id`, `customer`, `requested_parts`, `total_price`, `is_dispatched`.
  * `add_part_order(part_name, quantity, unit_price)`: добавляет товарную позицию в наряд поставки.
  * `dispatch()`: блокирует заказ от изменений и помечает статус «отгружен со склада».
  * `calculate_final_price()`: пересчитывает итоговую сумму с учетом клиентской скидки.
* **Связи:** Агрегирует клиента [`Customer`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/logistics/Customer.py).

### 8.4. `DeliveryVehicle`
* **Файл:** [`plant/logistics/DeliveryVehicle.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/logistics/DeliveryVehicle.py)
* **Что делает:** Грузовой магистральный тягач или малотоннажный фургон автопарка завода.
* **Как работает:**
  * Поля: `vehicle_plate`, `carrying_capacity_tons`, `current_load_tons`, `pallets_count`, `is_ready`.
  * `load_pallet(pallet_weight_tons)`: загружает паллету в кузов с контролем разрешенной массы.
  * `depart_for_delivery()`: отправляет автомобиль в рейс по путевому листу.
  * `get_load_factor()`: вычисляет коэффициент полезного использования грузоподъемности кузова.
* **Связи:** Назначается в транспортные заказы [`DispatchOrder`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/logistics/DispatchOrder.py).

### 8.5. `DispatchOrder`
* **Файл:** [`plant/logistics/DispatchOrder.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/logistics/DispatchOrder.py)
* **Что делает:** Товарно-транспортная накладная (ТТН) и маршрутный лист на рейс.
* **Как работает:**
  * Поля: `dispatch_id`, `customer_order`, `delivery_vehicle`, `departure_date`, `is_delivered`.
  * `confirm_delivery()`: регистрирует закрытие рейса и подписание акта приема-передачи груза получателем.
  * `calculate_transport_cost(distance_km, rate_per_km)`: рассчитывает себестоимость логистической доставки.
  * `generate_waybill()`: генерирует текст сопроводительной накладной ТТН.
* **Связи:** Связывает заказ [`CustomerOrder`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/logistics/CustomerOrder.py) и автомобиль [`DeliveryVehicle`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/logistics/DeliveryVehicle.py).

---

## 9. Главная управляющая система предприятия (`plant/enterprise/`)

### 9.1. `AutomotivePlant`
* **Файл:** [`plant/enterprise/AutomotivePlant.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/enterprise/AutomotivePlant.py)
* **Что делает:** Центральный управляющий класс («Фасад» завода), связывающий все цеха, склады, персонал и заказы воедино.
* **Как работает:**
  * Поля: `plant_name`, `director`, `warehouses`, `production_lines`, `active_orders`, `total_parts_produced`.
  * `register_warehouse(warehouse)`: добавляет склад сырья в единый логистический контур.
  * `add_production_line(line)` / `remove_production_line(line_id)`: конфигурирует цеховые мощности.
  * `receive_production_order(order)`: принимает наряд в оперативное производство.
  * `execute_daily_production(shifts_count)`: симулирует рабочий день завода: крутит смены на линиях, потребляет сырье, выпускает детали и прибавляет счетчик готовой продукции.
  * `restart_production_lines()`: производит сброс блокировок и перезапуск всех аварийных линий.
  * `emergency_plant_shutdown()`: аварийно обесточивает и останавливает все станки завода.
* **Связи:** Главный агрегатор всей системы: содержит [`PlantDirector`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/personnel/PlantDirector.py), список [`MaterialWarehouse`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/materials/MaterialWarehouse.py), список [`ProductionLine`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/production/ProductionLine.py) и список [`ProductionOrder`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/production/ProductionOrder.py).

---

## 10. Иерархия собственных классов исключений (`plant/exceptions/`)

Каждое исключение в проекте является полноценным доменным классом с уникальными методами обработки ошибок:

### 10.1. `PlantBaseException`
* **Файл:** [`plant/exceptions/PlantBaseException.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/PlantBaseException.py)
* **Что делает:** Базовый класс для всех нештатных ситуаций производственного цикла завода.
* **Как работает:** Поля: `message`, `error_code`. Метод `get_details()` возвращает структурированную строку об инциденте. Наследуется от стандартного `Exception`.

### 10.2. `CalibrationExpiredException`
* **Файл:** [`plant/exceptions/CalibrationExpiredException.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/CalibrationExpiredException.py)
* **Что делает:** Вызывается при попытке замера просроченным измерительным прибором лаборатории ОТК.
* **Методы:** `get_overdue_days()` возвращает количество дней, прошедших сверх допустимого межповерочного интервала.

### 10.3. `DefectThresholdExceededException`
* **Файл:** [`plant/exceptions/DefectThresholdExceededException.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/DefectThresholdExceededException.py)
* **Что делает:** Вызывается при превышении допустимого процента брака на производственной линии.
* **Методы:** `get_excess_percentage()` вычисляет разницу между фактическим процентом брака и лимитом стандарта IATF.

### 10.4. `EquipmentOverheatException`
* **Файл:** [`plant/exceptions/EquipmentOverheatException.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/EquipmentOverheatException.py)
* **Что делает:** Вызывается при перегреве подшипников шпинделя станка ЧПУ или термопечи.
* **Методы:** `get_excess_temp()` рассчитывает превышение текущей температуры над критическим порогом.

### 10.5. `InvalidSpecificationException`
* **Файл:** [`plant/exceptions/InvalidSpecificationException.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/InvalidSpecificationException.py)
* **Что делает:** Сигнализирует об ошибках в конструкторской документации (отрицательные допуски, нереалистичная чистота Ra).
* **Методы:** `format_validation_error()` формирует служебную записку в конструкторское бюро.

### 10.6. `MachineMalfunctionException`
* **Файл:** [`plant/exceptions/MachineMalfunctionException.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/MachineMalfunctionException.py)
* **Что делает:** Вызывается при аварийной механической поломке станка (обрыв ремня, клин ползуна, падение давления воздуха).
* **Методы:** `is_critical_failure()` возвращает `True`, если требуется полная остановка всей технологической цепочки.

### 10.7. `MaterialDefectException`
* **Файл:** [`plant/exceptions/MaterialDefectException.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/MaterialDefectException.py)
* **Что делает:** Вызывается при выявлении скрытых дефектов сырья (усадочные раковины в чушках, расслоение листа).
* **Методы:** `log_defect()` формирует запись для рекламации поставщику металла.

### 10.8. `OrderCapacityExceededException`
* **Файл:** [`plant/exceptions/OrderCapacityExceededException.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/OrderCapacityExceededException.py)
* **Что делает:** Вызывается при нехватке производственной мощности линий для выполнения заказа в требуемый срок.
* **Методы:** `get_overload_ratio()` вычисляет коэффициент перегрузки производственных мощностей.

### 10.9. `ProductionLineHaltException`
* **Файл:** [`plant/exceptions/ProductionLineHaltException.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/ProductionLineHaltException.py)
* **Что делает:** Вызывается при срабатывании концевых выключателей аварийного останова линии (E-Stop).
* **Методы:** `is_safety_fence_triggered()` определяет, вызвана ли остановка проникновением в опасную зону робота.

### 10.10. `QualityCheckFailedException`
* **Файл:** [`plant/exceptions/QualityCheckFailedException.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/QualityCheckFailedException.py)
* **Что делает:** Вызывается, если изготовленная автодеталь не уложилась в чертежный допуск по размерам.
* **Методы:** `get_dimension_deviation()` возвращает абсолютную величину геометрической погрешности в миллиметрах.

### 10.11. `RawMaterialShortageException`
* **Файл:** [`plant/exceptions/RawMaterialShortageException.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/RawMaterialShortageException.py)
* **Что делает:** Вызывается, когда остаток сырья в складской ячейке меньше, чем требуется на изготовление партии.
* **Методы:** `calculate_deficit()` возвращает точную недостающую массу металла/пластика в килограммах.

### 10.12. `SafetyViolationException`
* **Файл:** [`plant/exceptions/SafetyViolationException.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/SafetyViolationException.py)
* **Что делает:** Вызывается при нарушении рабочим правил охраны труда (работа без СИЗ, отсутствие аттестации).
* **Методы:** `requires_immediate_suspension()` возвращает `True`, если оператора необходимо немедленно отстранить от станка.

### 10.13. `StorageExhaustedException`
* **Файл:** [`plant/exceptions/StorageExhaustedException.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/StorageExhaustedException.py)
* **Что делает:** Вызывается при попытке положить деталь или сырье в переполненную ячейку хранения или паллету.
* **Методы:** `get_overflow_kg()` вычисляет величину перевеса в килограммах сверх лимита грузоподъемности.

### 10.14. `ToolWearExceededException`
* **Файл:** [`plant/exceptions/ToolWearExceededException.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/exceptions/ToolWearExceededException.py)
* **Что делает:** Вызывается при превышении предельного износа режущей кромки фрезы или циклов смыкания штампа.
* **Методы:** `requires_tool_replacement()` сигнализирует, что инструмент нельзя просто подточить, а требуется полная утилизация.

---

## 11. Консольный интерфейс и сериализация (`cli/`)

### 11.1. `PlantCli`
* **Файл:** [`cli/plant_cli.py`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/cli/plant_cli.py)
* **Что делает:** Реализует главное интерактивное меню пользователя из 13 пунктов: управление суточным циклом, нарядами-заказами, линиями, складом, заточкой инструмента, кадрами и сохранением/загрузкой состояния завода в JSON.
* **Как работает:**
  * Инкапсулирует объект [`AutomotivePlant`](file:///c:/Users/hxtxf/source/repos/ppois-lab/lab2/plant/enterprise/AutomotivePlant.py).
  * Поддерживает сквозную сериализацию всего состояния предприятия в файл `plant_state.json`.
  * Валидирует пользовательский ввод на неотрицательные числа, корректность индексов и существование нарядов.
* **Связи:** Главная точка контакта между пользователем и всей объектной моделью завода.
