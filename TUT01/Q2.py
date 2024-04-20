def sum_of_squares(n):
    result = 0
    for i in range(1, n+1):
        print(i)
        if i <= n:
            result += i * i

    return result


print(sum_of_squares(5))
