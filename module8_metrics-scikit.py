import numpy as np  
from sklearn.metrics import precision_score, recall_score  

def sofiakxs_get_binary_input(prompt):  
    while True:  
        try:  
            value = int(input(prompt))  
            if value in {0, 1}:  
                return value  
            print("Error: Value must be 0 or 1")  
        except ValueError:  
            print("Error: Please enter an integer")  

def main():  
    # Get valid N input  
    while True:  
        try:  
            n_sofiak = int(input("Enter number of points (N): "))  
            if n_sofiak > 0:  
                break  
            print("Error: N must be positive")  
        except ValueError:  
            print("Error: Please enter an integer")  
    
    # Collect points using numpy  
    data_sofiak = np.empty((n_sofiak, 2), dtype=int)  
    for i in range(n_sofiak):  
        x = sofiakxs_get_binary_input(f"Point {i+1} - Enter true class (0/1): ")  
        y = sofiakxs_get_binary_input(f"Point {i+1} - Enter predicted class (0/1): ")  
        data_sofiak[i] = [x, y]  
    
    # Calculate metrics with scikit-learn  
    true_sofiak = data_sofiak[:, 0]  
    pred_sofiak = data_sofiak[:, 1]  
    
    precision = precision_score(true_sofiak, pred_sofiak, zero_division=0)  
    recall = recall_score(true_sofiak, pred_sofiak, zero_division=0)  
    
    # Format output  
    print(f"\nPrecision: {precision:.2f}")  
    print(f"Recall: {recall:.2f}")  

if __name__ == "__main__":  
    main()  
