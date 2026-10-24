"""Протокол дефектоскопии и отбраковки изделия."""

from __future__ import annotations
from plant.parts.auto_part import AutoPart
from plant.personnel.quality_inspector import QualityInspector

class DefectReport:
    """Фиксирует причину выбраковки конкретного экземпляра детали контролером ОТК."""

    def __init__(
        self,
        report_id: str,
        auto_part: AutoPart,
        inspector: QualityInspector,
        defect_description: str,
        severity_level: str = "КРИТИЧЕСКИЙ"
    ) -> None:
        # Номер дефектной ведомости
        self.report_id = report_id
        # Забракованная автодеталь (Ассоциация: AutoPart)
        self.auto_part = auto_part
        # Контролер ОТК, выявивший брак (Ассоциация: QualityInspector)
        self.inspector = inspector
        # Подробное описание обнаруженного дефекта
        self.defect_description = defect_description
        # Степень тяжести дефекта (КРИТИЧЕСКИЙ, УСТРАНИМЫЙ, НЕЗНАЧИТЕЛЬНЫЙ)
        self.severity_level = severity_level.upper()

    def classify_disposition(self) -> str:
        """Определяет технологический маршрут детали: в утиль, на доработку или в переплавку."""
        if self.severity_level == "КРИТИЧЕСКИЙ":
            self.auto_part.mark_as_defective()
            return "УТИЛИЗАЦИЯ_В_БРАК"
        elif self.severity_level == "УСТРАНИМЫЙ":
            return "ВОЗВРАТ_НА_ДОРАБОТКУ"
        return "РАЗРЕШЕНО_С_ОТКЛОНЕНИЕМ"

    def is_scrap(self) -> bool:
        """Проверяет окончательную негодность детали к эксплуатации."""
        return self.severity_level == "КРИТИЧЕСКИЙ"

    def format_ticket(self) -> str:
        """Формирует бирку дефектного изделия для изолятора брака."""
        return f"ДЕФЕКТ {self.report_id} [{self.auto_part.part_number}]: {self.defect_description} | Контролер: {self.inspector.inspector_badge_id}"
