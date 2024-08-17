


import gurobipy as gp
from gurobipy import GRB
import sys

shifts, shiftRequirements = gp.multidict({
    "Mon1":  3,
    "Tue2":  2,
    "Wed3":  4,
    "Thu4":  4,
    "Fri5":  5,
    "Sat6":  6,
    "Sun7":  5,
    "Mon8":  2,
    "Tue9":  2,
    "Wed10": 3,
    "Thu11": 4,
    "Fri12": 6,
    "Sat13": 7,
    "Sun14": 5,
    })

workers, pay = gp.multidict({
    "Amy":   10,
    "Bob":   12,
    "Cathy": 10,
    "Dan":   8,
    "Ed":    8,
    "Fred":  9,
    "Gu":    11,
    })

availability = gp.tuplelist([
    ('Amy', 'Tue2'), ('Amy', 'Wed3'), ('Amy', 'Fri5'), ('Amy', 'Sun7'),
    ('Amy', 'Tue9'), ('Amy', 'Wed10'), ('Amy', 'Thu11'), ('Amy', 'Fri12'),
    ('Amy', 'Sat13'), ('Amy', 'Sun14'), ('Bob', 'Mon1'), ('Bob', 'Tue2'),
    ('Bob', 'Fri5'), ('Bob', 'Sat6'), ('Bob', 'Mon8'), ('Bob', 'Thu11'),
    ('Bob', 'Sat13'), ('Cathy', 'Wed3'), ('Cathy', 'Thu4'), ('Cathy', 'Fri5'),
    ('Cathy', 'Sun7'), ('Cathy', 'Mon8'), ('Cathy', 'Tue9'),
    ('Cathy', 'Wed10'), ('Cathy', 'Thu11'), ('Cathy', 'Fri12'),
    ('Cathy', 'Sat13'), ('Cathy', 'Sun14'), ('Dan', 'Tue2'), ('Dan', 'Wed3'),
    ('Dan', 'Fri5'), ('Dan', 'Sat6'), ('Dan', 'Mon8'), ('Dan', 'Tue9'),
    ('Dan', 'Wed10'), ('Dan', 'Thu11'), ('Dan', 'Fri12'), ('Dan', 'Sat13'),
    ('Dan', 'Sun14'), ('Ed', 'Mon1'), ('Ed', 'Tue2'), ('Ed', 'Wed3'),
    ('Ed', 'Thu4'), ('Ed', 'Fri5'), ('Ed', 'Sun7'), ('Ed', 'Mon8'),
    ('Ed', 'Tue9'), ('Ed', 'Thu11'), ('Ed', 'Sat13'), ('Ed', 'Sun14'),
    ('Fred', 'Mon1'), ('Fred', 'Tue2'), ('Fred', 'Wed3'), ('Fred', 'Sat6'),
    ('Fred', 'Mon8'), ('Fred', 'Tue9'), ('Fred', 'Fri12'), ('Fred', 'Sat13'),
    ('Fred', 'Sun14'), ('Gu', 'Mon1'), ('Gu', 'Tue2'), ('Gu', 'Wed3'),
    ('Gu', 'Fri5'), ('Gu', 'Sat6'), ('Gu', 'Sun7'), ('Gu', 'Mon8'),
    ('Gu', 'Tue9'), ('Gu', 'Wed10'), ('Gu', 'Thu11'), ('Gu', 'Fri12'),
    ('Gu', 'Sat13'), ('Gu', 'Sun14')
    ])


shiftRequirements = {k: max(1, int(v / 2)) for k, v in
                      shiftRequirements.items()}
# OPTIGUIDE DATA CODE GOES HERE
availability = gp.tuplelist(list(set(availability)))
m = gp.Model("assignment")
model = m

x = m.addVars(availability, ub=1, name="x")

m.setObjective(gp.quicksum(pay[w]*x[w, s] for w, s in availability), GRB.MINIMIZE)

reqCts = m.addConstrs((x.sum('*', s) == shiftRequirements[s]
                      for s in shifts), "_")


m.write('workforce1.lp')

m.optimize()

# OPTIGUIDE CONSTRAINT CODE GOES HERE

m.update()
m.optimize()
