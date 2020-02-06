
def main():
    current_num = 1
    triangle_num = 0
    factors = 0

    # Run until a number that has 500 factors
    while True:    

        # Convert number to triangle number
        for num in range(1, current_num + 1):
            triangle_num += num
        
        print(triangle_num)

        i = 1

        # Check if each number is a factor of the triangle number
        # Only go to half because factors would repeat from opposite side
        while i * i < triangle_num:
            
            if triangle_num % i == 0:
                factors += 2

            i +=1
        
        print(factors)

        # Break once factors is over 500
        if factors > 500:
            print(triangle_num)
            break

        # Reset factor count and triangle number
        factors = 0
        triangle_num = 0

        # Increase current number
        current_num += 1


if __name__ == "__main__":
    main()