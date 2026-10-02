class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(open_n: int, closed_n: int, path: str):
            # Base case: valid combination reached
            if len(path) == 2 * n:
                res.append(path)
                return
            
            # Can add an open parenthesis if we haven't used all 'n' of them
            if open_n < n:
                backtrack(open_n + 1, closed_n, path + "(")
            
            # Can add a closing parenthesis if it matches a previously opened one
            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, path + ")")
        
        backtrack(0, 0, "")
        return res