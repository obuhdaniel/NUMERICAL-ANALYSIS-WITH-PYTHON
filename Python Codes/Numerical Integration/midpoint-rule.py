def myFunction(x):

    #here you can return how your function is. this example uses exponential
    # e^x = 2.718^x
  

    return 2.718 ** x


def main():
    a=0
    b=2

    i = (b-a) * (myFunction((a + b)/2))

    print(i)

if __name__ == "__main__":
    main()