"""Исключение при некорректных или противоречивых конструкторских спецификациях автодетали."""

from plant.exceptions.plant_base_exception import PlantBaseException

class InvalidSpecificationException(PlantBaseException):
    """Вызывается при обнаружении недопустимых геометрических или прочностных параметров в КД."""

    def __init__(self, spec_id: str, reason: str) -> None:
        super().__init__(
            f"Недопустимая конструкторская спецификация '{spec_id}': {reason}",
            error_code="ERR_INVALID_SPECIFICATION"
        )
        # Идентификатор конструкторской спецификации
        self.spec_id = spec_id
        # Причина отклонения спецификации
        self.reason = reason

    def get_validation_report(self) -> str:
        """Формирует отчет для конструкторского бюро о несоответствии чертежа нормам."""
        return f"Спецификация {self.spec_id} отклонена технологическим отделом. Обоснование: {self.reason}"
