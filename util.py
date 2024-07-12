
def sort_them_into_list(data, columns) -> list:
    column_list = [column_dict['name'] for column_dict in columns]
    output = []
    for item in data:
        thingy_dict = {}
        for index, column in enumerate(column_list):
            thingy_dict[column] = item[index]
        output.append(thingy_dict)
    return output

def sort_it_into_dict(data, columns) -> dict:
    column_list = [column_dict['name'] for column_dict in columns]
    new_dict = {}
    for index, column in enumerate(column_list):
        new_dict[column] = data[index]
    return new_dict