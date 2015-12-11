__author__ = 'xnote'

import game_framework
import title_state
import store_state
import main_state
from pico2d import *

name = "GameOverState"

score_board = None
game_over_sound = None
best = None
best_score = 0

def enter():
    global score_board, game_over_sound, best_score, best

    store_state.sel_x = 380
    store_state.sel_y = 160
    score_board = load_image('score_board.png')

    game_over_sound = load_wav('game_over.wav')
    game_over_sound.set_volume(60)
    game_over_sound.play(1)

    best = load_image('best.png')

    if main_state.DownCnt > best_score:
        best_score = main_state.DownCnt
    pass


def exit():
    global score_board, game_over_sound

    del score_board
    del game_over_sound
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            del title_state.bgm
            del store_state.bgm
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
                        del title_state.bgm
                        game_framework.change_state(title_state)
                        pass
                    elif store_state.sel_x == 530:
                        del store_state.bgm
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

    best.draw(400, 290)
    if main_state.score_check(best_score) == 0:
        store_state.Num_image.clip_draw(0, 0, 21, 25, 400, 250)
    for i in range(main_state.score_check(best_score)):
            store_state.Num_image.clip_draw(store_state.Num[i] * 21, 0, 21, 25, (400 + int(main_state.score_check(best_score) / 2) * 21) - (i * 21), 250)

    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass
