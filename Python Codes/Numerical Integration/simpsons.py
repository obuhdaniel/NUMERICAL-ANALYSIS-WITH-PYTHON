def myFunction(x):
    return 2.718 ** x


def main():
    a=0
    b=2

    i = ((b-a)/6) * ((myFunction(a)) + 4*(myFunction((a+b)/2)) + myFunction(b))

    print(i)

if __name__ == "__main__":
    main()