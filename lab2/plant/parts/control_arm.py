"""Рычаг независимой передней/задней подвески автомобиля."""

from __future__ import annotations
from plant.parts.auto_part import AutoPart

class ControlArm:
    """Описывает штампованный или кованый рычаг подвески в сборе с сайлентблоками."""

    def __init__(
        self,
        auto_part: AutoPart,
        bushing_count: int,
        ball_joint_fitted: bool,
        load_rating_kn: float,
        is_aluminum: bool = False
    ) -> None:
        # Базовый паспорт автодетали (Ассоциация: AutoPart)
        self.auto_part = auto_part
        # Количество запрессованных резинометаллических шарниров (сайлентблоков)
        self.bushing_count = bushing_count
        # Наличие смонтированной шаровой опоры
        self.ball_joint_fitted = ball_joint_fitted
        # Расчетная допустимая статическая нагрузка на излом в кН
        self.load_rating_kn = load_rating_kn
        # Признак облегченной конструкции из кованого алюминия
        self.is_aluminum = is_aluminum

    def test_structural_strength(self, applied_load_kn: float) -> bool:
        """Проводит испытание рычага на гидропрессе на предельную нагрузку."""
        passes = applied_load_kn <= self.load_rating_kn
        if not passes:
            self.auto_part.is_defect_free = False
        return passes

    def install_ball_joint(self) -> None:
        """Выполняет операцию завальцовки/монтажа шарового пальца в проушину."""
        self.ball_joint_fitted = True

    def is_complete_subassembly(self) -> bool:
        """Проверяет полную комплектность узла перед передачей на автосборочный конвейер."""
        return self.bushing_count >= 2 and self.ball_joint_fitted and self.auto_part.is_defect_free
