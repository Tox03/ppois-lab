"""Конструкторско-технологическая спецификация автомобильной детали."""

from __future__ import annotations
from plant.exceptions.invalid_specification_exception import InvalidSpecificationException

class TechnicalSpecification:
    """Определяет прочностные и чистовые требования к изготовлению автодетали."""

    def __init__(
        self,
        spec_id: str,
        standard_code: str,
        required_tensile_strength_mpa: float,
        max_allowed_roughness_ra: float,
        is_critical: bool = False
    ) -> None:
        # Идентификатор технической спецификации
        self.spec_id = spec_id
        # Код отраслевого стандарта (ГОСТ / DIN / ISO)
        self.standard_code = standard_code
        # Минимальный требуемый предел прочности на разрыв (МПа)
        self.required_tensile_strength_mpa = required_tensile_strength_mpa
        # Предельная шероховатость обработанной поверхности (мкм Ra)
        self.max_allowed_roughness_ra = max_allowed_roughness_ra
        # Признак детали, влияющей на безопасность движения
        self.is_critical = is_critical

    def validate_roughness(self, measured_roughness: float) -> bool:
        """Проверяет соответствие шероховатости поверхности конструкторскому допуску."""
        if measured_roughness < 0:
            raise InvalidSpecificationException(self.spec_id, "Шероховатость не может быть отрицательной")
        return measured_roughness <= self.max_allowed_roughness_ra

    def verify_strength(self, measured_strength: float) -> bool:
        """Проверяет, превышает ли измеренный предел прочности металла минимальный порог."""
        if measured_strength <= 0:
            raise InvalidSpecificationException(self.spec_id, "Предел прочности должен быть больше 0")
        return measured_strength >= self.required_tensile_strength_mpa

    def mark_as_critical(self, reason: str) -> None:
        """Присваивает спецификации статус критической по безопасности с фиксацией причины."""
        if not reason.strip():
            raise InvalidSpecificationException(self.spec_id, "Причина критичности должна быть заполнена")
        self.is_critical = True
