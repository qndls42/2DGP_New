__author__ = 'xnote'

import game_framework
import main_state
import title_state
import random
from pico2d import *

global normal_stair

normal_stair = (
    (
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),
    (
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),
    (
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),
    (
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),
    (
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),  # 여기까지 왼쪽으로 올라가는 계단 5가지 경우
    (
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 1),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),
    (
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 1),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),
    (
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),
    (
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),
    (
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 1),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 1),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    )
)

hard_stair = (
    (
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),
    (
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),
    (
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),
    (
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),
    (
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),  # 여기까지 왼쪽으로 올라가는 계단 5가지 경우
    (
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 1),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),
    (
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 1),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),
    (
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),
    (
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    ),
    (
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 1),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 1),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0)
    )
)

global SelStair
SelStair = [normal_stair, hard_stair]


def draw():
    global normal_stair
    # for j in range(9, -1, -1):  # 맨 아래 계단
    #     for i in range(0, 7):
    #         if normal_stair[main_state.Selidx_1][j][i] == 1 or normal_stair[main_state.Selidx_1][j][i] == 2:
    #             main_state.stairImage.draw(main_state.stair1_X + (i * 49), main_state.stair1_Y + ((9-j) * 28))
    #
    # for j in range(9, -1, -1):  # 중간 계단
    #     for i in range(0, 7):
    #         if normal_stair[main_state.Selidx_2][j][i] == 1 or normal_stair[main_state.Selidx_2][j][i] == 2:
    #             main_state.stairImage.draw(main_state.stair2_X + (i * 49), main_state.stair2_Y + ((9-j) * 28))
    #
    # for j in range(9, -1, -1):  # 맨 아래 계단
    #     for i in range(0, 7):
    #         if normal_stair[main_state.Selidx_3][j][i] == 1 or normal_stair[main_state.Selidx_3][j][i] == 2:
    #             main_state.stairImage.draw(main_state.stair3_X + (i * 49), main_state.stair3_Y + ((9-j) * 28))

    for n in range(0, 3):
        for j in range(9, -1, -1):
            for i in range(0, 7):
                if SelStair[title_state.sel][main_state.SelIdx[n]][j][i] == 1 or SelStair[title_state.sel][main_state.SelIdx[n]][j][i] == 2:
                    main_state.stairImage.draw(main_state.Stair_X[n] + (i * 49), main_state.Stair_Y[n] + ((9-j) * 28))
    pass

def update():
    pass
