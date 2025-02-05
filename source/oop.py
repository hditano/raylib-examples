import pyray as pr
import raylib as rl
from os.path import join


class Player:
    def __init__(self, pos, radius) -> None:
        self.pos = pos
        self.radius = radius
        self.color = pr.WHITE
        self.direction = pr.Vector2()
        self.speed = 400

    def update(self):
        self.direction.x = int(pr.is_key_down(rl.KEY_RIGHT)) - int(
            pr.is_key_down(rl.KEY_LEFT)
        )
        self.direction.y = int(pr.is_key_down(rl.KEY_DOWN)) - int(
            pr.is_key_down(rl.KEY_UP)
        )

        dt = pr.get_frame_time()
        self.pos.x += self.direction.x * self.speed * dt
        self.pos.y += self.direction.y * self.speed * dt

    def draw(self):
        pr.draw_circle_v(self.pos, self.radius, self.color)


class Block:
    def __init__(self, pos) -> None:
        self.pos = pos
        self.radius = 20
        self.color = pr.MAGENTA

    def update(self):
        pass

    def draw(self):
        pr.draw_circle_v(self.pos, self.radius, self.color)


class LoadImage:
    def __init__(self, image_path) -> None:
        self.image_path = image_path
        self.load_texture = pr.load_texture(self.image_path)

    def draw(self):
        pr.draw_texture(self.load_texture, 0, 0, pr.WHITE)

    def unload(self):
        pr.unload_texture(self.image_path)


pr.init_window(1920, 1080, "OOP")
player = Player(pr.Vector2(500, 200), 50)
block = Block((400, 400))
image = LoadImage("./assets/lv-yov.png")

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    player.update()
    player.draw()
    block.draw()
    image.draw()
    pr.end_drawing()

image.unload()
pr.close_window()
