import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# get the json filename from the command line
import sys
filename = sys.argv[1]

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

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression with Square Array')

for finger in fingers:
    # Extract x and y coordinates from the dictionary using the current finger as the key
    x = np.array(lists_dict[finger][0])
    y = np.array(lists_dict[finger][1])

    # If either the x or y list is empty, skip to the next finger
    if x.size == 0 or y.size == 0:
        continue

    # Reshape the x-coordinates into a 2D array and create a LinearRegression model
    X = x.reshape(-1, 1)
    model = LinearRegression()
    model.fit(X, y)

    # Create a line of x-coordinates and generate corresponding y-coordinates using the linear regression model
    x_line = np.linspace(min(x), max(x), 100)
    X_line = x_line.reshape(-1, 1)
    y_line = model.predict(X_line)

    # Calculate the slope of the line on the right side of the plot using the coef_ attribute of the model
    pendiente_en_el_lado_derecho = model.coef_[0]

    # Calculate the angle of the slope in radians using the arctan function from NumPy
    arcotangente = np.arctan(pendiente_en_el_lado_derecho)

    # Print the slope and plot the data points and regression line using Matplotlib
    print(finger)
    print("\tPendiente:", pendiente_en_el_lado_derecho)
    # give me the angle in degrees minutes and seconds
    angulo_grados = np.degrees(arcotangente)
    angulo_minutos = (angulo_grados % 1) * 60
    angulo_segundos = (angulo_minutos % 1) * 60
    print("\tAngulo:", angulo_grados, angulo_minutos, angulo_segundos)
    print()
    # plt.figure()
    # plt.plot(x, y, 'o')
    # plt.plot(x_line, y_line)
    # plt.show()

