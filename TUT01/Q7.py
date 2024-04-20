list = [1, 2, 3]


def num_checker(list):
    for i in list:
        if i[0] == i[1] == i[2]:
            print("All are the same!")
        else:
            print("Not all are same!")


num_checker(list)
