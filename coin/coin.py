from random import randint

WIDTH = 400
HEIGHT = 400
score  = 0
game_over = False

fox = Actor("tesshinkun")
fox.pos = 100, 100

coin = Actor("hikari")
coin.pos = 200, 200

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("score: " + str(score), color = "blue", topleft=(10, 10))

    if game_over:
        screen.fill("yellow")
        screen.draw.text("Final score: " + str(score), color = "blue", topleft=(10, 10), fontsize=60)
        clock.schedule(quit, 5.0)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
        fox.x = fox.x - 2
    if keyboard.right:
        fox.x = fox.x + 2
    if keyboard.up:
        fox.y = fox.y - 2
    if keyboard.down:
        fox.y = fox.y + 2

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score = score + 1
        place_coin()    

clock.schedule(time_up, 30.0)

place_coin()
