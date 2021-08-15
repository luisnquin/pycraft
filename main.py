from ursina import held_keys, load_texture, scene, color, random, mouse, destroy, camera
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import Ursina, Audio, Button, Entity, Vec2, Vec3


app = Ursina()

punch_sound = Audio("assets/punch_sound", loop=False, autoplay=False)

grass_texture = load_texture("assets/grass_texture.png")
stone_texture = load_texture("assets/stone_texture.png")
brick_texture = load_texture("assets/brick_texture.png")
sky_texture = load_texture("assets/skybox_texture.png")
dirt_texture = load_texture("assets/dirt_texture.png")
arm_texture = load_texture("assets/arm_texture.png")


block_pick = 1


def update():
    global block_pick
    if held_keys["left mouse"] or held_keys["right mouse"]:
        hand.active()
    else:
        hand.passive()

    if held_keys["1"]:
        block_pick = 1
    if held_keys["2"]:
        block_pick = 2
    if held_keys["3"]:
        block_pick = 3
    if held_keys["4"]:
        block_pick = 4


class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model="assets/block",
            origin_y=0.5,
            texture=grass_texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == "right mouse down":
                punch_sound.play()
                if block_pick == 1:
                    voxel = Voxel(position=self.position + mouse.normal)
                    voxel.texture = grass_texture
                if block_pick == 2:
                    voxel = Voxel(position=self.position + mouse.normal)
                    voxel.texture = stone_texture
                if block_pick == 3:
                    voxel = Voxel(position=self.position + mouse.normal)
                    voxel.texture = brick_texture
                if block_pick == 4:
                    voxel = Voxel(position=self.position + mouse.normal)
                    voxel.texture = dirt_texture

            if key == "left mouse down":
                punch_sound.play()
                destroy(self)


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="sphere",
            texture=sky_texture,
            scale=150,
            double_sided=True
        )


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="assets/arm",
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6)
        )

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)


for z in range(10):
    for x in range(10):
        voxel1 = Voxel((x, 0, z))
        voxel2 = Voxel((x, -1, z)).texture = dirt_texture
        voxel4 = Voxel((x, -2, z)).texture = stone_texture

player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()
