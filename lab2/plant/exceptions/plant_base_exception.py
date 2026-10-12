"""Базовое исключение домена завода по изготовлению автомобильных деталей."""

class PlantBaseException(Exception):
    """Базовый класс для всех исключений производственного цикла завода."""

    def __init__(self, message: str, error_code: str = "ERR_PLANT_GENERAL") -> None:
        super().__init__(message)
        # Сообщение об ошибке
        self.message = message
        # Уникальный код ошибки
        self.error_code = error_code

    def get_details(self) -> str:
        """Возвращает форматированную детальную информацию об ошибке."""
        return f"[{self.error_code}] {self.message}"
