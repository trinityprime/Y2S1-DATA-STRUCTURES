list = [12, 19, 3, 13, 20, 5, 8, 16, 6, 15]

def sequential_search(number):
    comparison = 0
    for i in list:
        if i != number:
            comparison += 1
        elif i == number:
            comparison += 1
            print("Number found!")
            print(f"Comparisons: {comparison}")


sequential_search(12)