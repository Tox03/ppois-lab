"""Исключение при непрохождении деталью выходного контроля качества (ОТК)."""

from plant.exceptions.plant_base_exception import PlantBaseException

class QualityCheckFailedException(PlantBaseException):
    """Вызывается, если параметры готовой автодетали выходят за пределы допусков чертежа."""

    def __init__(self, part_number: str, failed_parameter: str, measured_value: float, tolerance_limit: float) -> None:
        super().__init__(
            f"Брак детали '{part_number}' по параметру '{failed_parameter}': измерено {measured_value}, допуск {tolerance_limit}",
            error_code="ERR_QUALITY_CHECK_FAILED"
        )
        # Артикул или серийный номер детали
        self.part_number = part_number
        # Наименование забракованного параметра
        self.failed_parameter = failed_parameter
        # Измеренное контрольное значение
        self.measured_value = measured_value
        # Предельно допустимое значение по техпроцессу
        self.tolerance_limit = tolerance_limit

    def get_deviation(self) -> float:
        """Возвращает модуль величины отклонения измеренного параметра от допуска."""
        return abs(self.measured_value - self.tolerance_limit)
