def sort_array(source_array):
    sorted_odd = []
    index_even = []
    for index, num in enumerate(source_array):
        if num % 2 == 0:
            index_even.append(index)
        else:
            sorted_odd.append(num)
    sorted_odd.sort()
    count = -1
    for index, num in enumerate(source_array):
        if index not in index_even:
            count += 1
            source_array[index] = sorted_odd[count]
    return source_array


print(sort_array([5, 3, 2, 8, 1, 4]))

