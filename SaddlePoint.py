matrix = [[10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10]]
row_max = len(matrix)
col_max = len(matrix[0])


for row in range(row_max):
    max_row = max(matrix[row])
    min_row = min(matrix[row])

    max_row_idx = matrix[row].index(max_row)
    min_row_idx = matrix[row].index(min_row)

    min_column = min([matrix[i][max_row_idx] for i in range(row_max)])
    max_column = max([matrix[i][min_row_idx] for i in range(row_max)])

    if max_row == min_column :
        print(f"Saddle Point number {max_row} found at row = {row} and col = {max_row_idx}")

    if min_row == max_column :
        print(f"Saddle Point number {min_row} found at row = {min_row_idx} and col = {row}")