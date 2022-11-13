from random import shuffle


# добавил параметры в качестве аргументов
def get_unique_list_numbers(start: int, stop: int, list_len: int) -> list[int]:
    range_list = list(range(start, stop+1))
    shuffle(range_list)
    rand_list = range_list[:list_len]

    return rand_list


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
