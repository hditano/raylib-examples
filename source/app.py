import pyray as pr
from random import choice, randint

# INITIAL SETUP
pr.set_target_fps(60)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
REC_1 = pr.Rectangle(0, 0, 100, 200)
rect_visible = True

pr.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Hello")
ball_position = pr.Vector2(800 / 2, 450 / 2)

circles = [
    (
        pr.Vector2(randint(-2000, 2000), randint(-1000, 1000)),  # Position
        randint(50, 200),  # radius
        choice([pr.RED, pr.GREEN, pr.BLUE, pr.YELLOW, pr.ORANGE]),  # color
    )
    for i in range(100)
]

# Player
pos = pr.Vector2()

# camera
camera = pr.Camera2D()
camera.zoom = 2
camera.target = pos
camera.offset = pr.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Player Input
while not pr.window_should_close():
    if pr.is_key_down(pr.KeyboardKey.KEY_RIGHT) and ball_position.x < SCREEN_WIDTH - 50:
        ball_position.x += 2
    if pr.is_key_down(pr.KeyboardKey.KEY_LEFT) and ball_position.x > 50:
        ball_position.x -= 2
    if pr.is_key_down(pr.KeyboardKey.KEY_DOWN) and ball_position.y < SCREEN_HEIGHT - 50:
        ball_position.y += 2
    if pr.is_key_down(pr.KeyboardKey.KEY_UP) and ball_position.y > 50:
        ball_position.y -= 2

    # Camera Update
    camera.target = pos

    ## Start Drawing
    pr.begin_drawing()
    pr.begin_mode_2d(camera)
    pr.clear_background(pr.WHITE)

    ## Collision
    ##if ball_position.x >= SCREEN_WIDTH or ball_position.x <= 0:
    ##    pr.draw_text("Llegaste al limite", 300, 600, 20, pr.MAGENTA)
    ##if ball_position.y >= SCREEN_HEIGHT or ball_position.y <= 0:
    ##    pr.draw_text(
    ##        "Llegaste al Limite de Height ({:.0f}, {:.0f})".format(
    ##            ball_position.x, ball_position.y
    ##        ),
    ##        300,
    ##        600,
    ##        20,
    ##        pr.MAGENTA,
    ##    )

    ## Checks for Rect Collision
    if rect_visible and pr.check_collision_circle_rec(ball_position, 50, REC_1):
        print("Toco el Rec!!")
        rect_visible = False

    ## Drawing Primitives
    if rect_visible:
        pr.draw_rectangle_rec(REC_1, pr.BLUE)

    ## Drawing Circles from list of tuples Line 15
    for circle in circles:
        pr.draw_circle_v(*circle)

    pr.draw_circle_v(ball_position, 50, pr.MAROON)
    pr.draw_text(
        "Ball Position: ({:.0f}, {:.0f})".format(ball_position.x, ball_position.y),
        200,
        200,
        15,
        pr.BLACK,
    )
    pr.draw_fps(500, 20)

    pr.end_drawing()

pr.close_window()
