
def main():
    
    prime_total = 0
    num = 0

    while num < 2000000:
        if check_prime(num):
            prime_total += num

        num += 1
    
    print(prime_total)

def check_prime(num):

    if num <= 1:
        return False
    
    elif num == 2:
        return True

    elif num % 2 == 0:
        return False

    counter = 3

    while counter * counter <=num:

        if num % counter == 0:
            return False
        else:
            counter += 2
    
    return True

if __name__ == "__main__":
    main()