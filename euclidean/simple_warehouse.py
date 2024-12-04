from docplex.mp.model import Model
import numpy as np
import pandas as pd
import math as m
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

wh_cordinates_f = pd.read_csv(os.path.join(script_dir, "..\\data\\wh_coords_OP.csv"))

# # Variables
X = wh_cordinates_f["x"].values
Y = wh_cordinates_f["y"].values


# plt.scatter(X, Y)
# plt.xlabel("X Coordinates")
# plt.ylabel("Y Coordinates")
# plt.title("Warehouse Coordinates")
# plt.grid(True)
# plt.show()
