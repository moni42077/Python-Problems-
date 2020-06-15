# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.

# Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

# Example

# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

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

