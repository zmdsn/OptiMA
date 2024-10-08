


import gurobipy as gp
from gurobipy import GRB



categories, minNutrition, maxNutrition = gp.multidict({
    'calories': [1800, 2200],
    'protein':  [91, GRB.INFINITY],
    'fat':      [0, 65],
    'sodium':   [0, 1779]})

foods, cost = gp.multidict({
    'hamburger': 2.49,
    'chicken':   2.89,
    'hot dog':   1.50,
    'fries':     1.89,
    'macaroni':  2.09,
    'pizza':     1.99,
    'salad':     2.49,
    'milk':      0.89,
    'ice cream': 1.59})

nutritionValues = {
    ('hamburger', 'calories'): 410,
    ('hamburger', 'protein'):  24,
    ('hamburger', 'fat'):      26,
    ('hamburger', 'sodium'):   730,
    ('chicken',   'calories'): 420,
    ('chicken',   'protein'):  32,
    ('chicken',   'fat'):      10,
    ('chicken',   'sodium'):   1190,
    ('hot dog',   'calories'): 560,
    ('hot dog',   'protein'):  20,
    ('hot dog',   'fat'):      32,
    ('hot dog',   'sodium'):   1800,
    ('fries',     'calories'): 380,
    ('fries',     'protein'):  4,
    ('fries',     'fat'):      19,
    ('fries',     'sodium'):   270,
    ('macaroni',  'calories'): 320,
    ('macaroni',  'protein'):  12,
    ('macaroni',  'fat'):      10,
    ('macaroni',  'sodium'):   930,
    ('pizza',     'calories'): 320,
    ('pizza',     'protein'):  15,
    ('pizza',     'fat'):      12,
    ('pizza',     'sodium'):   820,
    ('salad',     'calories'): 320,
    ('salad',     'protein'):  31,
    ('salad',     'fat'):      12,
    ('salad',     'sodium'):   1230,
    ('milk',      'calories'): 100,
    ('milk',      'protein'):  8,
    ('milk',      'fat'):      2.5,
    ('milk',      'sodium'):   125,
    ('ice cream', 'calories'): 330,
    ('ice cream', 'protein'):  8,
    ('ice cream', 'fat'):      10,
    ('ice cream', 'sodium'):   180}

# OPTIGUIDE DATA CODE GOES HERE
m = gp.Model("diet")
model = m

buy = m.addVars(foods, name="buy")


m.setObjective(buy.prod(cost), GRB.MINIMIZE)


m.addConstrs((gp.quicksum(nutritionValues[f, c] * buy[f] for f in foods)
             == [minNutrition[c], maxNutrition[c]]
             for c in categories), "_")



def printSolution():
    if m.status == GRB.OPTIMAL:
        print('\nCost: %g' % m.ObjVal)
        print('\nBuy:')
        for f in foods:
            if buy[f].X > 0.0001:
                print('%s %g' % (f, buy[f].X))
    else:
        print('No solution')


m.optimize()

# OPTIGUIDE CONSTRAINT CODE GOES HERE

m.update()
m.optimize()
printSolution()

print('\nAdding constraint: at most 6 servings of dairy')
m.addConstr(buy.sum(['milk', 'ice cream']) <= 6, "limit_dairy")

m.optimize()

# OPTIGUIDE CONSTRAINT CODE GOES HERE

m.update()
m.optimize()
printSolution()