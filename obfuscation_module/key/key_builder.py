from key.key_types.layer import Layer
from typing import List, Tuple
from key.key_types.zone_key import ZoneKey


class KeyBuilder:
    def __init__(self, coord):
        self.key: ZoneKey = ZoneKey()
        self.key.coordonates = coord
        self.steps: List[Layer] = []

    def reset(self) -> None:
        self.key = ZoneKey()
        self.steps = []

    def set_step(self, layer: Layer) -> None:
        self.steps.append(layer)


    def build(self) -> ZoneKey:
        # compile
        return self.key