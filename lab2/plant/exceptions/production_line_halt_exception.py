"""Исключение при экстренной остановке конвейерной производственной линии."""

from plant.exceptions.plant_base_exception import PlantBaseException

class ProductionLineHaltException(PlantBaseException):
    """Вызывается при аварийном размыкании цепи безопасности или сбое конвейера."""

    def __init__(self, line_id: str, halt_reason: str, requires_evacuation: bool = False) -> None:
        super().__init__(
            f"Аварийная остановка линии '{line_id}': {halt_reason}",
            error_code="ERR_PRODUCTION_LINE_HALT"
        )
        # Идентификатор остановленной производственной линии
        self.line_id = line_id
        # Причина экстренной остановки
        self.halt_reason = halt_reason
        # Требуется ли эвакуация персонала цеха
        self.requires_evacuation = requires_evacuation

    def requires_emergency_evacuation(self) -> bool:
        """Проверяет необходимость немедленной эвакуации рабочей смены."""
        return self.requires_evacuation
