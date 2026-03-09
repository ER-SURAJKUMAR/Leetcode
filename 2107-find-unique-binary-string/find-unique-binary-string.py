class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        ans = []
        for i in range(len(nums)):
            # Character at current index i of the i-th string
            current_char = nums[i][i]
            
            # Flip the bit and add to our result
            ans.append('1' if current_char == '0' else '0')
            
        return "".join(ans)