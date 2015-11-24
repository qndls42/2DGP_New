__author__ = 'xnote'

import game_framework
import title_state
import store_state
import main_state
import start_state
from pico2d import *

name = "GameOverState"

score_board = None


def enter():
    global score_board

    store_state.sel_x = 380
    store_state.sel_y = 160
    score_board = load_image('score_board.png')
    pass


def exit():
    global score_board

    del score_board
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    if store_state.sel_x > 380:
                        store_state.sel_x -= 150
                    pass
                elif event.key == SDLK_RIGHT:
                    if store_state.sel_x <= 380:
                        store_state.sel_x += 150
                    pass
                elif event.key == SDLK_SPACE:
                    if store_state.sel_x == 380:
                        game_framework.change_state(title_state)
                        pass
                    elif store_state.sel_x == 530:
                        game_framework.change_state(store_state)
                        pass
    pass


def draw():
    clear_canvas()
    title_state.title_bg.draw(400, 300)
    score_board.draw(400, 300)
    store_state.sel.draw(store_state.sel_x, store_state.sel_y)

    #=================== 스코어 출력
    if main_state.score_check(main_state.DownCnt) == 0:
        store_state.Num_image.clip_draw(0, 0, 21, 25, 400, 350)
        pass
    else:
        for i in range(main_state.score_check(main_state.DownCnt)):
            store_state.Num_image.clip_draw(store_state.Num[i] * 21, 0, 21, 25, (400 + int(main_state.score_check(main_state.DownCnt) / 2) * 21) - (i * 21), 350)

    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass
