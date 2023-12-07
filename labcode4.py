SET_POINTS = 10
BACKPACK_SIZE = 9
ROWS = 3
COLS = 3

def get_area_and_value(dict):
    area = [dict[item][0] for item in dict]
    value = [dict[item][1] for item in dict]
    return area, value

def get_memtable(stuff_dictionary):
    area, value = get_area_and_value(stuff_dictionary)
    total_number = len(value)
    matrix = [[0 for a in range(BACKPACK_SIZE + 1)] for i in range(total_number + 1)]

    for i in range(total_number + 1):
        mtrx_curr = matrix[i]
        mtrx_prev = matrix[i - 1]
        for a in range(BACKPACK_SIZE + 1):
            if i == 0 or a == 0:
                mtrx_curr[a] = 0

            elif area[i - 1] <= a:
                prev_area = area[i - 1]
                mtrx_curr[a] = max(value[i - 1]+mtrx_prev[a - prev_area], mtrx_prev[a])

            else:
                mtrx_curr[a] = mtrx_prev[a]
    return matrix, area, value

def get_selected_items_list(stuff_dictionary):
    matrix, area, value = get_memtable(stuff_dictionary)
    total_number = len(value)
    res = matrix[total_number][BACKPACK_SIZE]
    variable_area = BACKPACK_SIZE
    items_list = []

    for i in range(total_number-1, -1, -1):
        if res <= 0:
            break
        if res == matrix[i][variable_area]:
            continue
        else:
            items_list.append((area[i], value[i]))
            res -= value[i]
            variable_area -= area[i]

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
    total_value += stuff_dictionary[item][1] // stuff_dictionary[item][0]

entire_value = sum([stuff_dictionary[item][1] for item in stuff_dictionary])

stuff_size = len(stuff)
for row_start in range(0, stuff_size, COLS):
    row = stuff[row_start : row_start+COLS]
    for item in row:
         print(f'[{item}]', end =' ')
    print()
