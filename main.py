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

# Shoot Enemies with Projectiles
