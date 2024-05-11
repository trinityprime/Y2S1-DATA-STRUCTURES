def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    # Since low starts at 0, high needs to minus 1

    while low <= high:
        mid = (low + high) // 2
        # Use double slash, because need to round down divided number

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        # Since low = 0, mid need to plus 1
        else:
            high = mid - 1
        # Since low = 0, high need to minus 1

    return -1  # Target value not found

# Example usage
arr = [10,23,25,34,36,42,63,74,87,92,99]
target = 92
result = binary_search(arr, target)
print(f"Target value {target} found at index {result}")


#Note:
#For high, minus 1
#For mid, plus 1