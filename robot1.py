from collections import deque

def solve_maze_one_robot(lab_string):
    lab_map = [list(line) for line in lab_string.strip().split('\n')]
    rows_num, cols_num = len(lab_map), len(lab_map[0])
    
    start_location = None
    for row_idx in range(rows_num):
        for col_idx in range(cols_num):
            if lab_map[row_idx][col_idx] == 'S':
                start_location = (row_idx, col_idx)
                break
        if start_location:
            break
    
    cell_queue = deque([start_location])
    parent_cell = {start_location: None}
    moves_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    exit_found_status = False
    exit_position = None
    
    while cell_queue:
        current_row, current_col = cell_queue.popleft()
        
        if current_row == 0 or current_row == rows_num-1 or current_col == 0 or current_col == cols_num-1:
            if lab_map[current_row][current_col] != '#':
                exit_found_status = True
                exit_position = (current_row, current_col)
                break
        
        for dr_val, dc_val in moves_list:
            next_row, next_col = current_row + dr_val, current_col + dc_val
            
            if 0 <= next_row < rows_num and 0 <= next_col < cols_num:
                if lab_map[next_row][next_col] != '#' and (next_row, next_col) not in parent_cell:
                    parent_cell[(next_row, next_col)] = (current_row, current_col)
                    cell_queue.append((next_row, next_col))
    
    if exit_found_status:
        path_cells = []
        current_pos = exit_position
        while current_pos:
            path_cells.append(current_pos)
            current_pos = parent_cell[current_pos]
        path_cells.reverse()
        
        for r_pos, c_pos in path_cells[1:-1]:
            lab_map[r_pos][c_pos] = 'o'
        if exit_position != start_location:
            lab_map[exit_position[0]][exit_position[1]] = 'o'
    
    return '\n'.join(''.join(row) for row in lab_map)