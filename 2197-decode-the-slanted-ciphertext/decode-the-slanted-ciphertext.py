class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText or rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        res = []
        
        # Each diagonal starts at (0, i) where i is the column index
        for i in range(cols):
            r, c = 0, i
            # Move diagonally down-right: (r+1, c+1)
            while r < rows and c < cols:
                # Calculate the flat index in the encodedText string
                index = r * cols + c
                res.append(encodedText[index])
                r += 1
                c += 1
        
        # Join and remove trailing spaces as per problem note
        return "".join(res).rstrip()