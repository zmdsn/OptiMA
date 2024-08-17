


import sys
import math
import random
from itertools import combinations
import gurobipy as gp
from gurobipy import GRB


def subtourelim(model, where):
    if where == GRB.Callback.MIPSOL:
        vals = model.cbGetSolution(model._vars)
        tour = subtour(vals)
        if len(tour) < n:
            model.cbLazy(gp.quicksum(model._vars[i, j]
                                     for i, j in combinations(tour, 2))
                         <= len(tour)-1)



def subtour(vals):
    edges = gp.tuplelist((i, j) for i, j in vals.keys()
                         if vals[i, j] > 0.5)
    unvisited = list(range(n))
    cycle = range(n+1)  # initial length has 1 more city
    while unvisited:  # true if list is non-empty
        thiscycle = []
        neighbors = unvisited
        while neighbors:
            current = neighbors[0]
            thiscycle.append(current)
            unvisited.remove(current)
            neighbors = [j for i, j in edges.select(current, '*')
                         if j in unvisited]
        if len(cycle) > len(thiscycle):
            cycle = thiscycle
    return cycle

n = 10
random.seed(1)
points = [(random.randint(0, 100), random.randint(0, 100)) for i in range(n)]


dist = {(i, j):
        math.sqrt(sum((points[i][k]-points[j][k])**2 for k in range(2)))
        for i in range(n) for j in range(i)}

# OPTIGUIDE DATA CODE GOES HERE
m = gp.Model()
model = m

vars = m.addVars(dist.keys(), obj=dist, vtype=GRB.BINARY, name='e')
for i, j in list(vars.keys()):
    vars[j, i] = vars[i, j]  # edge in opposite direction




m.addConstrs(vars.sum(i, '*') == 2 for i in range(n))

m._vars = vars
m.Params.LazyConstraints = 1
m.optimize(subtourelim)

# OPTIGUIDE CONSTRAINT CODE GOES HERE

m.update()
m.optimize(subtourelim)

vals = m.getAttr('X', vars)
tour = subtour(vals)
assert len(tour) == n

print('')
print('Optimal tour: %s' % str(tour))
print('Optimal cost: %g' % m.ObjVal)
print('')
m._num_points = n
