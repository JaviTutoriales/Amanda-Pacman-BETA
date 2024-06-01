controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    jugador.vy = -50
    jugador.setImage(assets.image`
        jugadorArriba
    `)
})
function on_left_right_released() {
    jugador.vx = 0
}

function on_up_down_released() {
    jugador.vy = 0
}

controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    jugador.vx = -50
    jugador.setImage(assets.image`
        jugadorIzquierda
    `)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    jugador.vx = 50
    jugador.setImage(assets.image`
        jugadorDerecha
    `)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    jugador.vy = 50
    jugador.setImage(assets.image`
        jugadorAbajo
    `)
})
let jugador : Sprite = null
scene.setBackgroundColor(9)
tiles.setTilemap(tilemap`
    level1
`)
info.setScore(0)
info.setLife(3)
game.splash("Bienvenido a mi Pacman")
//  Crear el jugador
jugador = sprites.create(assets.image`
    jugadorDerecha
`, SpriteKind.Player)
controller.moveSprite(jugador)
controller.up.onEvent(ControllerButtonEvent.Released, on_up_down_released)
controller.down.onEvent(ControllerButtonEvent.Released, on_up_down_released)
controller.left.onEvent(ControllerButtonEvent.Released, on_left_right_released)
controller.right.onEvent(ControllerButtonEvent.Released, on_left_right_released)
//  Crear el fantasma
let fantasma = sprites.create(assets.image`
    fantasma
`, SpriteKind.Enemy)
scene.cameraFollowSprite(jugador)
//  Iniciar función para que el fantasma persiga al jugador
game.onUpdateInterval(500, function on_update_interval() {
    if (jugador.x < fantasma.x) {
        fantasma.vx = -50
    } else if (jugador.x > fantasma.x) {
        fantasma.vx = 50
    }
    
    if (jugador.y < fantasma.y) {
        fantasma.vy = -50
    } else if (jugador.y > fantasma.y) {
        fantasma.vy = 50
    }
    
})
