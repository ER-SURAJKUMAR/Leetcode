class Solution:

    def maxNumberOfFamilies(
        self, n: int, reservedSeats: list[list[int]]
    ) -> int:
        from collections import defaultdict

        # Map row -> bitmask of reserved seats (focusing on seats 2 through 9)
        reserved_rows = defaultdict(int)

        for r, c in reservedSeats:
            if 2 <= c <= 9:
                # Set bit (c - 2) for seats 2..9
                reserved_rows[r] |= 1 << (c - 2)

        # Max possible groups if no seats were reserved at all
        ans = n * 2

        # Bitmasks representing required clear seats
        # Left block: seats 2,3,4,5  -> bits 0,1,2,3 -> 0b00001111 (15)
        # Middle block: seats 4,5,6,7 -> bits 2,3,4,5 -> 0b00111100 (60)
        # Right block: seats 6,7,8,9  -> bits 4,5,6,7 -> 0b11110000 (240)
        LEFT_MASK = 15
        MIDDLE_MASK = 60
        RIGHT_MASK = 240

        for r, mask in reserved_rows.items():
            # A row starts with 2 potential groups. We deduce lost groups based on reservations.
            ans -= 2

            left_clear = (mask & LEFT_MASK) == 0
            right_clear = (mask & RIGHT_MASK) == 0
            middle_clear = (mask & MIDDLE_MASK) == 0

            if left_clear and right_clear:
                ans += 2
            elif left_clear or right_clear or middle_clear:
                ans += 1

        return ans