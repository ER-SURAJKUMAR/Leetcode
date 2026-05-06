class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])

        # Step 1: Apply gravity to each row
        for r in range(rows):
            # Track the rightmost available position for a stone to fall into
            empty_pos = cols - 1
            for c in range(cols - 1, -1, -1):
                if boxGrid[r][c] == '#':
                    # Move stone to the empty_pos and mark current as empty
                    boxGrid[r][c] = '.'
                    boxGrid[r][empty_pos] = '#'
                    empty_pos -= 1
                elif boxGrid[r][c] == '*':
                    # Obstacle blocks stones, reset empty_pos to just before it
                    empty_pos = c - 1
                elif boxGrid[r][c] == '.':
                    # If it's already empty, we don't move empty_pos 
                    # unless a stone lands here later
                    pass

        # Step 2: Rotate the matrix 90 degrees clockwise
        # Original (r, c) maps to (c, rows - 1 - r)
        rotated_box = [['' for _ in range(rows)] for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                rotated_box[c][rows - 1 - r] = boxGrid[r][c]

        return rotated_box