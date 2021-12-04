#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(array):
    zero_list = list()
    num_list = list()
    for i in array:
        if i == 0:
            zero_list.append(i)
        if i != 0:
            num_list.append(i)
    return num_list + zero_list