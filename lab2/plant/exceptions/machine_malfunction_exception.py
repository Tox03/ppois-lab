"""Исключение при механической или аппаратной аварии промышленного станка."""

from plant.exceptions.plant_base_exception import PlantBaseException

class MachineMalfunctionException(PlantBaseException):
    """Вызывается при аварийном сбое узлов станка, заклинивании или обрыве привода."""

    def __init__(self, machine_id: str, failure_reason: str, is_critical: bool = True) -> None:
        super().__init__(
            f"Авария станка '{machine_id}': {failure_reason}",
            error_code="ERR_MACHINE_MALFUNCTION"
        )
        # Идентификатор неисправного станка
        self.machine_id = machine_id
        # Описание неисправности
        self.failure_reason = failure_reason
        # Флаг критичности (требует ли немедленного вызова аварийной бригады)
        self.is_critical = is_critical

    def is_critical_failure(self) -> bool:
        """Проверяет, является ли поломка критической."""
        return self.is_critical
