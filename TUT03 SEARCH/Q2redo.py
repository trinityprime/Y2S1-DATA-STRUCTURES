list = [3, 6, 8, 10, 11, 15, 17, 18, 19, 20]

def sorted_sequential_search(number):
    comparison = 0
    for i in list:
        if i != number:
            comparison += 1
        elif i == number:
            comparison += 1
            print("Number found!")
            print(f"Comparisons: {comparison}")
            
    print(comparison)


sorted_sequential_search(12)
