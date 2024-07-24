def mergeSort( theList ):
    if len(theList) <= 1:
        return theList
    else:
        mid = len(theList) // 2
        leftHalf = mergeSort( theList[ :mid ] )
        rightHalf = mergeSort( theList[ mid: ] )

        newList = mergeSortedLists( leftHalf, rightHalf)
        return newList
    
def mergeSortedLists( listA, listB ):
    newList = []
    a = 0
    b = 0

    # Merge the two lists together until one is empty
    while a < len( listA ) and b < len( listB ):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b += 1
   
    # If listA contains more items, append remaining items to
    # newList
    while a < len(listA):
        newList.append(listA[a])
        a += 1
    
    # If listB contains more items, append remaining items to
    # newList
    while b < len(listB):
        newList.append(listB[b])
        b += 1

    return newList


# Test code
list_of_numbers = [12, 7, 9, 24, 7, 29, 5, 3, 11, 7]
print('Input List:', list_of_numbers)
merge_list = mergeSort(list_of_numbers)
print('Sorted List:', merge_list)