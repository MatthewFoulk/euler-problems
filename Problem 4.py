

def main():

    pal_max = 0

    for i in range(100, 1000):

        for j in range (100, 1000):

            k = i * j
            l = int(str(k)[::-1])

            if k == l:

                pal_total = i * j
                
                if pal_total > pal_max:
                    
                    pal_max = pal_total
                    print(pal_max)


if __name__ == "__main__":
    main()
    