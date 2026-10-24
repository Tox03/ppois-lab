"""Исключение при обнаружении брака или дефекта в партии сырья."""

from plant.exceptions.plant_base_exception import PlantBaseException

class MaterialDefectException(PlantBaseException):
    """Вызывается при обнаружении несоответствия физико-химических свойств сырья."""

    def __init__(self, material_name: str, defect_description: str) -> None:
        super().__init__(
            f"Обнаружен дефект материала '{material_name}': {defect_description}",
            error_code="ERR_MATERIAL_DEFECT"
        )
        # Наименование забракованного сырья
        self.material_name = material_name
        # Описание выявленного дефекта
        self.defect_description = defect_description

    def log_defect(self) -> str:
        """Формирует отчет о дефекте для службы рекламаций поставщикам."""
        return f"Материал: {self.material_name} | Причина: {self.defect_description}"
