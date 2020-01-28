

def main():

    # Initialize variables with first pythagorean triple
    a = 3
    b = 4
    c = 5

    if square(a) + square(b) == square(c):
        if a + b == c:
            print("A = " + str(a) + "\nB = " + str(b) + "\nC = " + str(c))

def square(num):
    return num * num



if __name__ == "__main__":
    main()