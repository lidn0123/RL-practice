# -*- coding: utf-8 -*-

import pulp as tf

name = ['apple', 'orange', 'pel', 'pp', 'ew']
# A dictionary of the costs of each of the Ingredients is created
low = {'apple': 1, 'ew': 1, 'orange': 1, 'pel': 1, 'pp': 1}

# A dictionary of the protein percent in each of the Ingredients is created
up = {'apple': 10, 'ew': 10, 'orange': 10, 'pel': 10, 'pp': 10}

prob = tf.LpProblem("The Whiskas Problem", tf.LpMinimize)
x = tf.LpVariable.dicts("Ingr", name, 0)


def get(s):
    return str(s) + 'low'


name1 = list(map(get, name))
name1 = dict(zip(name, name1))


def get(s):
    return str(s) + 'up'


name2 = list(map(get, name))
name2 = dict(zip(name, name2))

for i in name:
    prob += x[i] - low[i] >= 0, name1[i]
    prob += x[i] - up[i] <= 0, name2[i]

prob += tf.lpSum([low[i] * x[i] for i in name]), "Total Cost of Ingredients per can"
# The five constraints are added to 'prob'
prob += tf.lpSum([low[i] * x[i] for i in name]) >= 0, "PercentagesSum"
prob += tf.lpSum([up[i] * x[i] for i in name]) <= 100, "ProteinRequirement"

prob.solve()
print(prob)
for v in prob.variables():  ##变量输出
    print(v.name, "=", v.varValue)
