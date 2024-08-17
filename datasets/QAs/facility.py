


import gurobipy as gp
from gurobipy import GRB


demand = [15, 18, 14, 20]

capacity = [20, 22, 17, 19, 18]

fixedCosts = [12000, 15000, 17000, 13000, 16000]

transCosts = [[4000, 2000, 3000, 2500, 4500],
              [2500, 2600, 3400, 3000, 4000],
              [1200, 1800, 2600, 4100, 3000],
              [2200, 2600, 3100, 3700, 3200]]

plants = range(len(capacity))
warehouses = range(len(demand))
maxFixed = max(fixedCosts)

# OPTIGUIDE DATA CODE GOES HERE
m = gp.Model("facility")
model = m

open = m.addVars(plants,
                 vtype=GRB.BINARY,
                 obj=fixedCosts,
                 name="open")

transport = m.addVars(warehouses, plants, obj=transCosts, name="trans")


m.ModelSense = GRB.MINIMIZE

m.addConstrs(
    (transport.sum('*', p) <= capacity[p]*open[p] for p in plants), "Capacity")


m.addConstrs(
    (transport.sum(w) == demand[w] for w in warehouses),
    "Demand")


m.write('facilityPY.lp')


for p in plants:
    open[p].Start = 1.0

print('Initial guess:')
for p in plants:
    if fixedCosts[p] == maxFixed:
        open[p].Start = 0.0
        print('Closing plant %s' % p)
        break
print('')

m.Params.Method = 2

m.optimize()

# OPTIGUIDE CONSTRAINT CODE GOES HERE

m.update()
m.optimize()

print('\nTOTAL COSTS: %g' % m.ObjVal)
print('SOLUTION:')
for p in plants:
    if open[p].X > 0.99:
        print('Plant %s open' % p)
        for w in warehouses:
            if transport[w, p].X > 0:
                print('  Transport %g units to warehouse %s' %
                      (transport[w, p].X, w))
    else:
        print('Plant %s closed!' % p)