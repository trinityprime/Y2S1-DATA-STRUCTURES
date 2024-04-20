array = [6, 2, 9, 12, 25, -8]


def minmax(data):
    min = max = data[0]
    for i in data:
        print(i)
        if i <= min:
            min = i
        if i >= max:
            max = i
    return (min, max)


result = minmax(array)
print(result)
