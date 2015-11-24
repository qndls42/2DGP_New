__author__ = 'xnote'

import game_framework
import store_state
from pico2d import *


name = "TitleState"
title_bg = None
left_sel = None
right_sel = None
mode = None
sel = None
bgm = None


def enter():
    global title_bg, left_sel, right_sel, mode, sel, bgm
    title_bg = load_image('title_bg.png')
    left_sel = load_image('Left_sel.png')
    right_sel = load_image('Right_sel.png')
    mode = load_image('normal.png')

    bgm = load_music('Happy.ogg')
    bgm.set_volume(60)
    bgm.repeat_play()
    sel = 0
    pass


def exit():
    global left_sel, right_sel
    del(left_sel)
    del(right_sel)
    # close_canvas()
    pass


def handle_events():
    global left_sel, right_sel, mode, sel

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):    # 조건이 둘 다 맞으면 실행하도록!
                game_framework.quit()
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    left_sel = load_image('Left_sel_down.png')
                    mode = load_image('normal.png')
                    sel = 0
                    pass
                elif event.key == SDLK_RIGHT:
                    right_sel = load_image('Right_sel_down.png')
                    mode = load_image('hard.png')
                    sel = 1
                    pass
                elif event.key == SDLK_SPACE:
                    game_framework.change_state(store_state)
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_LEFT:
                    left_sel = load_image('Left_sel.png')
                    pass
                elif event.key == SDLK_RIGHT:
                    right_sel = load_image('Right_sel.png')
                    pass
            # elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            #     game_framework.change_state(main_state)
    pass


def draw():
    clear_canvas()
    title_bg.draw(400, 300)
    left_sel.draw(250, 100)
    right_sel.draw(550, 100)
    mode.draw(402, 100)
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass






