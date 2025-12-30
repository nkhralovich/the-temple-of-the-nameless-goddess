from dataclasses import dataclass
from enum import Enum


class RoomType(Enum):
    ENEMY = "enemy"
    BOOK = "book"
    EMPTY = "empty"

# W przyszłości dodam tu dataclass Room, która pozwoli mieć różne opisy dla każdego pokoju + różne efekty (pułapki, nagrody itd) i flagę, która pokaże czy gracz już odwiedził ten pokój.