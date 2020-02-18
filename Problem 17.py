
def main():

    total = 0

    # Iterate through all the numbers
    for num in range(1,1001):

        # Convert number into words based on length
        if len(str(num)) == 1:
            total += get_ones(int(str(num)[0]))
            
        if len(str(num)) == 2:
            total += get_ones(int(str(num)[1])) + get_tens(int(str(num)[0]),int(str(num)[1]))

        if len(str(num)) == 3:
            total += get_ones(int(str(num)[2])) + get_tens(int(str(num)[1]), int(str(num)[2])) + get_hundreds(int(str(num)[0]), int(str(num)[1]), int(str(num)[2]))

        if len(str(num)) == 4:
            total += get_ones(int(str(num)[3])) + get_tens(int(str(num)[2]), int(str(num)[3])) + get_hundreds(int(str(num)[1]), int(str(num)[2]), int(str(num)[3])) + get_thousands(int(str(num)[0]))
    
    print(total)

# Return the number of letters in each numbers single digit equivalent, e.g. 1 == "one" == 3 digits
def get_ones(ones_digit):
    
    if ones_digit == 0:
        return 0 # Zero is never said unless its zero, which doesn't apply to this problem
    if ones_digit == 1:
        return 3
    if ones_digit == 2:
        return 3
    if ones_digit == 3:
        return 5
    if ones_digit == 4:
        return 4
    if ones_digit == 5:
        return 4
    if ones_digit == 6:
        return 3
    if ones_digit == 7:
        return 5
    if ones_digit == 8:
        return 5
    if ones_digit == 9:
        return 4

# Get the second digit character count, e.g. 2 == twenty == 6
def get_tens(tens_digit, ones_digit):

    if tens_digit == 0:
        return 0 # Zero is not said
    if tens_digit == 1:
        return get_teen(ones_digit) - get_ones(ones_digit)
    if tens_digit == 2:
        return 6
    if tens_digit == 3:
        return 6
    if tens_digit == 4:
        return 5
    if tens_digit == 5:
        return 5
    if tens_digit == 6:
        return 5
    if tens_digit == 7:
        return 7
    if tens_digit == 8:
        return 6
    if tens_digit == 9:
        return 6

def get_teen(ones_digit):

    if ones_digit == 0:
        return 3 
    if ones_digit == 1:
        return 6 
    if ones_digit == 2:
        return 6
    if ones_digit == 3:
        return 8
    if ones_digit == 4:
        return 8
    if ones_digit == 5:
        return 7
    if ones_digit == 6:
        return 7
    if ones_digit == 7:
        return 9
    if ones_digit == 8:
        return 8
    if ones_digit == 9:
        return 8

# Get the third digit character count by adding ten or to the single digit count because
# 'hundred' == 7 characters and 'and' == 3 characters, so either 7 or 3+7=10
def get_hundreds(hundreds_digit, tens_digit, ones_digit):
    if hundreds_digit == 0:
        return 0
    if ones_digit + tens_digit == 0:
        return get_ones(hundreds_digit) + 7
    else:
        return get_ones(hundreds_digit) + 10


# Return the single digit equivalent for the thousands place and add 8 for "thousand"
def get_thousands(thousands_digit):
    return get_ones(thousands_digit) + 8



if __name__ == "__main__":
    main()