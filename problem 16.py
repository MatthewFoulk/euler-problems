
def main():

    total_exp = 1 # start at one because multiplying
    total_sum = 0

    # Find 2 to the 1000th
    for exponent in range(0,1000):
        total_exp *= 2

    for digit in str(total_exp):
        total_sum += int(digit)

    print(total_sum)

if __name__ == "__main__":
    main()