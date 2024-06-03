my_list = [1, 2, 3]


def num_checker(lst):
    for i in lst:
        if i == lst[0]:
            print("All are the same!")
        else:
            print("Not all are same!")


num_checker(my_list)
