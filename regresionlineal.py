import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# get the json filename from the command line
import sys
filename = sys.argv[1]
print("Filename:", filename)

# read the json file
import json
with open(filename) as file:
    data = json.load(file)

fingers = ["thumb", "index_far", "index", "middle", "ring", "pinky"]
lists_dict={}
for finger in fingers:
    lists_dict[finger] = [],[]
    for point in data[finger]:
        for n, element in enumerate(point.values()):
            if n%2 == 0:
               lists_dict[finger][0].append(element)
            else:
                lists_dict[finger][1].append(element)
            


print(lists_dict)


for finger in fingers:
    x = np.array(lists_dict[finger][0])
    y = np.array(lists_dict[finger][1])
    
    if x.size == 0 or y.size == 0:
        continue
    X = x.reshape(-1, 1)
    model = LinearRegression()
    model.fit(X, y)

    x_line = np.linspace(min(x), max(x), 100)
    X_line = x_line.reshape(-1, 1)
    y_line = model.predict(X_line)

    pendiente_en_el_lado_derecho = model.coef_[0]

    arcotangente = np.arctan(pendiente_en_el_lado_derecho)

    print("Pendiente:", pendiente_en_el_lado_derecho)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression with Square Array')
    plt.show()

