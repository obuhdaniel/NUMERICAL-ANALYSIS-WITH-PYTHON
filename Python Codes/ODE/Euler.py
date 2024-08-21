# Define the differential equation dy/dx = x + y
def myFunction(x, y):
    return x + y

# Euler's method implementation
def euler_method():
    

    x = 0       # Initial x value
    y = 1       # Initial y value
    x_end = 0.5   # End x value
    h = 0.1      # Step size
    
    # Lists to store x and y values
    x_values = []
    y_values = []
    
    # Perform Euler's method iterations
    while x <= x_end:
        # Append current values to lists
        x_values.append(x)
        y_values.append(y)
        
        # Update y using Euler's method formula

        # the += sign handles that y + in y = y + h(y')
        y += h * myFunction(x, y)
        
        # Increment x by step size
        x += h
    
  
    # Print the table with x and y values
    for i in range(len(x_values)):
        x = x_values[i]
        y = y_values[i]
        print(f"{x:0.02f}\t\t\t\t{y:0.4f}".format())
        
        
euler_method()





