def binarySearch( theValues, target ):
# Start with the entire sequence of elements
    numpass = 0
    low = 0
    high = len(theValues) - 1

    while low <= high:
        numpass += 1

        mid = (high + low) // 2
        print("Pass", numpass, "low:", low, "high:", high, "mid:", mid)

        if theValues[mid] == target:
            print("Total passes: ", numpass )
            return mid

        elif target < theValues[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return -1

theValues = [12,19,3,13,20,5,8,16,6,15]
print(binarySearch(theValues, 12))