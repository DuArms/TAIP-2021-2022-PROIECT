from typing import List, Tuple


from key.layer import Layer


class ZoneKey:
    coordonates : Tuple[Tuple[int]] = ()
    layers : List[Layer] = [] 

    def __init__(self) -> None:
        pass
    pass