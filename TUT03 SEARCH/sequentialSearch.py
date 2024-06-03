list = [ 12, 19, 3, 13, 20, 5, 8, 16, 6, 15 ]

def sequential_search(list):
    comparison = 0

    for i in list:
        comparison += 1
        if i == 8:
            print("Found!")
            break

    print(f"Comparisons required: {comparison}")


sequential_search(list)

sorted_list = [ 3, 6, 8, 10, 11, 15, 17, 18, 19, 20 ]

def sorted_sequential_search(list):
    comparison = 0

    for i in list:
        comparison += 1
        if i == 12:
            print("Found!")
            break
    
    if i != 12:
        print("Not found!")

    
    print(f"Comparisons required: {comparison}")

sorted_sequential_search(sorted_list)

list = [10, 23, 25, 34, 36, 42, 63, 74, 87, 92, 99]

def sequential_search(list):
	comparison = 0
	for i in list:
		comparison += 1
		if i == 25:
			print(f"Number 25 found with {comparison} comparisons")
			break
	if i != 25:
		print("Number 25 not found.")


sequential_search(list)