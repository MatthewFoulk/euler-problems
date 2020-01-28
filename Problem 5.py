

def main():

    num = 2520
    con = 0

    while True:

        for i in range(2,21):
            if not num % i == 0:
                num += 1
                con = 0
                break
            else:
                con += 1

        if con == 19:
            break
    
    print("Finished:" + str(num))
            



if __name__ == "__main__":
    main()