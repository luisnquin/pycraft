from ursina import *


def update():
    if held_keys["a"]:
        squareone.x -= .1 * time.dt


app = Ursina()

squareone = Entity(model="quad", color=color.green, scale=(10, 5), position=(5, 0))

sans_texture = load_texture("")
sans = Entity(model="quad", texture="")

app.run()
