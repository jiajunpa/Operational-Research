from gurobipy import *
# Code for problem 1 of HW5
model_q1 = Model('Bowls&muds')

x1 = model_q1.addVar(vtype = GRB.CONTINUOUS, name = 'Bowl' )
x2 = model_q1.addVar(vtype = GRB.CONTINUOUS, name = 'Mug')

model_q1.update()

model_q1.setObjective(40*x1 + 50*x2, GRB.MAXIMIZE)

model_q1.addConstr(x1 + 2*x2 <= 40, "c0")
model_q1.addConstr(4*x1 + 3*x2 <= 120, "c1")

model_q1.optimize()

for v in model_q1.getVars():
    print('%s %g' % (v.varName, v.x))

print('Obj: %g' % model_q1.objVal)


#Code for problem 2 of HW5
#create an empty dictionary for variables
x = {}
# name the model
model_q2 = Model('Computer allocation')
# Specify the number of plants and markets
n_p = 3
n_m = 4

# add variables

for i in range(n_p):
    for j in range(n_m):
        x[i,j] = model_q2.addVar(vtype = GRB.INTEGER, name = 'x_{},{}'.format(i,j))

model_q2.update()

# set objective function
model_q2.setObjective(quicksum(x[i,j] for i in range(n_p) for j in range(n_m)), GRB.MAXIMIZE)

# add constraints
# 1. capacities of manufacturing plants
Capacities = [3000, 6000, 9000]

for i in range(n_c):
    model_q2.addConstr(quicksum(x[i,j] for j in range(n_m)) <= Capacities[i])

# 2. Quota Limitation
model_q2.addConstr(quicksum(x[i,2] for i in range(n_p)) <= 2000)
model_q2.addConstr(quicksum(x[i,3] for i in range(n_p)) <= 2000)

# 3. Transportation capacity Limitation
trans_capacity = [800, 1600, 1000, 900, 900, 1200, 1300, 700, 1400, 1300, 1600, 500]

for i in range(n_p):
    for j in range(n_m):
        k = 4*i + j
        print(k)
        model_q2.addConstr(x[i,j] <= trans_capacity[k])

# 4. Fleet size restriction
model_q2.addConstr(x[0,1] + x[0,2] <= 2000)
model_q2.addConstr(x[2,0] + x[2,1] + x[2,2] <= 3000)

model_q2.optimize()

# print result
for v in model_q2.getVars():
    print('%s %g' % (v.varName, v.x))

print('Obj: %g' % model_q2.objVal)
