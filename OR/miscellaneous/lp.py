#!/usr/bin/env python3.7

# Copyright 2021, Gurobi Optimization, LLC

# This example formulates and solves the following simple LP model
# using the matrix API:
#  maximize
#        x +   y + 2 z
#  subject to
#        x + 2 y + 3 z <= 4
#        x +   y       >= 1
#        x, y, z binary
#  A = (5,3,2;4,2,1) b = (20;15)  d = (3;2;1) c= (4,3,2)

import gurobipy as gp
from gurobipy import GRB
import numpy as np
import scipy.sparse as sp

# dir(gp.Model.addMVar)
# help(gp.Model.addMVar)

try:

    # Create a new model
    m = gp.Model("lp1")

    # Create variables
    x = m.addMVar(shape=3, vtype=GRB.CONTINUOUS, name="y")

    # Set objective
    obj = np.array([4.0, 3.0, 2.0])  # c
    m.setObjective(obj @ x-20, GRB.MINIMIZE)

    # Build (sparse) constraint matrix

    val = np.array([5.0, 3.0, 2.0, 4.0, 2.0, 1.0])
    row = np.array([0, 0, 0, 1, 1, 1])
    col = np.array([0, 1, 2, 0, 1, 2])

    A = sp.csr_matrix((val, (row, col)), shape=(2, 3))

    d = np.array([3.0, 2.0, 1.0])  # c
# A[0,1]
    b = np.array([20,15])  #

    # Build rhs vector
    rhs = A @ d - b
# Ad -b

    # Add constraints
    m.addConstr(A @ x >= rhs, name="c")

    # Optimize model
    m.optimize()

    print(x.X)
    print('Obj: %g' % m.objVal)

except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')
