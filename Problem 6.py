
def main():

    # Declare variables
    sum_of_squares = 0
    square_of_sums = 0

    # Loop through first 100 numbers
    for i in range(1,101):
        sum_of_squares += (i * i)
        square_of_sums += i
    
    difference = (square_of_sums * square_of_sums) - sum_of_squares
    print(difference)



if __name__ == "__main__":
    main()