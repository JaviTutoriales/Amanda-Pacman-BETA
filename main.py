def on_up_pressed():
    jugador.vy = -50
    jugador.set_image(assets.image("""
        jugadorArriba
    """))
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_left_right_released():
    jugador.vx = 0
def on_up_down_released():
    jugador.vy = 0

def on_left_pressed():
    jugador.vx = -50
    jugador.set_image(assets.image("""
        jugadorIzquierda
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    jugador.vx = 50
    jugador.set_image(assets.image("""
        jugadorDerecha
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    jugador.vy = 50
    jugador.set_image(assets.image("""
        jugadorAbajo
    """))
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

jugador: Sprite = None
scene.set_background_color(9)
tiles.set_tilemap(tilemap("""
    level1
"""))
info.set_score(0)
info.set_life(3)
game.splash("Bienvenido a mi Pacman")
# Crear el jugador
jugador = sprites.create(assets.image("""
    jugadorDerecha
"""), SpriteKind.player)
controller.move_sprite(jugador)
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_down_released)
controller.down.on_event(ControllerButtonEvent.RELEASED, on_up_down_released)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_right_released)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_left_right_released)
# Crear el fantasma
fantasma = sprites.create(assets.image("""
    fantasma
"""), SpriteKind.enemy)
scene.camera_follow_sprite(jugador)
# Iniciar función para que el fantasma persiga al jugador

def on_update_interval():
    if jugador.x < fantasma.x:
        fantasma.vx = -50
    elif jugador.x > fantasma.x:
        fantasma.vx = 50
    if jugador.y < fantasma.y:
        fantasma.vy = -50
    elif jugador.y > fantasma.y:
        fantasma.vy = 50
game.on_update_interval(500, on_update_interval)
