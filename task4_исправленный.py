import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file_name, delimiter=',', new_line='\n') -> list[dict]:
    with open(file_name) as csv_file:
        csv_string = csv_file.read()

        csv_list = csv_string.split(new_line)
        table_list = [column.split(delimiter) for column in csv_list]

        error_indic = 0  # индикатор корректности CSV-файла

        keys = table_list[0]
        val_list = table_list[1:]
        len_val = len(val_list)

        # добавление пустых ключей в случае некорректной таблицы
        if len(keys) < max(len(val_list[i]) for i in range(len_val)):
            error_indic += 1
            emp = ['']*(max(len(val_list[i]) for i in range(len_val)) - len(keys))
            keys.extend(emp)

        json_list = []
        for row in range(len_val):
            new_dict = {}
            for num, col in enumerate(keys):
                try:
                    new_dict[col] = val_list[row][num]
                except IndexError:
                    error_indic += 1
                    new_dict[col] = ''  # добавление пустых полей в случае некорректной таблицы
            json_list.append(new_dict)

        if error_indic > 0:
            print('Формат CSV-файла некорректен, отсутствующие элементы заменены пустыми строками')

        return json_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
