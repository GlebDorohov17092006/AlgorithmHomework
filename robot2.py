from collections import deque

def solve_two_robots(lab_string):
    lab_map = [list(line) for line in lab_string.strip().split('\n')]
    rows_num, cols_num = len(lab_map), len(lab_map[0])
    
    positions_dict = {}
    for row_idx in range(rows_num):
        for col_idx in range(cols_num):
            if lab_map[row_idx][col_idx] in ['A', 'B', 'F']:
                positions_dict[lab_map[row_idx][col_idx]] = (row_idx, col_idx)
    
    robot_a_pos = positions_dict['A']
    robot_b_pos = positions_dict['B']
    finish_pos = positions_dict['F']
    
    def compute_distances(start_point):
        distance_grid = [[float('inf')] * cols_num for _ in range(rows_num)]
        dist_queue = deque([start_point])
        distance_grid[start_point[0]][start_point[1]] = 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while dist_queue:
            cr, cc = dist_queue.popleft()
            for dr_val, dc_val in directions:
                nr, nc = cr + dr_val, cc + dc_val
                if 0 <= nr < rows_num and 0 <= nc < cols_num:
                    if lab_map[nr][nc] != '#' and distance_grid[nr][nc] == float('inf'):
                        distance_grid[nr][nc] = distance_grid[cr][cc] + 1
                        dist_queue.append((nr, nc))
        return distance_grid
    
    dist_a = compute_distances(robot_a_pos)
    dist_b = compute_distances(robot_b_pos)
    dist_f = compute_distances(finish_pos)
    
    min_total_cost = float('inf')
    meeting_point = finish_pos
    
    for row_idx in range(rows_num):
        for col_idx in range(cols_num):
            if lab_map[row_idx][col_idx] != '#':
                cost_value = dist_a[row_idx][col_idx] + dist_b[row_idx][col_idx] + dist_f[row_idx][col_idx]
                if cost_value < min_total_cost:
                    min_total_cost = cost_value
                    meeting_point = (row_idx, col_idx)
    
    def reconstruct_path(start_pt, end_pt, dist_grid):
        path_points = []
        current = end_pt
        
        if dist_grid[end_pt[0]][end_pt[1]] == float('inf'):
            return path_points
        
        dir_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while current != start_pt:
            path_points.append(current)
            cr, cc = current
            for dr_val, dc_val in dir_list:
                nr, nc = cr + dr_val, cc + dc_val
                if 0 <= nr < rows_num and 0 <= nc < cols_num:
                    if dist_grid[nr][nc] == dist_grid[cr][cc] - 1:
                        current = (nr, nc)
                        break
        return path_points
    
    path_a_to_m = reconstruct_path(robot_a_pos, meeting_point, dist_a)
    path_b_to_m = reconstruct_path(robot_b_pos, meeting_point, dist_b)
    path_m_to_f = reconstruct_path(meeting_point, finish_pos, dist_f) if meeting_point != finish_pos else []
    
    all_path_cells = set()
    all_path_cells.update(path_a_to_m)
    all_path_cells.update(path_b_to_m)
    all_path_cells.update(path_m_to_f)
    
    result_grid = [row[:] for row in lab_map]
    
    for r_pos, c_pos in all_path_cells:
        if result_grid[r_pos][c_pos] not in ['A', 'B', 'F', 'M']:
            result_grid[r_pos][c_pos] = 'o'
    
    if meeting_point != finish_pos:
        mr, mc = meeting_point
        result_grid[mr][mc] = 'M'
    
    return '\n'.join(''.join(row) for row in result_grid)