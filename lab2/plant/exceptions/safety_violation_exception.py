"""Исключение при грубом нарушении требований техники безопасности и охраны труда."""

from plant.exceptions.plant_base_exception import PlantBaseException

class SafetyViolationException(PlantBaseException):
    """Вызывается при несоблюдении регламентов безопасности оператором или рабочим."""

    def __init__(self, employee_id: str, violation_type: str, penalty_points: int = 1) -> None:
        super().__init__(
            f"Нарушение ТБ сотрудником '{employee_id}': {violation_type}",
            error_code="ERR_SAFETY_VIOLATION"
        )
        # Табельный номер сотрудника-нарушителя
        self.employee_id = employee_id
        # Категория нарушения (отсутствие СИЗ, вход в опасную зону и т.п.)
        self.violation_type = violation_type
        # Штрафные баллы
        self.penalty_points = penalty_points

    def get_penalty_level(self) -> str:
        """Возвращает уровень тяжести дисциплинарного взыскания."""
        if self.penalty_points >= 3:
            return "КРИТИЧЕСКИЙ_ОТСТРАНЕНИЕ"
        return "ПРЕДУПРЕЖДЕНИЕ"
