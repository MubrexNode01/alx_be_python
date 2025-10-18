def operation (a, b, operations):

   # Perform a basic arithmetic operation on two numbers.

    if operations == 'add':
        return a + b
    elif operations == 'subtract':
        return a - b
    elif operations == 'multiply':
        return a * b
    elif operations == 'divide':
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError(f"Unsupported operation: {operation} ")   
    
    
def perform_operation(num1, num2, operations):
    return operation(num1, num2, operations)  
 
