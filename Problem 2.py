
def main():

    # Declare varaibles for original starting numbers
    num1 = 0
    num2 = 1
    temp = 0
    total = 0

    # Run until number exceeds 4 mil
    while True:

        if num2 <= 4000000:

            # Check if number is even, if so add to total
            if num2 % 2 == 0:
                total += num2
            
            # Change numbers 
            temp = num2
            num2 = num1 + num2
            num1 = temp

        # Break loop if number exceeds 4 mil
        else:
            break

    print(total)


if __name__ == "__main__":
    main()