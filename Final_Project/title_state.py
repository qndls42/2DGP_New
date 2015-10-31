__author__ = 'xnote'

import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image
    open_canvas()
    image = load_image('menu.png')
    pass


def exit():
    global image
    del(image)
    # close_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):    # 조건이 둘 다 맞으면 실행하도록!
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)
    pass


def draw():
    global image
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass



def update():
    pass


def pause():
    pass


def resume():
    pass






