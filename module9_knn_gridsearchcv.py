from sklearn.datasets import load_iris  
from sklearn.model_selection import train_test_split, GridSearchCV  
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.pipeline import Pipeline  
from sklearn.preprocessing import MinMaxScaler  

# Load and prepare dataset  
skx_dataset = load_iris()  
X_features = skx_dataset.data  
y_target = skx_dataset.target  

# Train-test split with reproducibility  
X_train_set, X_test_set, y_train_labels, y_test_labels = train_test_split(  
    X_features,   
    y_target,  
    test_size=0.25,  
    random_state=42,  
    stratify=y_target  
)  

# Build preprocessing pipeline  
model_pipeline = Pipeline([  
    ('feature_scaler', MinMaxScaler()),  
    ('classifier', KNeighborsClassifier())  
])  

# Optimized parameter grid
tuning_parameters = [{  
    'classifier__n_neighbors': [3, 5, 7, 9, 11],  
    'classifier__weights': ['uniform', 'distance'],  
    'classifier__leaf_size': [10, 15, 20],  
    'classifier__p': [1, 2] 
}]  

# Configure GridSearchCV with parallel processing  
grid_search = GridSearchCV(  
    estimator=model_pipeline,  
    param_grid=tuning_parameters,  
    scoring='accuracy',  
    cv=5,  
    n_jobs=-1,  
    verbose=1,  
    pre_dispatch='2*n_jobs'  
)  

# Execute grid search  
grid_search.fit(X_train_set, y_train_labels)  

# Results analysis  
best_params = grid_search.best_params_  
best_score = grid_search.best_score_  

print(f"\nOptimal Parameters: {best_params}")  
print(f"Cross-Validation Accuracy: {best_score:.4f}")  

# Final model evaluation  
train_accuracy = grid_search.score(X_train_set, y_train_labels)  
test_accuracy = grid_search.score(X_test_set, y_test_labels)  

print(f"\nTraining Accuracy: {train_accuracy:.4f}")  
print(f"Test Accuracy: {test_accuracy:.4f}")  

# Overfitting check  
if (train_accuracy - test_accuracy) > 0.15:  
    print("\nWarning: Potential overfitting detected!")  
    print("Recommended actions:")  
    print("1. Simplify parameter grid")  
    print("2. Add regularization")  
    print("3. Investigate feature selection")  



