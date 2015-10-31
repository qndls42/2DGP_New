__author__ = 'xnote'

import random

from pico2d import *

import game_framework
import title_state
import stairs

name = "MainState"


IsOver = None

boy = None
background = None
background1_1 = None
background1_2 = None

bg_Y = None
bg1_Y = None
bg2_Y = None
stairImage = None
Selidx_1 = None
Selidx_2 = None
Selidx_3 = None
SelIdx = None

stair1_X = None
stair1_Y = None
stair2_X = None
stair2_Y = None
stair3_X = None
stair3_Y = None
Stair_X = None
Stair_Y = None

DownCnt = None


class Boy:
    image = None

    RIGHT_STAND, LEFT_STAND, RIGHT_RUN, LEFT_RUN = 4, 3, 2, 1

    def __init__(self):
        self.x, self.y = 450, 200
        self.frame = 0
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.LEFT_STAND
        self.image = load_image('player.png')
        self.dir = 1  # 왼쪽을 향하고 있는 상태 = 1

    def handle_left_run(self):
        self.run_frames += 1
        if self.run_frames == 3:
            self.state = self.LEFT_STAND
            self.stand_frames = 0

    def handle_left_stand(self):
        self.stand_frames += 1

        # if self.stand_frames == 50:
        #     self.state = self.LEFT_RUN
        #     self.run_frames = 0

    def handle_right_run(self):
        self.run_frames += 1
        if self.run_frames == 3:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0

    def handle_right_stand(self):
        self.stand_frames += 1
        # if self.stand_frames == 50:
        #     self.state = self.RIGHT_RUN
        #     self.run_frames = 0

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand
    }

    def update(self):
        # fill here
        self.frame = (self.frame + 1) % 6
        self.handle_state[self.state](self)

    def draw(self):
        if self.state == self.LEFT_RUN or self.state == self.RIGHT_RUN:
            self.image.clip_draw(self.frame * 96, self.state * 148, 86, 136, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 96, self.state * 145, 86, 136, self.x, self.y)


def enter():
    global boy
    global background, background1_1, background1_2
    global bg_Y, bg1_Y, bg2_Y
    global stairImage, SelIdx, Selidx_1, Selidx_2, Selidx_3
    global stair1_X, stair1_Y, stair2_X, stair2_Y, stair3_X, stair3_Y, Stair_X, Stair_Y
    global DownCnt, IsOver

    IsOver = False
    DownCnt = 0
    stair1_X, stair1_Y = 250, 150
    stair2_X, stair2_Y = 250, 430
    stair3_X, stair3_Y = 250, 710
    Stair_X = [stair1_X, stair2_X, stair3_X]
    Stair_Y = [stair1_Y, stair2_Y, stair3_Y]

    Selidx_1 = random.randint(0, 4)
    Selidx_2 = random.randint(0, 9)
    Selidx_3 = random.randint(0, 9)
    SelIdx = [Selidx_1, Selidx_2, Selidx_3]

    boy = Boy()
    bg_Y = 650
    bg1_Y = bg_Y + 1458
    bg2_Y = bg1_Y + 1516
    background = load_image('background.png')
    background1_1 = load_image('background1.png')
    background1_2 = load_image('background1.png')
    stairImage = load_image('stair.png')
    pass


def exit():
    global boy
    del (boy)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global background, background1_1, background1_2
    global bg_Y, bg1_Y, bg2_Y, DownCnt
    global stairImage, Selidx_1, Selidx_2, Selidx_3, SelIdx
    global stair1_X, stair1_Y, stair2_X, stair2_Y, stair3_X, stair3_Y, Stair_X, Stair_Y
    global IsOver


    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        elif not IsOver:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    boy.run_frames = 0
                    boy.state = boy.LEFT_RUN
                    DownCnt += 1
                    if DownCnt == 1:
                        boy.x -= 57
                        boy.y += 23
                    else:
                        for i in range(0, 3):
                            Stair_X[i] += 50
                            Stair_Y[i] -= 28
                        # stair1_X += 50
                        # stair1_Y -= 28
                        # stair2_X += 50
                        # stair2_Y -= 28
                        # stair3_X += 50
                        # stair3_Y -= 28
                        pass
                    if DownCnt > 1:
                        if (bg1_Y + 758) < -1:
                            bg1_Y = bg2_Y + 1516
                        elif (bg2_Y + 758) < -1:
                            bg2_Y = bg1_Y + 1516
                        bg2_Y -= 28
                        bg1_Y -= 28
                        bg_Y -= 28
                    if Stair_Y[1] + 242 < 0:
                        SelIdx[1] = random.randint(0, 9)
                        Stair_Y[1] = Stair_Y[0] + (10 * 28)
                    elif Stair_Y[2] + 242 < 0:
                        SelIdx[2] = random.randint(0, 9)
                        Stair_Y[2] = Stair_Y[1] + (10 * 28)
                    elif Stair_Y[0] + 242 < 0:
                        SelIdx[0] = random.randint(0, 9)
                        Stair_Y[0] = Stair_Y[2] + (10 * 28)

                    # check()
                    pass
                elif event.key == SDLK_RIGHT:
                    DownCnt += 1
                    if DownCnt == 1:
                        boy.x += 57
                        boy.y += 23
                    else:
                        for i in range(0, 3):
                            Stair_X[i] -= 50
                            Stair_Y[i] -= 28
                        # stair1_X -= 50
                        # stair1_Y -= 28
                        # stair2_X -= 50
                        # stair2_Y -= 28
                        # stair3_X -= 50
                        # stair3_Y -= 28
                        pass
                    boy.run_frames = 0
                    boy.state = boy.RIGHT_RUN
                    if DownCnt > 1:
                        if (bg1_Y + 758) < -1:
                            bg1_Y = bg2_Y + 1516
                        elif (bg2_Y + 758) < -1:
                            bg2_Y = bg1_Y + 1516
                        bg2_Y -= 28
                        bg1_Y -= 28
                        bg_Y -= 28
                    if Stair_Y[1] + 242 < 0:
                        SelIdx[1] = random.randint(0, 9)
                        Stair_Y[1] = Stair_Y[0] + (10 * 28)
                    elif Stair_Y[2] + 242 < 0:
                        SelIdx[2] = random.randint(0, 9)
                        Stair_Y[2] = Stair_Y[1] + (10 * 28)
                    elif Stair_Y[0] + 242 < 0:
                        SelIdx[0] = random.randint(0, 9)
                        Stair_Y[0] = Stair_Y[2] + (10 * 28)

    check()



def update():
    boy.update()
    pass


def check():
    global stair1_X, stair1_Y, stair2_X, stair2_Y, stair3_X, stair3_Y, Stair_X, Stair_Y
    global Selidx_1, Selidx_2, Selidx_3, SelIdx
    global IsOver

    if DownCnt > 0:
        for n in range(0, 3):
            for j in range(9, -1, -1):
                for i in range(0, 7):
                    if (Stair_X[n] + (i * 49) - 25) < boy.x < (Stair_X[n] + (i * 49) + 25) and Stair_Y[n] + ((9 - j) * 28) - 14 < boy.y - 70 <= Stair_Y[n] + ((9 - j) * 28) + 14:
                        if stairs.normal_stair[SelIdx[n]][j][i] == 0:
                            IsOver = True

        for i in range(0, 3):
            if boy.x < (Stair_X[i] - 25) or boy.x > (Stair_X[i] + 318):
                IsOver = True


def draw():
    clear_canvas()
    background.draw(400, bg_Y)
    background1_1.draw(400, bg1_Y)
    background1_2.draw(400, bg2_Y)

    stairs.draw()
    boy.draw()
    update_canvas()
    delay(0.1)
    pass
