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
