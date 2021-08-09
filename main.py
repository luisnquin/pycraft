from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            model="cube",
            position=position,
            origin_y=0.5,
            texture="white_cube",
            color=color.white,
            hightlight_color=color.lime
        )


app = Ursina()

for z in range(10):
    for x in range(10):
        voxel1 = Voxel((x, 0, z))

player1 = FirstPersonController()

app.run()
