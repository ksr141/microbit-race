function DrawScreen () {
    for (let Screen_X = 0; Screen_X <= 4; Screen_X++) {
        if (Screen_X != Player_X) {
            led.unplot(Screen_X, 4)
        }
        if (Road1[Screen_X]) {
            led.unplot(Screen_X, Road1_Y - 1)
            led.plotBrightness(Screen_X, Road1_Y, 50)
        }
        if (Road2[Screen_X]) {
            led.unplot(Screen_X, Road2_Y - 1)
            led.plotBrightness(Screen_X, Road2_Y, 50)
        }
    }
}
input.onButtonPressed(Button.A, function () {
    if (Player_X > 0) {
        led.unplot(Player_X, 4)
        Player_X = Player_X - 1
    }
    led.plot(Player_X, 4)
})
function MakeNewRoad () {
    if (Road1_Y == 4) {
        RandomOpening = randint(0, 4)
        Road1 = [
        1,
        1,
        1,
        1,
        1
        ]
        Road1[RandomOpening] = 0
        Road1_Y = 0
        for (let Screen_X = 0; Screen_X <= 4; Screen_X++) {
            if (Road1[Screen_X]) {
                led.plotBrightness(Screen_X, Road1_Y, 50)
            }
        }
        Score += 1
    }
    if (Road2_Y == 4) {
        RandomOpening = randint(0, 3)
        Road2 = [
        1,
        1,
        1,
        1,
        1
        ]
        Road2[RandomOpening] = 0
        Road2_Y = 0
        for (let Screen_X = 0; Screen_X <= 4; Screen_X++) {
            if (Road2[Screen_X]) {
                led.plotBrightness(Screen_X, Road2_Y, 50)
            }
        }
        Score += 1
    }
}
input.onButtonPressed(Button.B, function () {
    if (Player_X < 4) {
        led.unplot(Player_X, 4)
        Player_X = Player_X + 1
        led.plot(Player_X, 4)
    }
})
let RandomOpening = 0
let Road2_Y = 0
let Road1_Y = 0
let Player_X = 0
let Road2: number[] = []
let Road1: number[] = []
Road1 = [
1,
1,
1,
0,
1
]
Road2 = [
1,
0,
1,
1,
1
]
Player_X = 2
Road1_Y = 1
Road2_Y = -1
let Score = 0
led.plot(Player_X, 4)
basic.forever(function () {
    Road1_Y = Road1_Y + 1
    Road2_Y = Road2_Y + 1
    DrawScreen()
    if (Road1_Y == 4 && Road1[Player_X] == 1) {
        game.setScore(Score)
        game.gameOver()
    }
    if (Road2_Y == 4 && Road2[Player_X] == 1) {
        game.setScore(Score)
        game.gameOver()
    }
    MakeNewRoad()
    basic.pause(500)
})
