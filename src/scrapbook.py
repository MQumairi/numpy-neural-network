import random
from statistics import mean
import numpy as np

# print(type("string") == str)

# input = ["0", "5", "6"]
# print(input)

# for i in range(len(input)):
#     input[i] = int(input[i])

# print(input)


# {'0,0': {'prev': None, 'cost': 0},
#  '0,1': {'prev': '0,0', 'cost': 5},
#  '0,2': {'prev': '0,1', 'cost': 10},
#  '1,0': {'prev': '0,0', 'cost': 9},
#  '1,1': {'prev': '0,1', 'cost': 10},
#  '1,2': {'prev': '0,2', 'cost': 17},
#  '2,0': {'prev': '1,0', 'cost': 18},
#  '2,1': {'prev': '1,1', 'cost': 12},
#  '2,2': {'prev': '2,1', 'cost': 14}}


# move_y = random.choice([1, 2, 3, 4])
# print(f"Random choice: {move_y}")

# print(int(1.5))

# print(sum([1, 2, 3]))

a_1 = np.array([1, 2, 3])
a_2 = np.array([1, 2, 3])
print(a_1 * a_2)
