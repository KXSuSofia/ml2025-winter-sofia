import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# Validate N input
while True:
    try:
        sofia_kxs_N = int(input("Enter N (positive integer): "))
        if sofia_kxs_N > 0:
            break
        else:
            print("Error: N must be a positive integer.")
    except ValueError:
        print("Error: Invalid input. Please enter a positive integer.")

# Validate k input
while True:
    try:
        sofia_kxs_k = int(input(f"Enter k (positive integer <= {sofia_kxs_N}): "))
        if sofia_kxs_k > 0 and sofia_kxs_k <= sofia_kxs_N:
            break
        else:
            print(f"Error: k must be a positive integer <= {sofia_kxs_N}.")
    except ValueError:
        print("Error: Invalid input. Please enter a positive integer.")

# Collect data points
sofia_kxs_X_data = []
sofia_kxs_y_labels = []
for i in range(sofia_kxs_N):
    print(f"Point {i+1}:")
    sofia_kxs_x = float(input("Enter x: "))
    sofia_kxs_y = float(input("Enter y: "))
    sofia_kxs_X_data.append([sofia_kxs_x])
    sofia_kxs_y_labels.append(sofia_kxs_y)

sofia_kxs_X_train = np.array(sofia_kxs_X_data)
sofia_kxs_y_train = np.array(sofia_kxs_y_labels)

# Calculate label variance
sofia_kxs_variance = np.var(sofia_kxs_y_train)
print(f"Variance of training labels: {sofia_kxs_variance:.4f}")

# Get X for prediction
while True:
    try:
        sofia_kxs_X_input = float(input("Enter X to predict Y: "))
        break
    except ValueError:
        print("Error: Invalid input. Please enter a real number.")

# k-NN Regression
sofia_kxs_model = KNeighborsRegressor(n_neighbors=sofia_kxs_k)
sofia_kxs_model.fit(sofia_kxs_X_train, sofia_kxs_y_train)
sofia_kxs_Y_pred = sofia_kxs_model.predict([[sofia_kxs_X_input]])

print(f"Predicted Y for X = {sofia_kxs_X_input}: {sofia_kxs_Y_pred[0]:.4f}")
