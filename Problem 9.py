

def main():

    # Initialize variables with first pythagorean triple
    a = 3
    b = 4
    c = 5

    while True:
        while (c-b) > 0:
            
            # Check if the numbers add to 1000
            if a + b + c == 1000:
                print(str(a) + " " + str(b) + " " + str(c))
                sq_ab = square(a) + square(b)
                sq_c = square(c)

                # Check if numbers are a pythagorean triple
                if sq_ab == sq_c:
                    print("A = " + str(a) + "\nB = " + str(b) + "\nC = " + str(c))
                    break
                
            # Increase a, so long as it won't equal b with increase
            if (b - a) > 1:
                a += 1
            
            # Increase b and reset a
            else:
                b += 1
                a = 3

        # Increase c and reset b
        else:
            c += 1
            b = 4
            
            
        


def square(num):
    return num * num



if __name__ == "__main__":
    main()