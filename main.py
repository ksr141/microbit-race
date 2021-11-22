def DrawScreen():
    for Screen_X in range(5):
        if Screen_X != Player_X:
            led.unplot(Screen_X, 4)
        if Screen_X != Road1_Opening:
            led.unplot(Screen_X, Road1_Y - 1)
            led.plot_brightness(Screen_X, Road1_Y, 50)
        if Screen_X != Road2_Opening:
            led.unplot(Screen_X, Road2_Y - 1)
            led.plot_brightness(Screen_X, Road2_Y, 50)

def on_button_pressed_a():
    global Player_X
    if Player_X > 0:
        led.unplot(Player_X, 4)
        Player_X = Player_X - 1
    led.plot(Player_X, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def MakeNewRoad():
    global Road1_Opening, Road1_Y, Score, Road2_Opening, Road2_Y
    if Road1_Y == 4:
        Road1_Opening = randint(0, 4)
        Road1_Y = 0
        for Screen_X2 in range(5):
            if Screen_X2 != Road1_Opening:
                led.plot_brightness(Screen_X2, Road1_Y, 50)
        Score += 10
    if Road2_Y == 4:
        Road2_Opening = randint(0, 4)
        Road2_Y = 0
        for Screen_X3 in range(5):
            if Screen_X3 != Road2_Opening:
                led.plot_brightness(Screen_X3, Road2_Y, 50)
        Score += 10

def on_button_pressed_b():
    global Player_X
    if Player_X < 4:
        led.unplot(Player_X, 4)
        Player_X = Player_X + 1
        led.plot(Player_X, 4)
input.on_button_pressed(Button.B, on_button_pressed_b)

Road2_Y = 0
Road1_Y = 0
Player_X = 0
Road2_Opening = 0
Road1_Opening = 0
Road1_Opening = randint(0, 4)
Road2_Opening = randint(0, 4)
Player_X = 2
Road1_Y = 1
Road2_Y = -1
Score = 0
led.plot(Player_X, 4)

def on_forever():
    global Road1_Y, Road2_Y
    Road1_Y = Road1_Y + 1
    Road2_Y = Road2_Y + 1
    DrawScreen()
    if Road1_Y == 4 and Road1_Opening != Player_X:
        game.set_score(Score)
        game.game_over()
    if Road2_Y == 4 and Road2_Opening != Player_X:
        game.set_score(Score)
        game.game_over()
    MakeNewRoad()
    basic.pause(500)
basic.forever(on_forever)
