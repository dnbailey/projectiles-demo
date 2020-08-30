# Shoot Enemies with Projectiles

def on_player1_button_a_pressed():
    global blast
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
        """),
        spaceship,
        50,
        0)
controller.player1.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player1_button_a_pressed)

# Destroy Rock when Blasted

def on_on_overlap(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy(effects.fire, 100)
    info.change_score_by(1)
    if info.score() % 10 == 0:
        if info.life() < 5:
            info.change_life_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

# Lose Life when Hit

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

rock: Sprite = None
blast: Sprite = None
spaceship: Sprite = None
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
    """),
    0)
spaceship.set_position(10, scene.screen_height() / 2)
spaceship.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
spaceship.set_kind(SpriteKind.player)
# Configure Player Controls
controller.move_sprite(spaceship, 200, 200)
# Generate Enemies

def on_update_interval():
    global rock
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
        """),
        0)
    rock.set_position(scene.screen_width(), randint(0, scene.screen_height()))
    rock.set_velocity(-50, 0)
    rock.set_kind(SpriteKind.enemy)
game.on_update_interval(750, on_update_interval)
