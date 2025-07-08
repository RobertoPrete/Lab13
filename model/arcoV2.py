from dataclasses import dataclass

from model.driver import Driver


@dataclass
class ArcoV2:
    d1: Driver
    p1: int
    raceId: int
    d2: Driver
    p2: int
    peso: int
