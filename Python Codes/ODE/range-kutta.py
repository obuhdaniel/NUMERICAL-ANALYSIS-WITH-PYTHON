# Define the differential equation dy/dx = x + y
def myFunction(x, y):
    return x + y

# Euler's method implementation
def runge_method():
    

    x = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]     # Initial x value
    y = [0] * len(x)       # Initial y value
    y[0] = 1   # End x value
    h = 0.1      # Step size
    
    
    for i in range(1, len(x)):
        k1 = h * myFunction(x[i-1], y[i-1])
        k2 = h * myFunction((x[i-1] + 0.5 * h), (y[i-1] + 0.5 *k1))
        k3 = h * myFunction((x[i-1] + 0.5 * h), (y[i-1] + 0.5 *k2))
        k4 = h * myFunction((x[i-1] + h), (y[i-1] + k3))
        
        y[i] = y[i-1] + (1/6) * (k1 + 2* k2 + 2 * k3 + k4 )
        
        y_value = y[i]
        print(f"{y_value:0.4f}".format())
        
    
        
    
       
       
        
        
runge_method()





