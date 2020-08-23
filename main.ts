//  Setup the Game
info.setScore(0)
info.setLife(3)
//  Setup the Player
let spaceship = sprites.create(img`
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
`)
spaceship.setPosition(10, scene.screenHeight() / 2)
spaceship.setFlag(SpriteFlag.StayInScreen, true)
//  Configure Player Controls
controller.moveSprite(spaceship, 200, 200)
//  Generate Enemies
game.onUpdateInterval(750, function on_update_interval() {
    let rock = sprites.create(img`
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
    `)
    rock.setPosition(scene.screenWidth(), randint(0, scene.screenHeight()))
    rock.setVelocity(-50, 0)
})
//  Shoot Enemies with Projectiles
controller.player1.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function on_button_event_a_pressed() {
    let blast = sprites.createProjectileFromSprite(img`
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
