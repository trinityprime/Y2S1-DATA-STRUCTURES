def sequentialSearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        if theValues[i] == target:
            return "Found"
    return "Not Found"

def sortedSequentialSearch(theValues, target):
    theValues.sort()
    n = len(theValues)
    for i in range(n):
        print(theValues[i])
        if theValues[i] == target:
            return "Found"
        elif theValues[i] > target:
            return "Not Found"
    return "Not Found"

theValues = [12,19,3,13,20,5,8,16,6,15]
target = 20

print(sequentialSearch(theValues, target)) 
print(sortedSequentialSearch(theValues, target))
