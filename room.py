from dataclasses import dataclass
from enum import Enum


class RoomType(Enum):
    ENEMY = "enemy"
    BOOK = "book"
    EMPTY = "empty"


ROOM_TABLE = {
    1: RoomType.EMPTY,
    2: RoomType.ENEMY,
    3: RoomType.ENEMY,
    4: RoomType.ENEMY,
    5: RoomType.EMPTY,
    6: RoomType.BOOK
}
# W przyszłości dodam tu dataclass Room, która pozwoli mieć różne opisy dla każdego pokoju + różne efekty (pułapki, nagrody itd) i flagę, która pokaże czy gracz już odwiedził ten pokój.