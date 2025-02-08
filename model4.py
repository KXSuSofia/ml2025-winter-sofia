
N = int(input("Enter a positive integer N: "))  
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(N)]  
X = int(input("Enter an integer X: "))  

print(numbers.index(X) + 1 if X in numbers else -1)







