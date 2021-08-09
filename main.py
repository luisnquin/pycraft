from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
grass_texture = load_texture("Textures/grass_texture.png")


class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model="textures/block",
            origin_y=0.5,
            texture=grass_texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            hightlight_color=color.lime,
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == "right mouse down":
                voxel = Voxel(position=self.position + mouse.normal)

            if key == "left mouse down":
                destroy(self)


for z in range(10):
    for x in range(10):
        voxel1 = Voxel((x, 0, z))

player1 = FirstPersonController()

app.run()
