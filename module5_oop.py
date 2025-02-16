class NumberProcessor:  
    def __init__(self):  
        self.numbers = []  
    
    def add_number(self, number: int) -> None:  
        self.numbers.append(number)  
    
    def find_index(self, x: int) -> int:  
        try:  
            return self.numbers.index(x) + 1  
        except ValueError:  
            return -1  

if __name__ == "__main__":  
    processor = NumberProcessor()  
    
    n = int(input("Enter N: "))  
    for _ in range(n):  
        num = int(input("Enter a number: "))  
        processor.add_number(num)  
    
    x = int(input("Enter X: "))  
    print(processor.find_index(x))
