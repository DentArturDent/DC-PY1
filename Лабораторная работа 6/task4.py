import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file_name, delimiter=',', new_line='\n') -> list[dict]:
    with open(file_name) as csv_file:
        csv_list = csv_file.read().split(new_line)

        keys = csv_list[0].split(delimiter)
        values = csv_list[1:]
        len_val = len(values)

        val_list = [column.split(delimiter) for column in values]

        json_list = []
        for row in range(len_val):
            json_list.append({col: val_list[row][num] for num, col in enumerate(keys)})
        return json_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
