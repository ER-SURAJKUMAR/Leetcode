class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        answer = []
        for num in nums:
            # Convert number to string to iterate through digits
            for digit in str(num):
                answer.append(int(digit))
        return answer