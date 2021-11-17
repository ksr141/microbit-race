def DrawScreen():
    for Screen_X in range(5):
        if Screen_X != Player_X:
            led.unplot(Screen_X, 4)
        if Road1[Screen_X]:
            led.unplot(Screen_X, Road1_Y - 1)
            led.plot_brightness(Screen_X, Road1_Y, 50)
        if Road2[Screen_X]:
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
    global RandomOpening, Road1, Road1_Y, Score, Road2, Road2_Y
    if Road1_Y == 4:
        RandomOpening = randint(0, 4)
        Road1 = [1, 1, 1, 1, 1]
        Road1[RandomOpening] = 0
        Road1_Y = 0
        for Screen_X2 in range(5):
            if Road1[Screen_X2]:
                led.plot_brightness(Screen_X2, Road1_Y, 50)
        Score += 1
    if Road2_Y == 4:
        RandomOpening = randint(0, 3)
        Road2 = [1, 1, 1, 1, 1]
        Road2[RandomOpening] = 0
        Road2_Y = 0
        for Screen_X3 in range(5):
            if Road2[Screen_X3]:
                led.plot_brightness(Screen_X3, Road2_Y, 50)
        Score += 1

def on_button_pressed_b():
    global Player_X
    if Player_X < 4:
        led.unplot(Player_X, 4)
        Player_X = Player_X + 1
        led.plot(Player_X, 4)
input.on_button_pressed(Button.B, on_button_pressed_b)

RandomOpening = 0
Road2_Y = 0
Road1_Y = 0
Player_X = 0
Road2: List[number] = []
Road1: List[number] = []
Road1 = [1, 1, 1, 0, 1]
Road2 = [1, 0, 1, 1, 1]
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
    if Road1_Y == 4 and Road1[Player_X] == 1:
        game.set_score(Score)
        game.game_over()
    if Road2_Y == 4 and Road2[Player_X] == 1:
        game.set_score(Score)
        game.game_over()
    MakeNewRoad()
    basic.pause(500)
basic.forever(on_forever)
