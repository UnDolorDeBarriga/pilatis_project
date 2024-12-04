from docplex.mp.model import Model
import numpy as np
import pandas as pd
import math as m
import matplotlib.pyplot as plt
import os


# Functions
def euclidean_distance(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points
    Args:
        x1 (int): x coordinate of the first point
        y1 (int): y coordinate of the first point
        x2 (int): x coordinate of the second point
        y2 (int): y coordinate of the second point

    Return:
        int: The Euclidean distance between the two points
    """
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


bounding_corridor_size_X = 3
bounding_corridor_size_Y = 3

script_dir = os.path.dirname(os.path.abspath(__file__))

wh_cordinates_f = pd.read_csv(os.path.join(script_dir, "..\\data\\wh_coords_OP.csv"))
orders_f = pd.read_csv(os.path.join(script_dir, "..\\data\\orders.csv"))

# Parameters
X = wh_cordinates_f["x"].values
Y = wh_cordinates_f["y"].values

orders = []
for i in range(len(orders_f)):
    k = []
    for j in orders_f.iloc[i]:
        if pd.notna(j):
            k.append(int(j))

    orders.append(k)

s = 1  # Size of a storage unit (in meters)
v = 1  # Speed of the drone
M = len(X)  # Number of storage units
N = len(orders)  # Number of orders
(x_o, y_o) = (0, 0)  # Origin coordinates
d = [0] * N  # Total distance of each order

# total size of the warehouse
x_w, y_w = (
    max(X) * s + bounding_corridor_size_X * 2,
    max(Y) * s + bounding_corridor_size_Y * 2,
)

# Model
mdl = Model(name="Euclidean basquet allocation")

basket_position = mdl.integer_var_list(2, name="basket_position")

for i, order in enumerate(orders):
    for item in order:
        d[i] += 2 * euclidean_distance(
            basket_position[0], basket_position[1], int(X[item]), int(Y[item])
        )

# Constraints
mdl.add_constraint(basket_position[0] >= 0)
mdl.add_constraint(basket_position[0] <= x_w)
mdl.add_constraint(basket_position[1] >= 0)
mdl.add_constraint(basket_position[1] <= y_w)
for i in range(M):
    mdl.add_constraint(basket_position[0] not in X and basket_position[1] not in Y)

# Objective function
mdl.minimize(mdl.sum(d[i] for i in range(N)))
