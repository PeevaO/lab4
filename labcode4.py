SET_POINTS = 10
BACKPACK_SIZE = 9
def get_area_and_value(stuff_dictionary):
    area = [stuff_dictionary[item][0] for item in stuff_dictionary]
    value = [stuff_dictionary[item][1] for item in stuff_dictionary]
    return area, value
def get_memtable(stuff_dictionary):
    area, value = get_area_and_value(stuff_dictionary)
    total_number = len(value)
    matrix = [[0 for variable_area in range(BACKPACK_SIZE + 1)] for i in range(total_number + 1)]

    for i in range(total_number + 1):
        for variable_area in range(BACKPACK_SIZE + 1):
            if i == 0 or variable_area == 0:
                matrix[i][variable_area] = 0

            elif area[i - 1] <= variable_area:
                matrix[i][variable_area] = max(value[i - 1] + matrix[i - 1][variable_area - area[i - 1]], matrix[i - 1][variable_area])

            else:
                matrix[i][variable_area] = matrix[i - 1][variable_area]
    return matrix, area, value

def get_selected_items_list(stuff_dictionary):
    matrix, area, value = get_memtable(stuff_dictionary)
    total_number = len(value)
    res = matrix[total_number][BACKPACK_SIZE]
    variable_area = BACKPACK_SIZE
    items_list = []

    for i in range(total_number, 0, -1):
        if res <= 0:
            break
        if res == matrix[i - 1][variable_area]:
            continue
        else:
            items_list.append((area[i - 1], value[i - 1]))
            res -= value[i - 1]
            variable_area -= area[i - 1]

    selected_stuff = []

    for search in items_list:
        for key,  area in stuff_dictionary.items():
            if area == search:
                if not(key in selected_stuff):
                    for i in range(0, area[0]):
                        selected_stuff.append(key)
    return selected_stuff


stuff_dictionary = {'в': (3, 25),
             'п': (2, 15),
             'б': (2, 15),
             'а': (2, 20),
             'и': (1, 5),
             'н': (1, 15),
             'т': (3, 20),
             'о': (1, 25),
             'ф': (1, 15),
             'д': (1, 10),
             'к': (2, 20),
             'р': (2, 20)
            }

stuff = get_selected_items_list(stuff_dictionary)

total_value = 0
for item in stuff:
    total_value += stuff_dictionary[item][1]//stuff_dictionary[item][0]


entire_value = sum([stuff_dictionary[item][1] for item in stuff_dictionary])

for i in range(0, 3):
    if i % 2 == 0:
        print(f'[{stuff[i*3]}], [{stuff[i*3 + 1]}], [{stuff[i*3 + 2]}]')
    else:
        print(f'[{stuff[i*3 + 2]}], [{stuff[i*3 + 1]}], [{stuff[i*3]}]')
print(f'Итоговые очки выживания: {2 * total_value+SET_POINTS-entire_value}')