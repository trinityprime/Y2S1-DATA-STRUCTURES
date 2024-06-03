list = [10, 23, 25, 34, 36, 42, 63, 74, 87, 92, 99]

def binary_search(target):
    low = 0
    high = len(list) - 1
    #Since list has 11 values, high needs to minus 1

    while low <= high:
        mid = (low + high) // 2
        
        if target == list[mid]:
            return mid
        
        elif target > list[mid]:
            low = mid + 1
        #If target is greater than mid, lowest = mid

        elif target < list[mid]:
            high = mid - 1
        #If target is lesser than mid, highest = mid

    return -1

value = 10
if binary_search(value) == -1:
    print("Target value not found")
else:
    print(f"Target value {value} found at index {binary_search(value)}")