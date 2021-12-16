#!/usr/bin/env python3.7

# Copyright 2021, Gurobi Optimization, LLC

# This example formulates and solves the following simple LP model
# using the matrix API:
#  minimize
#        c y -20
#  subject to
#        x + 2 y + 3 z <= 4
#        x +   y       >= 1
#        x, y, z
#  A = (5,3,2;4,2,1) b = (20;15)  d = (3;2;1) c= (4,3,2)

import gurobipy as gp
from gurobipy import GRB
import numpy as np
import scipy.sparse as sp

# dir(gp.Model.addMVar)
# help(gp.Model.addMVar)

try:

    # Create a new model
    m = gp.Model("lp2")

    # Create variables
    x = m.addMVar(shape=5, vtype=GRB.CONTINUOUS, name="x")

    # Set objective
    obj = np.array([-3.0, -2.0, 0, 0, 0])  # c
    m.setObjective(obj @ x+20, GRB.MINIMIZE)

    # Build (sparse) constraint matrix

    val = np.array([5.0, 3.0, 2.0, 4.0, 2.0, 1.0, 1,1,1])
    row = np.array([0, 1, 2, 0, 1, 2, 0, 1, 2])
    col = np.array([0, 0, 0, 1, 1, 1, 2, 3, 4])
    # A.toarray()
    A = sp.csr_matrix((val, (row, col)), shape=(3, 5))

    # help(sp.csr_matrix)

    # Build rhs vector
    rhs = np.array([4,3,2])

    # Add constraints
    m.addConstr(A @ x == rhs, name="c")
    m.write('3.lp')
    # Optimize model
    m.optimize()

    print(x.X)
    print('Obj: %g' % m.objVal)

except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')
