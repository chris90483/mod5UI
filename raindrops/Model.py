import utilities
import random


class Model:

    # model of the cube.
    cube = None

    # array of raindrops. Each layer is its own array.
    drops = []

    def __init__(self):
        self.cube = utilities.cube.get_cube(32)

    # advance the model to the next frame
    def step(self):
        if not(len(self.drops) < 4):
            self.drops.remove(self.drops[0])
        self.drops.append(self.generate_raindrop_layer())
        self.put_drops_in_cube()

    def put_drops_in_cube(self):
        self.clear_cube()
        for y in range(0, len(self.drops)):
            drop_layer = self.drops[len(self.drops) - 1 - y]
            for x in range(0, 4):
                for z in range(0, 4):
                    if [x, z] in drop_layer:
                        self.cube[z][y][x][1] = True

    def clear_cube(self):
        for plane in self.cube:
            for row in plane:
                for val in row:
                    val[1] = False

    # generate a new layer of raindrops
    def generate_raindrop_layer(self):
        amount = random.randint(0, 16)
        raindrop_ints = random.sample(range(0, 16), amount)
        drop_layer = []
        for raindrop in raindrop_ints:
            x, z = divmod(raindrop, 4)
            drop_layer.append([x, z])
        return drop_layer
