from collections import deque

def calculate_flood_time(area_string):
    area_grid = [list(line) for line in area_string.strip().split('\n')]
    rows_num, cols_num = len(area_grid), len(area_grid[0])
    
    water_cells_queue = deque()
    flood_times = [[-1] * cols_num for _ in range(rows_num)]
    
    for row_idx in range(rows_num):
        for col_idx in range(cols_num):
            if area_grid[row_idx][col_idx] == 'W':
                water_cells_queue.append((row_idx, col_idx))
                flood_times[row_idx][col_idx] = 0
    
    move_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    maximum_time = 0
    while water_cells_queue:
        current_row, current_col = water_cells_queue.popleft()
        current_time_value = flood_times[current_row][current_col]
        
        for dr_val, dc_val in move_directions:
            next_row = current_row + dr_val
            next_col = current_col + dc_val
            
            if 0 <= next_row < rows_num and 0 <= next_col < cols_num:
                if area_grid[next_row][next_col] == 'L' and flood_times[next_row][next_col] == -1:
                    flood_times[next_row][next_col] = current_time_value + 1
                    water_cells_queue.append((next_row, next_col))
                    maximum_time = max(maximum_time, current_time_value + 1)
    
    return maximum_time