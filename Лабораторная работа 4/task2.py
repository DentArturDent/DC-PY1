def get_count_char(str_):
    letters = {}

    str_low = str_.lower()

    for let in str_low:
        if let.isalpha():
            letters[let] = letters.setdefault(let, 0) + 1
    return letters


def perc_in_dict(dict_):  # функция для процентов
    dict_all = sum(dict_.values())
    let_perc = {let: (dict_[let]/dict_all)*100 for let in dict_.keys()}

    return let_perc


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

