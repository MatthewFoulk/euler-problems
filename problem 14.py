

def main():

    current_number = 13
    max_chain = 0
    max_chain_number = 0

    # Run until the millionth number
    while current_number < 1000000:

        # Initialize counter for chained numbers, set chain number to be broken down
        chain_counter = 0
        chain_number = current_number
        
        # Run until the chain number is 1 (ie the final chain number)
        while chain_number > 1:

            # Increment the counter for each chain number
            chain_counter += 1
            
            # Check if number is even or odd
            if chain_number % 2 == 0:
                chain_number = even_num(chain_number)

            else:
                chain_number = odd_num(chain_number)

        # Check if number has the longest chain
        if chain_counter > max_chain:
            max_chain = chain_counter
            max_chain_number = current_number
        
        # Increase current number by 1
        current_number += 1
    
    # Print the number with the longest chain
    print(max_chain_number)
            
# Handle even numbers
def even_num(chain_number):
    return chain_number / 2

# Handle odd numbers
def odd_num(chain_number):
    return chain_number * 3 + 1


if __name__ == "__main__":
    main()