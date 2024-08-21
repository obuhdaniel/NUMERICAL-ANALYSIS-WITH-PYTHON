def myFunction(x):
    return 2.718 ** x


def main():
    a=0
    b=2

    i = ((b-a)/2) * (myFunction(a) + myFunction(b))

    print(i)

if __name__ == "__main__":
    main()