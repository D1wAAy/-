def corrected_copy(table, row_number, column_number, value):
    if row_number < 1 or row_number > len(table):
        return None
    if column_number < 1 or column_number > len(table[0]):
        return None
    if value < 0 or value > 100:
        return None
    new_table = [row.copy() for row in table]
    new_table[row_number - 1][column_number - 1] = value
    return new_table
table = [[70, 80], [60, 90]]
result = corrected_copy(table, 1, 2, 100)
print(result)
print(table)
result[1][0] = 0
print(table)
print(corrected_copy(table, 0, 1, 50))
print(corrected_copy(table, 1, 3, 50))
print(corrected_copy(table, 1, 1, -1))