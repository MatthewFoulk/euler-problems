
def main():

    num = 0
    x = 0

    while x != 10001:
        num += 1

        if check_prime(num):
            x += 1

    print(num)

def check_prime(num):

    if num <= 1:
        return False

    elif num == 2:
        return True

    elif num % 2 == 0:
        return False
    
    counter = 3 

    while counter * counter <= num:
        
        if num % counter == 0:
            return False
        else:
            counter += 2

    return True
            


if __name__ == "__main__":
    main()