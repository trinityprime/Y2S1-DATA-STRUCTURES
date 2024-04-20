list = []

while True:
    sentence = input("Enter line: ")
    if sentence != ".":
        list.append(sentence)
    else: 
        break

list_len = len(list)
for i in range(list_len-1, -1, -1):
    print(list[i])