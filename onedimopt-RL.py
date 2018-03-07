# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import time

import pulp as lp

np.random.seed(10)

MAX_POZITON = 10
ACTIONS = ['plus', 'miners']
EPSILON = 0.9
ALPHA = 0.1
LAMBDA = 0.9
MAX_EPISODES = 100
FRESH_TIME = 0

SETP = 1


# region 线性规划部分代码

def lp_prob():
    prob = lp.LpProblem('OneDimOpt', sense=lp.LpMaximize)

    x = lp.LpVariable('x', lowBound=0)
    # prob += x, 'x'

    cons = 10 - x >= 0
    prob += cons, 'c'
    # prob.addConstraint(cons, 'c')

    obj = lp.lpSum([x, ])
    prob += obj, 'Object'

    prob.solve()

    print(prob)
    for v in prob.variables():  ##变量输出
        print(v.name, "=", v.varValue)

# endregion


def get_env_feedback(S, A):
    if S + A > MAX_POZITON:
        S_ = MAX_POZITON - (S + A - MAX_POZITON)
        R = 0
    elif 0 <= S + A < MAX_POZITON:
        S_ = S + A
        R = 0
    elif S + A < 0:
        S_ = 0
        R = 0
    else:
        S_ = 'end'
        R = 1

    return S_, R


def rl():
    pass


if __name__ == '__main__':
    lp_prob()
