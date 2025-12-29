from dataclasses import dataclass
from enum import Enum


class EquipmentType(Enum):
    WEAPON ="weapon"
    ARMOR = "armor"
    OTHER = "other"


@dataclass
class Equipment:
    equipment_type: EquipmentType
    die: int
    description: str



EQUIPMENT_TABLE = {
    1: Equipment(EquipmentType.WEAPON, 6, "a sword"),
    2: Equipment(EquipmentType.WEAPON, 4, "a club"),
    3: Equipment(EquipmentType.OTHER, 0, "nothing"),
    4: Equipment(EquipmentType.OTHER, 0,  "nothing"),
    5: Equipment(EquipmentType.ARMOR, 2, "a shield"),
    6: Equipment(EquipmentType.ARMOR, 4, "leather armor")
}
