def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None
    return sorted(my_list)[1]
    # return 0
def find_second_smallest_v2(my_list):
    if len(my_list) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in my_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest


print(find_second_smallest([5, 8, 3, 2, 6]))
print(find_second_smallest_v2([5, 8, 3, 2, 6]))
