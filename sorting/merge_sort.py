def merge_sort(input_list, iterate=0):
    if len(input_list) == 1:
        return input_list
    pivot = int((len(input_list)+1)/2)
    a = merge_sort(input_list[:pivot], iterate+1)
    b = merge_sort(input_list[pivot:], iterate+1)
    a_index = 0
    b_index = 0
    return_list = []

    while a_index < len(a) and b_index < len(b):
        if b[b_index] < a[a_index]:
            return_list.append(b[b_index])
            b_index += 1
        else:
            return_list.append(a[a_index])
            a_index += 1

    if a_index == len(a):
        for i in b[b_index:]:
            return_list.append(i)
    if b_index == len(b):
        for i in a[a_index:]:
            return_list.append(i)

    return return_list
