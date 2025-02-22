import numpy as np  

class SofiakxsuRegressor:  
    def __init__(self):  
        self.sofiakxsu_data = np.empty((0, 2))  
    
    def sofiakxsu_add(self, x_input, y_output):  
        self.sofiakxsu_data = np.vstack([self.sofiakxsu_data, [x_input, y_output]])  
    
    def sofiakxsu_predict(self, target_x, k_param):  
        sofiakxsu_distances = np.abs(self.sofiakxsu_data[:, 0] - target_x)  
        nearest_sofiakxsu = np.argsort(sofiakxsu_distances)[:k_param]  
        return np.mean(self.sofiakxsu_data[nearest_sofiakxsu, 1])  

def sofiakxsu_get_int(prompt_msg):  
    while True:  
        try:  
            user_value = int(input(prompt_msg))  
            if user_value > 0:  
                return user_value  
            print("Positive integers only please")  
        except ValueError:  
            print("Invalid number format")  

def sofiakxsu_get_float(prompt_msg):  
    while True:  
        try:  
            return float(input(prompt_msg))  
        except ValueError:  
            print("Number required")  

if __name__ == "__main__":  
    sofiakxsu_model = SofiakxsuRegressor()  
    
    data_points = sofiakxsu_get_int("Total points to collect: ")  
    k_selection = sofiakxsu_get_int("Neighbor count (k): ")  
    
    if k_selection > data_points:  
        print(f"Error: {k_selection} exceeds maximum {data_points}")  
        exit()  
    
    print(f"\nProvide {data_points} coordinates:")  
    for idx in range(data_points):  
        x_val = sofiakxsu_get_float(f"X{idx+1}: ")  
        y_val = sofiakxsu_get_float(f"Y{idx+1}: ")  
        sofiakxsu_model.sofiakxsu_add(x_val, y_val)  
    
    prediction_x = sofiakxsu_get_float("\nTarget X value: ")  
    result = sofiakxsu_model.sofiakxsu_predict(prediction_x, k_selection)  
    print(f"\nCalculated Y: {result:.4f}")  
