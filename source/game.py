import pyray as pr
import raylib as rl
from random import choice, randint


pr.init_window(1920, 1080, "Collisions")
pr.set_target_fps(60)

player_pos = pr.Vector2()
player_speed = 400
player_radius = 50
player_direction = pr.Vector2()

# random circles
circles = [
    (
        pr.Vector2(randint(-2000, 2000), randint(-1800, 1800)),  # pos
        randint(50, 200),  # radius
        choice([pr.RED, pr.GREEN, pr.BLUE, pr.YELLOW, pr.ORANGE]),
    )
    for i in range(100)
]

# camera
camera = pr.Camera2D()
camera.zoom = 1
camera.target = player_pos
camera.offset = pr.Vector2(1920 / 2, 1080 / 2)
camera.rotation = 0


while not pr.window_should_close():
    # input
    player_direction.x = int(pr.is_key_down(rl.KEY_RIGHT)) - int(
        pr.is_key_down(rl.KEY_LEFT)
    )

    player_direction.y = int(pr.is_key_down(rl.KEY_DOWN)) - int(
        pr.is_key_down(rl.KEY_UP)
    )
    player_direction = pr.vector2_normalize(player_direction)

    # update
    dt = pr.get_frame_time()
    player_pos.x += player_direction.x * player_speed * dt
    player_pos.y += player_direction.y * player_speed * dt

    # camera update
    rotate_direction = int(pr.is_key_down(rl.KEY_S)) - int(pr.is_key_down(rl.KEY_A))
    zoom_camera = int(pr.is_key_down(rl.KEY_Q)) - int(pr.is_key_down(rl.KEY_W))
    camera.zoom += zoom_camera * dt * 1
    camera.rotation += rotate_direction * dt * 50
    camera.target = player_pos

    # drawing
    pr.begin_drawing()
    pr.begin_mode_2d(camera)  # add mode 2d
    pr.clear_background(pr.WHITE)
    for circle in circles:
        pr.draw_circle_v(*circle)
    pr.draw_circle_v(player_pos, player_radius, pr.RED)

    pr.end_mode_2d()
    pr.end_drawing()

pr.close_window()
