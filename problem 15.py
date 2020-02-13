

def main():
    matrix = []

    for row in range(0,21):
        layer = []
        for col in range(0,21):
            if col == 0 or row == 0:
                layer.append(1)
            else:
                layer.append(matrix[row - 1][col] + layer[col - 1])
            print(layer[col])
        print("\n")
        matrix.append(layer)
    


if __name__ == "__main__":
    main()