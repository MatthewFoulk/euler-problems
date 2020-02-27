
def main():
    
    triangle = [[75],[95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 04, 82, 47, 65], [19 01 23 75 03 34],]
    curr_total = 0
    max_total = 0
    max_num = 99

    # Change the starting point
    for start_num in range(0,len(triangle)):

        # Start num in left corner
        if start_num == 0:
            curr_total = left_path(triangle, max_num, max_total, start_num, curr_total)
        
        # Start num in right corner
        elif start_num == len(triangle) - 1:
            curr_total = right_path(triangle, max_num, max_total, start_num, curr_total)
        
        # Start num in middle
        else:
            curr_total = middle_path(triangle, max_num, max_total, start_num, curr_total)

        # Check if this is a new max total, then change accordingly
        if curr_total > max_total:
            max_total = curr_total

        # Reset current total
        curr_total = 0
    
    # Print the maximum pathway
    print(max_total)
        

def left_path(triangle, max_num, max_total, start_num, curr_total):
    for row in range(len(triangle) - 1, -1, -1):
        if (curr_total + (row + 1) * max_num) > max_total:
            curr_total += triangle[row][start_num]
        else:
            return 0
    return curr_total

def right_path(triangle, max_num, max_total, start_num, curr_total):
    num_position = 0
    for row in range(len(triangle) - 1, -1, -1):
        if (curr_total + (row + 1) * max_num) > max_total:
            curr_total += triangle[row][start_num - num_position]

        else:
            return 0
        num_position += 1
    return curr_total

def middle_path(triangle, max_num, middle_max_total, start_num, curr_total):
    
    path = 0

    while path <= start_num:
        curr_num = start_num
        # Iterate up the rows of the triangle
        for row in range(len(triangle) - 1, -1, -1):
            # Check if current path is still viable for maximum
            if (curr_total + (row + 1) * max_num) > middle_max_total:
                if curr_num != 0 and curr_num + path > len(triangle[row]) - 1:
                    curr_num -= 1
                curr_total += triangle[row][curr_num]
        
        path += 1
        
        if curr_total > middle_max_total:
            middle_max_total = curr_total

        curr_total = 0

    return middle_max_total        

if __name__ == "__main__":
    main()