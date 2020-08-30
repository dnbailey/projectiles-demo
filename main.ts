//  Shoot Enemies with Projectiles
controller.player1.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function on_player1_button_a_pressed() {
    
    blast = sprites.createProjectileFromSprite(img`
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
        `, spaceship, 50, 0)
})
//  Destroy Rock when Blasted
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    sprite.destroy()
    otherSprite.destroy(effects.fire, 100)
    info.changeScoreBy(1)
    if (info.score() % 10 == 0) {
        if (info.life() < 5) {
            info.changeLifeBy(1)
        }
        
    }
    
})
//  Lose Life when Hit
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap2(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy()
    info.changeLifeBy(-1)
})
let rock : Sprite = null
let blast : Sprite = null
let spaceship : Sprite = null
//  Setup the Game
info.setScore(0)
info.setLife(3)
//  Setup the Player
spaceship = sprites.create(img`
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
    `, 0)
spaceship.setPosition(10, scene.screenHeight() / 2)
spaceship.setFlag(SpriteFlag.StayInScreen, true)
spaceship.setKind(SpriteKind.Player)
//  Configure Player Controls
controller.moveSprite(spaceship, 200, 200)
//  Generate Enemies
game.onUpdateInterval(750, function on_update_interval() {
    
    rock = sprites.create(img`
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
        `, 0)
    rock.setPosition(scene.screenWidth(), randint(0, scene.screenHeight()))
    rock.setVelocity(-50, 0)
    rock.setKind(SpriteKind.Enemy)
})
