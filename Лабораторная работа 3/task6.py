list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение

max_val = max(list_numbers)
max_ind = list_numbers.index(max_val)
list_numbers[max_ind], list_numbers[-1] = list_numbers[-1], list_numbers[max_ind]
print(list_numbers)
