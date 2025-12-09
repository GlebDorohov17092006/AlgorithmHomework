from collections import deque
from typing import List

class Solution:
    def neighbours(self, cell: List[int], grid: List[str], keys: dict) -> List[List[int]]:
        neighbour = []
        m, n = len(grid), len(grid[0])
        for el in ([cell[0] + 1, cell[1]], [cell[0] - 1, cell[1]],[cell[0], cell[1]+1], [cell[0], cell[1]-1]):
            if not (0 <= el[0] < m and 0 <= el[1] < n):
                continue
                
            cell = grid[el[0]][el[1]]
            
            if cell == "#":
                continue
                
            if 'A' <= cell <= 'Z':
                if not keys.get(cell.lower(), False):
                    continue
            
            neighbour.append(el)
        return neighbour
    
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        start, keys = [], {}
        alf_small = "abcdefghijklmnopqrstuvwxyz"
        
        m, n = len(grid), len(grid[0])
        
        total_keys = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "@":
                    start = [i, j]
                elif grid[i][j] in alf_small:
                    keys[grid[i][j]] = 0
                    total_keys += 1
        
        if total_keys == 0:
            return 0
        
        all_keys_mask = (1 << total_keys) - 1
        
        key_to_index = {}
        key_idx = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] in alf_small:
                    key_to_index[grid[i][j]] = key_idx
                    key_idx += 1
        
        visited = [[[False] * n for _ in range(m)] for _ in range(1 << total_keys)]
        
        initial_mask = 0
        
        q = deque()
        q.append((start[0], start[1], initial_mask, 0))
        visited[initial_mask][start[0]][start[1]] = True
        
        while q:
            x, y, mask, steps = q.popleft()
            
            if mask == all_keys_mask:
                return steps
            
            cell = [x, y]
            
            temp_keys = {}
            for key_char, idx in key_to_index.items():
                temp_keys[key_char] = bool(mask & (1 << idx))
            
            for nx, ny in self.neighbours(cell, grid, temp_keys):
                new_mask = mask
                cell = grid[nx][ny]
                
                if cell in alf_small:
                    key_idx = key_to_index[cell]
                    new_mask = mask | (1 << key_idx)
                
                if not visited[new_mask][nx][ny]:
                    visited[new_mask][nx][ny] = True
                    q.append((nx, ny, new_mask, steps + 1))
        
        return -1