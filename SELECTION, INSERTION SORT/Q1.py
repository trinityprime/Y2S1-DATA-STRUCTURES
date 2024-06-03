# Sort a sequence in ascending order using the selection sort
# algorithm
def selectionSort( theSeq, theOrder ):
    if theOrder == "A":
        print("Sort Ascending")
    elif theOrder == "D":
        print("Sort Descending")
    else:
        print("Parameter error.")
        return
    
    n = len( theSeq )
    for i in range(n - 1):
        # Assume the ith element is the smallest.
        currentIndex = i
        # Determine if any other element contains a smaller value.
        for j in range(i+1, n):

            if theOrder == "A":
                if theSeq[j] < theSeq[currentIndex]:
                    currentIndex = j

            if theOrder == "D":
                if theSeq[j] > theSeq[currentIndex]:
                    currentIndex = j

            # Swap the ith value and currentIndex value only if the
            # smallest value is not already in its proper position.
        if currentIndex != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[currentIndex]
            theSeq[currentIndex] = tmp
        print(f"Pass {str(i+1)}: {list_of_numbers} ")
# Test codes
list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
print('Input List:', list_of_numbers)
selectionSort(list_of_numbers, "A")
print('Sorted List:', list_of_numbers)