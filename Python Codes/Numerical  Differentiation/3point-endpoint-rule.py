def myFunction(x):

    #here you can return how your function is. this example uses exponential
    # e^x = 2.718^x
  

    return x **2


def main():
    x = 2
    h = 1

    i = (1/(2 * h)) * ((-3 * myFunction(x)) + (4 * myFunction(x + h)) - (myFunction( x+ (2 *h))))

    print(i)

if __name__ == "__main__":
    main()