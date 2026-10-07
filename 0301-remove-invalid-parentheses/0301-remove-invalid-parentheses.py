from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        visited = {s}
        result = []
        found = False

        while queue:
            curr = queue.popleft()

            if is_valid(curr):
                result.append(curr)
                found = True

            # If we found at least one valid string at the current BFS depth,
            # do not generate further levels (ensures minimum removals).
            if found:
                continue

            for i in range(len(curr)):
                # Skip non-parenthesis characters
                if curr[i] not in '()':
                    continue

                # Generate state after removing character at index i
                next_str = curr[:i] + curr[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)

        return result