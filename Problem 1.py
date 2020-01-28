

def main():

    # Store the total sum of multiples of 3 and 5
    sum_multiples = 0

    # Loop through every number less than 1000
    for num in range(1,1000):
        
        # Check if number is divisible by 3 or 5, i.e. a multiple
        if num % 3 == 0 or num % 5 == 0:
            sum_multiples += num

    print(sum_multiples)

if __name__ == '__main__':
    main()