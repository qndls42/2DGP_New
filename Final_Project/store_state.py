__author__ = 'xnote'

import game_framework
import main_state
import title_state
from pico2d import *


name = "TitleState"
title_bg = None
store = None
Item_Hero = None
Item_Life = None
Item_Stop = None
GameStart = None

sel = None
sel_x, sel_y = None, None

def enter():
    global title_bg, store, Item_Hero, Item_Life, Item_Stop, sel, sel_x, sel_y, GameStart
    title_bg = load_image('menu.png')
    store = load_image('store.png')
    Item_Hero = load_image('Item_Hero.png')
    Item_Life = load_image('Item_Life.png')
    Item_Stop = load_image('Item_Stop.png')
    GameStart = load_image('GameStart.png')
    sel = load_image('select.png')
    sel_x, sel_y = 330, 170
    pass


def exit():
    global title_bg, Item_Hero, Item_Life, Item_Stop, store, sel, GameStart
    del(title_bg)
    del(store)
    del(Item_Hero)
    del(Item_Life)
    del(Item_Stop)
    del(GameStart)
    del(sel)
    # close_canvas()
    pass


def handle_events():
    global sel, sel_x, sel_y, Item_Hero, Item_Life, Item_Stop

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):    # 조건이 둘 다 맞으면 실행하도록!
                game_framework.change_state(title_state)
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    if sel_x > 330:
                        sel_x -= 110
                    pass
                elif event.key == SDLK_RIGHT:
                    if sel_x < 550:
                        sel_x += 110
                    pass
                elif event.key == SDLK_SPACE:
                    if sel_y == 90:
                        game_framework.change_state(main_state)
                    elif sel_y == 170:
                        if sel_x == 330:
                            main_state.HeroFlag *= -1
                            if main_state.HeroFlag == 1:
                                Item_Hero = load_image('usedItem_Hero.png')
                            else:
                                Item_Hero = load_image('Item_Hero.png')
                            pass
                        elif sel_x == 440:
                            main_state.LifeFlag *= -1
                            if main_state.LifeFlag == 1:
                                Item_Life = load_image('usedItem_Life.png')
                            else:
                                Item_Life = load_image('Item_Life.png')
                            pass
                        elif sel_x == 550:
                            main_state.StopFlag *= -1
                            if main_state.StopFlag == 1:
                                Item_Stop = load_image('usedItem_Stop.png')
                            else:
                                Item_Stop = load_image('Item_Stop.png')
                            pass
                elif event.key == SDLK_DOWN:
                    if sel_y > 90:
                        sel_x = 460
                        sel_y -= 80
                elif event.key == SDLK_UP:
                    if sel_y < 170:
                        sel_x = 330
                        sel_y += 80

            # elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            #     game_framework.change_state(main_state)
    pass


def draw():
    clear_canvas()
    title_bg.draw(400, 300)
    store.draw(400, 300)
    Item_Hero.draw(291, 200)
    Item_Life.draw(401, 200)
    Item_Stop.draw(511, 200)
    GameStart.draw(401, 120)
    sel.draw(sel_x, sel_y)
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass