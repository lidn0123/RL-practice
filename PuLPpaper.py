# -*- coding=utf-8 -*-
from pulp import *

REQUIRE = {1: 7,
           2: 5,
           3: 3,
           4: 2,
           5: 2}
PRODUCTS = [1, 2, 3, 4, 5]
LOCATIONS = [1, 2, 3, 4, 5]
CAPACITY = 8

prob = LpProblem('FacilityLocation', LpMinimize)
