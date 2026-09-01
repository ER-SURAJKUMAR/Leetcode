from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start_pos = None
        litter_positions = []
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_pos = (r, c)
                elif classroom[r][c] == 'L':
                    litter_positions.append((r, c))
                    
        num_litter = len(litter_positions)
        litter_map = {pos: i for i, pos in enumerate(litter_positions)}
        
        start_r, start_c = start_pos
        target_mask = (1 << num_litter) - 1
        
        # max_energy stores the maximum energy recorded for a given state (r, c, mask)
        max_energy = {}
        max_energy[(start_r, start_c, 0)] = energy
        
        # Queue elements: (row, col, collected_litter_mask, current_energy, steps)
        queue = deque([(start_r, start_c, 0, energy, 0)])
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, mask, cur_energy, steps = queue.popleft()
            
            if mask == target_mask:
                return steps
                
            if cur_energy == 0:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_energy = cur_energy - 1
                    next_mask = mask
                    
                    cell_type = classroom[nr][nc]
                    
                    if cell_type == 'L':
                        if (nr, nc) in litter_map:
                            litter_idx = litter_map[(nr, nc)]
                            next_mask |= (1 << litter_idx)
                    elif cell_type == 'R':
                        next_energy = energy
                    
                    state_key = (nr, nc, next_mask)
                    if state_key not in max_energy or max_energy[state_key] < next_energy:
                        max_energy[state_key] = next_energy
                        queue.append((nr, nc, next_mask, next_energy, steps + 1))
                        
        return -1