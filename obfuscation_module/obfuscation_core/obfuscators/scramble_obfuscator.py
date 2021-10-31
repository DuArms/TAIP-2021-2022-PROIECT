import random
from datetime import datetime

from numpy import ndarray

from obfuscation_module.key.key_builder import KeyBuilder
from obfuscation_module.key.key_types.layer import Layer
from obfuscation_module.obfuscation_core.obfuscators.obfuscator import Obfuscator


class ScrambleObfuscator(Obfuscator):
    # def get_image(self, coordinates, image):
    #     ((x1, y1), (x2, y2)) = coordinates
    #     return image[y1:y2, x1:x2]

    scramble_percent = 100

    def obfuscate(self, image: ndarray, key_builder: KeyBuilder):
        print("Scrambling")
        random.seed(datetime.now())
        key_data = int(random.random() * 100000000000)
        layer = Layer(50, str(key_data) + "||" + str(self.scramble_percent))
        key_builder.set_step(layer)

        random.seed(key_data)
        y_size = len(image)
        x_size = len(image[0])
        nr_pixels = (self.scramble_percent * image.size) // 100

        coords_list = []
        for i in range(nr_pixels):
            start_x = random.randrange(1000000) % x_size
            start_y = random.randrange(1000000) % y_size
            end_x = random.randrange(1000000) % x_size
            end_y = random.randrange(1000000) % y_size

            aux = image[start_y][start_x].copy()
            image[start_y][start_x] = image[end_y][end_x]
            image[end_y][end_x] = aux
            coords_list.append(((start_y, start_x), (end_y, end_x)))

        if self.next_obfuscator is not None:
            self.next_obfuscator.obfuscate(image, key_builder)