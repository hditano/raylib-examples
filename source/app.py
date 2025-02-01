import pyray as pr

pr.set_target_fps(60)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

pr.init_window(1920, 1080, "Hello")
ball_position = pr.Vector2(800 / 2, 450 / 2)

while not pr.window_should_close():
    if pr.is_key_down(pr.KeyboardKey.KEY_RIGHT) and ball_position.x < SCREEN_WIDTH - 50:
        ball_position.x += 2
    if pr.is_key_down(pr.KeyboardKey.KEY_LEFT) and ball_position.x > 50:
        ball_position.x -= 2
    if pr.is_key_down(pr.KeyboardKey.KEY_DOWN) and ball_position.y < SCREEN_HEIGHT - 50:
        ball_position.y += 2
    if pr.is_key_down(pr.KeyboardKey.KEY_UP) and ball_position.y > 50:
        ball_position.y -= 2

    pr.begin_drawing()
    pr.clear_background(pr.WHITE)

    if ball_position.x >= SCREEN_WIDTH or ball_position.x <= 0:
        pr.draw_text("Llegaste al limite", 300, 600, 20, pr.MAGENTA)
    if ball_position.y >= SCREEN_HEIGHT or ball_position.y <= 0:
        pr.draw_text(
            "Llegaste al Limite de Height ({:.0f}, {:.0f})".format(
                ball_position.x, ball_position.y
            ),
            300,
            600,
            20,
            pr.MAGENTA,
        )

    pr.draw_rectangle(SCREEN_WIDTH - 50, 0, 50, 50, pr.BLUE)
    pr.draw_circle_v(ball_position, 50, pr.MAROON)
    pr.draw_ellipse(500, 200, 100, 150, pr.RED)
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
