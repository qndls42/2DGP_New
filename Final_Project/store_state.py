__author__ = 'xnote'

import game_framework
import main_state
import title_state
import start_state
from pico2d import *


name = "StoreState"
store = None
Item_Life = None
Item_Stop = None
GameStart = None
Num_image = None
Num = None
sel = None
coin_image = None
coin_sound = None
sel_x, sel_y = None, None
bgm = None


def enter():
    global store, Item_Life, Item_Stop, sel, sel_x, sel_y, GameStart, Num_image, Num, coin_image
    global coin_sound, bgm

    store = load_image('store.png')
    Item_Life = load_image('usedItem_Life.png')
    Item_Stop = load_image('usedItem_Stop.png')
    GameStart = load_image('GameStart.png')
    sel = load_image('select.png')
    Num_image = load_image('Num_create.png')
    coin_image = load_image('coin.png')

    coin_sound = load_wav('coin_sound.wav')
    coin_sound.set_volume(35) # 원 볼륨

    if (title_state.bgm.get_volume()) == 0:
        bgm = load_music('Happy.ogg')
        bgm.set_volume(60) # 원 볼륨
        bgm.repeat_play()

    Num = []
    sel_x, sel_y = 390, 195

    main_state.LifeFlag = -1
    main_state.StopFlag = -1
    pass


def exit():
    global store, sel, GameStart

    pass


def handle_events():
    global sel, sel_x, sel_y, Item_Life, Item_Stop, bgm

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            del title_state.bgm
            del bgm
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    if sel_x > 390 and sel_y == 195:
                        sel_x -= 110
                    pass
                elif event.key == SDLK_RIGHT:
                    if sel_x < 500 and sel_y == 195:
                        sel_x += 110
                    pass
                elif event.key == SDLK_SPACE:
                    if sel_y == 90:
                        game_framework.push_state(main_state)
                    elif sel_y == 195:
                        if sel_x == 390:
                            main_state.LifeFlag = buy(main_state.LifeFlag)
                            if main_state.LifeFlag == 1:
                                Item_Life = load_image('Item_Life.png')
                            else:
                                Item_Life = load_image('usedItem_Life.png')
                            pass
                        elif sel_x == 500:
                            main_state.StopFlag = buy(main_state.StopFlag)
                            if main_state.StopFlag == 1:
                                Item_Stop = load_image('Item_Stop.png')
                            else:
                                Item_Stop = load_image('usedItem_Stop.png')
                            pass
                elif event.key == SDLK_DOWN:
                    if sel_y > 90:
                        sel_x = 460
                        sel_y -= 105
                elif event.key == SDLK_UP:
                    if sel_y < 195:
                        sel_x = 390
                        sel_y += 105

    pass


def draw():
    clear_canvas()
    title_state.title_bg.draw(400, 300)
    store.draw(400, 300)

    Item_Life.draw(351, 225)
    Item_Stop.draw(461, 225)

    for i in range(2):
        Num_image.clip_draw(21, 0, 21, 25, 331 + (i * 110), 175)
        Num_image.clip_draw(0, 0, 21, 25, 350 + (i * 110), 175)
        Num_image.clip_draw(0, 0, 21, 25, 371 + (i * 110), 175)
    GameStart.draw(401, 120)
    sel.draw(sel_x, sel_y) # 화살표

    #=================== 코인 출력
    if main_state.score_check(start_state.TotalMoney) == 0:
        Num_image.clip_draw(0, 0, 21, 25, 400, 350)
        pass
    else:
        for i in range(main_state.score_check(start_state.TotalMoney)):
            Num_image.clip_draw(Num[i] * 21, 0, 21, 25, (400 + int(main_state.score_check(start_state.TotalMoney) / 2) * 21) - (i * 21), 350)

    coin_image.draw((400 + int(main_state.score_check(start_state.TotalMoney) / 2) * 21) + 50, 350)
    update_canvas()
    pass


def buy(flag):
    if start_state.TotalMoney - 100 >= 0 and flag == -1:
        flag *= -1
        start_state.TotalMoney -= 100
        coin_sound.play()
    elif flag == 1:
        flag *= -1
        start_state.TotalMoney += 100
        coin_sound.play()


    return flag


def update():
    pass


def pause():
    pass


def resume():
    pass