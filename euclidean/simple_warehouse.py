from docplex.mp.model import Model
import numpy as np
import pandas as pd
import math as m
import matplotlib.pyplot as plt
import os


def euclidean_distance(x1, y1, x2, y2):
    return m.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


script_dir = os.path.dirname(os.path.abspath(__file__))

wh_cordinates_f = pd.read_csv(os.path.join(script_dir, "..\\data\\wh_coords_OP.csv"))
orders_f = pd.read_csv(os.path.join(script_dir, "..\\data\\orders.csv"))
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes

# # Variables
X = wh_cordinates_f["x"].values
Y = wh_cordinates_f["y"].values

orders = []
for i in range(len(orders_f)):
    k = []
    for j in orders_f.iloc[i]:
        if pd.notna(j):
            k.append(int(j))

    orders.append(k)

# Parameters
v = 1                       # Speed of the drone
M = len(X)                  # Number of storage units
N = len(orders)             # Number of orders
(x_o, y_o) = (0, 0)         # Origin coordinates


# Model
mdl = Model(name = "Euclidean basquet allocation")


basket_position = mdl.integer_var_list(2, name="basket_position")

# # Plotting
# plt.scatter(X, Y)
# plt.xlabel("X Coordinates")
# plt.ylabel("Y Coordinates")
# plt.title("Warehouse Coordinates")
# plt.grid(True)
# plt.show()


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
    return m.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)