from module5_mod import Sofia  

if __name__ == "__main__":  
    processor = Sofia()  
    
    n = int(input("Enter N: "))  
    for _ in range(n):  
        num = int(input("Enter a number: "))  
        processor.add_number(num)  
    
    x = int(input("Enter X: "))  
    print(processor.find_index(x))
