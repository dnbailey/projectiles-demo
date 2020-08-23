# Setup the Game
info.set_score(0)
info.set_life(3)

# Setup the Player
spaceship = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . 2 2 . . . . . . . . . . . .
    . . 2 2 2 2 . . . . . . . . . .
    . . 2 2 2 2 2 . . . . . . . . .
    . . 4 4 4 4 4 2 . . . . . . . .
    . . 4 4 4 4 4 2 2 2 . . . . . .
    . . 4 4 4 4 4 2 2 2 2 . . . . .
    . . 4 4 4 4 4 2 2 2 . . . . . .
    . . 4 4 4 4 4 2 . . . . . . . .
    . . 2 2 2 2 2 . . . . . . . . .
    . . 2 2 2 2 . . . . . . . . . .
    . . 2 2 . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""))
spaceship.set_position(10, scene.screen_height()/2)
spaceship.set_flag(SpriteFlag.StayInScreen, True)

# Configure Player Controls
controller.move_sprite(spaceship, 200, 200)

# Generate Enemies
def on_update_interval():
    rock = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . c c c . . . . . . .
    . . . . . c c b . c c . . . . .
    . . . . . c c c c . c c c . . .
    . . . . c c c c c c . c . . . .
    . . . . c . c c c c c b . . . .
    . . . c c c c c . . c c . . . .
    . . . . . c b b c c b c . . . .
    . . . . . c . c b c c . . . . .
    . . . . . c c . c c c . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    """))
    rock.set_position(scene.screen_width(), randint(0,scene.screen_height()))
    rock.set_velocity(-50, 0)

game.on_update_interval(750, on_update_interval)

# Shoot Enemies with Projectiles
