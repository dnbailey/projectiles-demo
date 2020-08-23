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
spaceship.set_kind(SpriteKind.player)

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
    rock.set_kind(SpriteKind.enemy)

game.on_update_interval(750, on_update_interval)

# Shoot Enemies with Projectiles
def on_button_event_a_pressed():
    blast = sprites.create_projectile_from_sprite(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . 2 2 4 5 . . . . . .
    . . . . . . 2 2 4 5 . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    """), spaceship, 50, 0)

controller.player1.on_button_event(ControllerButton.A, ControllerButtonEvent.PRESSED, on_button_event_a_pressed)

# Lose Life when Hit
def on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    info.change_life_by(-1)

sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap)

# Destroy Rock when Blasted
def on_rock_blasted(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy(effects.fire, 100)
    info.change_score_by(1)
    if info.score() % 10 is 0:
        if info.life() < 5:
            info.change_life_by(1)

sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_rock_blasted)