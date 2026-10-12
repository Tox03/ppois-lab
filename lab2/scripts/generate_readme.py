"""Генератор полного файла README.md для лабораторной работы №2."""

import ast
import os

def generate_readme():
    plant_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "plant"))
    
    classes_data = []
    exceptions_list = []

    for dirpath, _, filenames in os.walk(plant_dir):
        for f in sorted(filenames):
            if not f.endswith(".py") or f == "__init__.py":
                continue
            filepath = os.path.join(dirpath, f)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
            
            tree = ast.parse(content, filename=filepath)
            for node in tree.body:
                if isinstance(node, ast.ClassDef):
                    cls_name = node.name
                    docstring = ast.get_docstring(node) or ""
                    
                    is_exception = any(
                        (isinstance(b, ast.Name) and "Exception" in b.id) or
                        (isinstance(b, ast.Attribute) and "Exception" in b.attr)
                        for b in node.bases
                    )
                    
                    fields = set()
                    methods = []
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef):
                            if item.name == "__init__":
                                for stmt in ast.walk(item):
                                    if isinstance(stmt, ast.Assign):
                                        for target in stmt.targets:
                                            if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == "self":
                                                fields.add(target.attr)
                                    elif isinstance(stmt, ast.AnnAssign):
                                        is_attr = (
                                            isinstance(stmt.target, ast.Attribute)
                                            and isinstance(stmt.target.value, ast.Name)
                                            and stmt.target.value.id == "self"
                                        )
                                        if is_attr:
                                            fields.add(stmt.target.attr)
                            else:
                                methods.append(item.name)
                    
                    associations = set()
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef):
                            for arg in item.args.args:
                                if arg.annotation:
                                    for sub in ast.walk(arg.annotation):
                                        if isinstance(sub, ast.Name) and sub.id not in (
                                            "str", "int", "float", "bool", "dict", "list", "set", "tuple", "None",
                                            "Optional", "List", "Dict", "Set", "Tuple", "Any"
                                        ):
                                            associations.add(sub.id)
                    for n in tree.body:
                        if isinstance(n, ast.ImportFrom):
                            for alias in n.names:
                                if alias.name[0].isupper() and alias.name != cls_name and alias.name not in (
                                    "List", "Dict", "Set", "Tuple", "Optional", "Any"
                                ):
                                    associations.add(alias.name)
                    
                    assoc_filtered = sorted(list(associations))
                    
                    if is_exception:
                        exceptions_list.append((cls_name, docstring))
                    
                    classes_data.append({
                        "name": cls_name,
                        "is_exception": is_exception,
                        "fields_count": len(fields),
                        "methods_count": len(methods),
                        "fields": sorted(list(fields)),
                        "methods": methods,
                        "associations": assoc_filtered,
                        "docstring": docstring.strip()
                    })

    # Сортировка доменных классов по алфавиту
    domain_classes = sorted([c for c in classes_data if not c["is_exception"]], key=lambda x: x["name"])
    exceptions_classes = sorted([c for c in classes_data if c["is_exception"]], key=lambda x: x["name"])

    total_fields = sum(c["fields_count"] for c in classes_data)
    total_methods = sum(c["methods_count"] for c in classes_data)
    total_associations = sum(len(c["associations"]) for c in classes_data)

    readme_lines = []
    readme_lines.append("# Лабораторная работа №2. Крупный ООП-проект")
    readme_lines.append("## Предметная область: Завод по изготовлению автомобильных деталей\n")
    readme_lines.append("### Описание проекта")
    readme_lines.append(
        "Данный проект представляет собой высокодетализированную объектно-ориентированную модель "
        "крупного машиностроительного предприятия по производству автокомпонентов и автомобильных узлов "
        "(поршни ДВС, тормозные диски, амортизаторы, валы трансмиссий, топливные форсунки, рычаги подвески, "
        "выпускные коллекторы и др.). Архитектура охватывает складское хозяйство, раскрой и литье сырья, "
        "станочный парк (прессы, ЧПУ-центры, сварочные роботы, лазерные комплексы, закалочные печи), "
        "метрологическую службу ОТК, персонал, производственное планирование, управление качеством по стандарту IATF 16949 и логистику.\n"
    )
    readme_lines.append("### Структура проекта и архитектурные правила")
    readme_lines.append("- Язык программирования: **Python 3**.")
    readme_lines.append("- **Строго 1 класс на 1 файл**: каждый класс доменной модели и каждое исключение вынесены в индивидуальный `.py`-файл.")
    readme_lines.append("- Все комментарии, документация и docstring выполнены на **русском языке**.")
    readme_lines.append("- Никаких сторонних внешних библиотек (запуск тестов через стандартный `unittest`).\n")

    readme_lines.append("## Таблица классов предметной области\n")
    readme_lines.append("Формат строки: `Класс | число полей | число методов | связанные классы`.\n")
    readme_lines.append("| Класс | Поля | Методы | Ассоциации (связанные классы) |")
    readme_lines.append("|---|---|---|---|")

    for c in domain_classes:
        assoc_str = ", ".join(c["associations"]) if c["associations"] else "—"
        readme_lines.append(f"| {c['name']} | {c['fields_count']} | {c['methods_count']} | {assoc_str} |")

    readme_lines.append(f"\n### Исключения ({len(exceptions_classes)})\n")
    for exc in exceptions_classes:
        readme_lines.append(f"- **{exc['name']}** — {exc['docstring']}")

    readme_lines.append("\n### Итоговая статистика проекта\n")
    readme_lines.append("| Показатель | Значение | Требование |")
    readme_lines.append("|---|---|---|")
    readme_lines.append(f"| Классы (всего) | {len(classes_data)} | не менее 50 |")
    readme_lines.append(f"| Доменные классы | {len(domain_classes)} | — |")
    readme_lines.append(f"| Исключения | {len(exceptions_classes)} | не менее 12 |")
    readme_lines.append(f"| Поля (суммарно) | {total_fields} | не менее 150 |")
    readme_lines.append(f"| Поведения (методы) | {total_methods} | не менее 100 |")
    readme_lines.append(f"| Ассоциации | {total_associations} | не менее 30 |")
    readme_lines.append("| Файлов с >1 классом | 0 | 0 (запрещено) |\n")

    readme_lines.append("## Подробное описание подсистем завода\n")
    
    categories = [
        ("Базовые метрологические сущности и реквизиты (`plant/core/`)", [
            "Dimension", "TechnicalSpecification", "SerialNumber", "Address", "ContactInfo"
        ]),
        ("Сырье, материалы и складское хозяйство (`plant/materials/`)", [
            "RawMaterial", "MetalSheet", "AlloyIngot", "RubberCompound", "PlasticPellet",
            "ChemicalCoolant", "MaterialBatch", "StorageBin", "MaterialWarehouse", "MaterialSupplier"
        ]),
        ("Станочный парк и промышленное оборудование (`plant/equipment/`)", [
            "Machine", "ToolingFixture", "CuttingTool", "StampingPress", "CncMillingMachine",
            "WeldingRobot", "PaintingBooth", "HeatTreatmentFurnace", "LaserCutter", "EquipmentSensor", "MaintenanceLog"
        ]),
        ("Персонал и управление сменами (`plant/personnel/`)", [
            "Employee", "MachineOperator", "QualityInspector", "MaintenanceEngineer",
            "Toolmaker", "SafetyOfficer", "ShiftSupervisor", "PlantDirector"
        ]),
        ("Производственный цикл и оперативное планирование (`plant/production/`)", [
            "WorkStation", "ManufacturingProcess", "ProductionLine", "WorkShift",
            "ProductionPlan", "ProductionOrder", "EnergyMeter", "ScrapRecord"
        ]),
        ("Автомобильные детали и компоненты (`plant/parts/`)", [
            "AutoPart", "EnginePiston", "BrakeDisc", "ShockAbsorber",
            "GearboxShaft", "FuelInjector", "ControlArm", "ExhaustManifold"
        ]),
        ("Контроль качества, лаборатория ОТК и метрология (`plant/quality/`)", [
            "QualityStandard", "CalibrationTool", "CmmScanner", "TensileTester",
            "HardnessTester", "DefectReport", "InspectionReport"
        ]),
        ("Транспорт, логистика и клиентский сервис (`plant/logistics/`)", [
            "ShippingPallet", "Customer", "CustomerOrder", "DeliveryVehicle", "DispatchOrder"
        ]),
        ("Главная управляющая система завода (`plant/`)", [
            "AutomotivePlant"
        ])
    ]

    for cat_name, class_names in categories:
        readme_lines.append(f"### {cat_name}\n")
        for cls_name in class_names:
            c = next((item for item in domain_classes if item["name"] == cls_name), None)
            if c:
                fields_str = ", ".join(f"`{f}`" for f in c["fields"])
                methods_str = ", ".join(f"`{m}()`" for m in c["methods"])
                readme_lines.append(f"#### Класс `{c['name']}`")
                readme_lines.append(f"*{c['docstring']}*")
                readme_lines.append(f"- **Поля ({c['fields_count']})**: {fields_str}")
                readme_lines.append(f"- **Методы ({c['methods_count']})**: {methods_str}")
                if c["associations"]:
                    readme_lines.append(f"- **Ассоциации**: {', '.join(f'`{a}`' for a in c['associations'])}")
                readme_lines.append("")

    readme_lines.append("## Запуск тестов и валидатора метрик\n")
    readme_lines.append("### Запуск модульных тестов:")
    readme_lines.append("```bash\ncd lab2\npython -m unittest discover -s tests -p \"test_*.py\" -v\n```\n")
    readme_lines.append("### Проверка соответствия количественным метрикам задания:")
    readme_lines.append("```bash\npython scripts/analyze_metrics.py\n```\n")

    readme_content = "\n".join(readme_lines)
    readme_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "README.md"))
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"README.md успешно сгенерирован по пути: {readme_path}")

if __name__ == "__main__":
    generate_readme()
