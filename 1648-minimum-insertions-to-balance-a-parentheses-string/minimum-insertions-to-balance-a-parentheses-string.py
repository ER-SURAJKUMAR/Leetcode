class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_needed = 0  # Number of '(' currently waiting for two ')'
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                open_needed += 1
                i += 1
            else:  # s[i] == ')'
                # Check if we have a consecutive '))'
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    # Single ')' found, we need to insert one ')' to make it '))'
                    insertions += 1
                    i += 1

                # Match with a '(' if available, otherwise insert a '('
                if open_needed > 0:
                    open_needed -= 1
                else:
                    insertions += 1

        # Each unmatched '(' needs two ')'
        insertions += open_needed * 2

        return insertions