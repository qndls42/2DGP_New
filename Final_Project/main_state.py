__author__ = 'xnote'

from pico2d import *

import game_framework
import title_state
import store_state
import start_state
import gameover_state
import stairs
import random

name = "MainState"

IsOver = None

boy = None
current_x = None
current_y = None

background = None
background1_1 = None
background1_2 = None
bg_Y = None
bg1_Y = None
bg2_Y = None

stairImage = None
Selidx_1 = None     # 계단
Selidx_2 = None     # 계단
Selidx_3 = None     # 계단
SelIdx = None
stair1_X = None
stair1_Y = None
stair2_X = None
stair2_Y = None
stair3_X = None
stair3_Y = None
Stair_X = None
Stair_Y = None

LifeFlag = None
StopFlag = None

time_frame = None
time = None
current_time = 0.0

DownCnt = None


class Time:
    gauge_image = None
    ticking = None
    ticking_break = None

    def __init__(self):
        self.x, self.y = 400, 500
        self.width = 158
        self.sub = 2
        self.gauge_image = load_image('time_gauge.png')

        if Time.ticking is None:
            Time.ticking = load_wav('time_ticking.wav')
            Time.ticking.set_volume(32)
        if Time.ticking_break is None:
            Time.ticking_break = load_wav('ticking_break.wav')
            Time.ticking_break.set_volume(32)

    def update(self):
        if not IsOver and DownCnt > 0:
            self.width -= self.sub

    def draw(self):
        self.gauge_image.clip_draw_to_origin(0, 0, self.width, 26, 243, 500)


class Boy:
    image = None
    dead_sound = None
    walk_sound = None

    RIGHT_STAND, LEFT_STAND, RIGHT_RUN, LEFT_RUN, DEAD = 4, 3, 2, 1, 0

    def __init__(self):
        self.x, self.y = 450, 200
        self.frame = 0
        self.run_frames = 0
        self.stand_frames = 0
        self.dead_frames = 0
        self.state = self.LEFT_STAND
        self.image = load_image('player.png')
        self.dir = 1  # 왼쪽을 향하고 있는 상태 = 1
        if Boy.dead_sound is None:
            Boy.dead_sound = load_wav('dead_sound.wav')
            Boy.dead_sound.set_volume(32)
            pass
        if Boy.walk_sound is None:
            Boy.walk_sound = load_wav('walk_sound.wav')
            Boy.walk_sound.set_volume(32)
            pass

    def handle_left_run(self):
        self.run_frames += 1
        if self.run_frames == 3:
            self.state = self.LEFT_STAND
            self.stand_frames = 0

    def handle_left_stand(self):
        self.stand_frames += 1

    def handle_right_run(self):
        self.run_frames += 1
        if self.run_frames == 3:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0

    def handle_right_stand(self):
        self.stand_frames += 1

    def handle_dead(self):
        global LifeFlag, IsOver

        if self.dead_frames == 9 and LifeFlag == -1:
            self.dead_frames = -1
        elif self.dead_frames == 9 and LifeFlag == 1:
            self.state = self.LEFT_STAND
            self.stand_frames = 0
            boy.x = current_x
            boy.y = current_y
            IsOver = False
            LifeFlag = -1
            store_state.Item_Life = load_image('usedItem_Life.png')
            self.dead_frames = 0
            pass
        else:
            self.dead_frames += 1
        pass

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand,
        DEAD: handle_dead
    }

    def update(self):
        if self.state == self.LEFT_RUN or self.state == self.RIGHT_RUN:
            self.frame = self.run_frames % 6
        elif self.state == self.LEFT_STAND or self.state == self.RIGHT_STAND:
            self.frame = self.stand_frames % 7
        elif self.state == self.DEAD and self.dead_frames != 9:     # 한번만 실행하기위해
            self.frame = self.dead_frames % 9
            pass

        self.handle_state[self.state](self)

    def draw(self):
        if self.state == self.LEFT_RUN or self.state == self.RIGHT_RUN:
            self.image.clip_draw(self.frame * 96, self.state * 148, 86, 136, self.x, self.y)
        elif self.state == self.LEFT_STAND or self.state == self.RIGHT_STAND:
            self.image.clip_draw(self.frame * 96, self.state * 145, 86, 136, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 96, self.state * 145, 86, 140, self.x, self.y)
            pass

    def dead(self):
        self.dead_sound.play()

    def walk(self):
        self.walk_sound.play()


def enter():
    global boy, time
    global background, background1_1, background1_2
    global bg_Y, bg1_Y, bg2_Y
    global stairImage, SelIdx, Selidx_1, Selidx_2, Selidx_3
    global stair1_X, stair1_Y, stair2_X, stair2_Y, stair3_X, stair3_Y, Stair_X, Stair_Y
    global DownCnt, IsOver
    global time_frame

    IsOver = False
    DownCnt = 0

    stairImage = load_image('stair.png')
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
    time = Time()

    bg_Y = 650
    bg1_Y = bg_Y + 1458
    bg2_Y = bg1_Y + 1516
    background = load_image('background.png')
    background1_1 = load_image('background1.png')
    background1_2 = load_image('background1.png')

    time_frame = load_image('time_frame.png')
    pass


def exit():
    global boy, time, background
    del background
    del boy
    del time
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
    global LifeFlag, StopFlag, current_time
    global current_x, current_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            del title_state.bgm
            del store_state.bgm
            game_framework.quit()
        elif not IsOver:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    boy.run_frames = 0
                    boy.state = boy.LEFT_RUN
                    DownCnt += 1

                    over_check(1)

                    if DownCnt % 20 == 0:
                        time.sub += 2

                    if IsOver:
                        # 캐릭터만 움직임
                        current_x = boy.x
                        current_y = boy.y
                        boy.x -= 57
                        boy.y += 23
                        pass
                    else:
                        boy.walk()
                        if DownCnt == 1:
                            boy.x -= 57
                            boy.y += 23
                        else:
                            for i in range(0, 3):
                                Stair_X[i] += 50
                                Stair_Y[i] -= 28
                            if DownCnt > 1:
                                if (bg1_Y + 758) < -1:
                                    bg1_Y = bg2_Y + 1516
                                elif (bg2_Y + 758) < -1:
                                    bg2_Y = bg1_Y + 1516
                                if DownCnt < 47:
                                    bg2_Y -= 20
                                    bg1_Y -= 20
                                    bg_Y -= 20
                                else:
                                    bg2_Y -= 10
                                    bg1_Y -= 10
                                    bg_Y -= 10
                        pass

                    if time.width < 316 - 25 and StopFlag != 0:
                        time.width += 25
                    elif 316 - 25 <= time.width <= 316 and StopFlag != 0:
                        time.width = 316

                    if Stair_Y[1] + 242 < 0:
                        SelIdx[1] = random.randint(0, 9)
                        Stair_Y[1] = Stair_Y[0] + (10 * 28)
                    elif Stair_Y[2] + 242 < 0:
                        SelIdx[2] = random.randint(0, 9)
                        Stair_Y[2] = Stair_Y[1] + (10 * 28)
                    elif Stair_Y[0] + 242 < 0:
                        SelIdx[0] = random.randint(0, 9)
                        Stair_Y[0] = Stair_Y[2] + (10 * 28)
                    pass
                elif event.key == SDLK_RIGHT:
                    DownCnt += 1
                    boy.run_frames = 0
                    boy.state = boy.RIGHT_RUN

                    over_check(2)

                    if DownCnt % 20 == 0:
                        time.sub += 2

                    if IsOver:
                        current_x = boy.x
                        current_y = boy.y
                        boy.x += 57
                        boy.y += 23
                        pass
                    else:
                        boy.walk()
                        if DownCnt == 1:
                            boy.x += 57
                            boy.y += 23
                        else:
                            for i in range(0, 3):
                                Stair_X[i] -= 50
                                Stair_Y[i] -= 28
                            if DownCnt > 1:
                                if (bg1_Y + 758) < -1:
                                    bg1_Y = bg2_Y + 1516
                                elif (bg2_Y + 758) < -1:
                                    bg2_Y = bg1_Y + 1516
                                if DownCnt < 47:
                                    bg2_Y -= 20
                                    bg1_Y -= 20
                                    bg_Y -= 20
                                else:
                                    bg2_Y -= 10
                                    bg1_Y -= 10
                                    bg_Y -= 10
                        pass

                        if time.width < 316 - 25 and StopFlag != 0:
                            time.width += 25
                        elif 316 - 25 <= time.width <= 316 and StopFlag != 0:
                            time.width = 316

                    if Stair_Y[1] + 242 < 0:
                        SelIdx[1] = random.randint(0, 9)
                        Stair_Y[1] = Stair_Y[0] + (10 * 28)
                    elif Stair_Y[2] + 242 < 0:
                        SelIdx[2] = random.randint(0, 9)
                        Stair_Y[2] = Stair_Y[1] + (10 * 28)
                    elif Stair_Y[0] + 242 < 0:
                        SelIdx[0] = random.randint(0, 9)
                        Stair_Y[0] = Stair_Y[2] + (10 * 28)
                elif DownCnt > 0 and event.key == SDLK_c and StopFlag != -1:
                    StopFlag = 0
                    store_state.Item_Stop = load_image('usedItem_Stop.png')
                    time.gauge_image = load_image('time_gauge_stop.png')
                    current_time = get_time()
                    time.ticking.play(3)
                    Time.ticking.set_volume(32)
                    pass


def update():
    global DownCnt, current_time, StopFlag
    boy.update()

    # Stop 아이템 사용시 코드
    if StopFlag != 0:
        time.update()
    elif get_time() - current_time >= 5.0:
        StopFlag = -1
        time.gauge_image = load_image('time_gauge.png')
        time.ticking_break.play()

    time_over()

    if IsOver and boy.dead_frames == -1:
        start_state.TotalMoney += DownCnt
        game_framework.change_state(gameover_state)
    pass


def over_check(event):   # 게임 종료 체크
    global Selidx_1, Selidx_2, Selidx_3, SelIdx
    global IsOver, DownCnt
    global LifeFlag

    if DownCnt == 1 and event == 2:
        IsOver = True
        DownCnt -= 1
        boy.state = boy.DEAD
        boy.dead()
        title_state.bgm.set_volume(0)
        title_state.bgm.stop()

    elif not IsOver and DownCnt > 1:
        for n in range(0, 3):
            for j in range(9, -1, -1):
                for i in range(0, 7):
                    if (Stair_X[n] + (i * 49) - 25) < boy.x < (Stair_X[n] + (i * 49) + 25) and Stair_Y[n] + ((9 - j) * 28) - 14 < boy.y - 70 <= Stair_Y[n] + ((9 - j) * 28) + 14:
                        if stairs.SelStair[title_state.sel][SelIdx[n]][j - 1][i - 1] == 1:  # 서있던 계단의 왼쪽 위 계단이 진짜일 경우
                            if event == 1:  # 왼쪽 방향키 눌렀을 때
                                pass
                            elif event == 2:   # 오른쪽 방향키 눌렀을 때
                                # 게임 종료
                                IsOver = True
                                DownCnt -= 1
                                boy.state = boy.DEAD
                                boy.dead()
                                if LifeFlag == -1:
                                    time.ticking.set_volume(0)
                                    title_state.bgm.set_volume(0)
                                    title_state.bgm.stop()
                                pass
                        elif stairs.SelStair[title_state.sel][SelIdx[n]][j - 1][i + 1] == 1:  # 서있던 계단의 오른쪽 위 계단이 진짜일 경우
                            if event == 1:
                                # 게임 종료
                                IsOver = True
                                DownCnt -= 1
                                boy.state = boy.DEAD
                                boy.dead()
                                if LifeFlag == -1:
                                    time.ticking.set_volume(0)
                                    title_state.bgm.set_volume(0)
                                    title_state.bgm.stop()
                            elif event == 2:
                                pass
                        else:
                            IsOver = True
                            DownCnt -= 1
                            boy.state = boy.DEAD
                            boy.dead()
                            if LifeFlag == -1:
                                time.ticking.set_volume(0)
                                title_state.bgm.set_volume(0)
                                title_state.bgm.stop()
                        pass


def time_over():
    global IsOver

    if time.width <= 0 and not IsOver:     # 시간이 모두 경과
        IsOver = True
        boy.state = boy.DEAD
        boy.dead_sound.set_volume(32)
        boy.dead()
        title_state.bgm.set_volume(0)
        title_state.bgm.stop()


def score_check(num):      # 게임 스코어 및 게임 머니 체크
    store_state.Num = []
    temp_num = num
    count = 0
    while temp_num > 0:
        store_state.Num.append(int(temp_num % 10))
        temp_num = int(temp_num / 10)
        count += 1
    return count
    pass


def Item_draw():
    store_state.Item_Life.draw(60, 50)
    store_state.Item_Stop.draw(180, 50)


def draw():
    clear_canvas()
    background.draw(400, bg_Y)
    background1_1.draw(400, bg1_Y)
    background1_2.draw(400, bg2_Y)

    stairs.draw()
    boy.draw()
    time.draw()
    time_frame.draw(400, 513)
    Item_draw()

     #=================== 스코어 출력
    if score_check(DownCnt) == 0:
        store_state.Num_image.clip_draw(0, 0, 21, 25, 270, 470)
        pass
    else:
        for i in range(score_check(DownCnt)):
            store_state.Num_image.clip_draw(store_state.Num[i] * 21, 0, 21, 25, (270 + int(score_check(DownCnt) / 2) * 21) - (i * 21), 470)

    update_canvas()
    delay(0.08)
    pass
