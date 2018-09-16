def insertion_sort(input_list):
    for i in range(2, len(input_list)):
        key = input_list.pop()
        index = 0
        for j in range(i):
            if key > input_list[j]:
                index = j+1
            else:
                break
        input_list.insert(index, key)
