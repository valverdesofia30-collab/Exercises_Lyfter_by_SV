def print_parameters_and_return(func):
    def wrapper(*args, **kwargs):
        print("Received parameters: ")
        print(f"args = {args}")
        print(f"kwargs = {kwargs}")
        
        
        result = func(*args, **kwargs)
        
        print(f"Return value = {result}")
        
        return result
    
    return wrapper

@print_parameters_and_return
def add(a, b):
    return a + b

sum_result = add (5, 3)