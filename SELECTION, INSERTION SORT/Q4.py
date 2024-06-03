theA = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]

def getSortKey(theElement):
    return theElement[-1]

print(theA)
theA = sorted(theA, key=getSortKey)
print(theA)