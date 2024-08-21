def newton(x):
    return x**2 - 4*x + 2


def newtonPrime(x):
    return 2*x - 4

def main():
    # starting value
    x0 = 0.00
    for i in range(5):
        # Calculate the next approximation
        xnew = x0 - (newton(x0) / newtonPrime(x0))
        
        # Update the old value
        x0 = xnew

        print(f"Iteration {i+1}: x = {xnew}")

if __name__ == "__main__":
    main()