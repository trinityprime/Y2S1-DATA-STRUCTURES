positive_integer = 0
negative_integer = 0
integers = 8
integer_list = []

for i in range(integers):
    integer_input = int(input("Please enter an integer: "))
    integer_list.append(integer_input)

for num in integer_list:
    if num > 0:
        positive_integer += 1
    elif num < 0:
        negative_integer += 1

print(f"Positive integers: {positive_integer}")
print(f"Negative integers: {negative_integer}")