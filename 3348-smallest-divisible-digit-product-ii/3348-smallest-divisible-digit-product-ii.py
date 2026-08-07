class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Prime factorize t into 2, 3, 5, 7
        temp_t = t
        req2 = req3 = req5 = req7 = 0
        while temp_t % 2 == 0: req2 += 1; temp_t //= 2
        while temp_t % 3 == 0: req3 += 1; temp_t //= 3
        while temp_t % 5 == 0: req5 += 1; temp_t //= 5
        while temp_t % 7 == 0: req7 += 1; temp_t //= 7
        
        # If t has factors other than 2, 3, 5, 7, impossible
        if temp_t > 1:
            return "-1"

        def get_needed_len(c2, c3, c5, c7):
            """Returns (length, string) of minimal digit sequence needed."""
            if c2 <= 0 and c3 <= 0 and c5 <= 0 and c7 <= 0:
                return 0, ""

            c2 = max(0, c2)
            c3 = max(0, c3)
            c5 = max(0, c5)
            c7 = max(0, c7)

            d9, rem_c3 = divmod(c3, 2)
            d8, rem_c2 = divmod(c2, 3)

            d6 = d4 = d3 = d2 = 0

            if rem_c3 == 1 and rem_c2 == 1:
                d6 = 1
            elif rem_c3 == 1 and rem_c2 == 2:
                d6 = 1
                d2 = 1
            else:
                if rem_c3 == 1:
                    d3 = 1
                if rem_c2 == 2:
                    d4 = 1
                elif rem_c2 == 1:
                    d2 = 1

            total_len = d2 + d3 + d4 + c5 + d6 + c7 + d8 + d9
            res = (
                '2' * d2 + '3' * d3 + '4' * d4 + '5' * c5 +
                '6' * d6 + '7' * c7 + '8' * d8 + '9' * d9
            )
            return total_len, res

        # Factor contributions for digits 0-9
        digit_factors = [
            (0, 0, 0, 0), (0, 0, 0, 0), (1, 0, 0, 0), (0, 1, 0, 0),
            (2, 0, 0, 0), (0, 0, 1, 0), (1, 1, 0, 0), (0, 0, 0, 1),
            (3, 0, 0, 0), (0, 2, 0, 0)
        ]

        n = len(num)
        zero_idx = num.find('0')

        # Precompute prefix factor counts up to the first '0'
        max_pref_len = zero_idx if zero_idx != -1 else n
        pref2 = [0] * (max_pref_len + 1)
        pref3 = [0] * (max_pref_len + 1)
        pref5 = [0] * (max_pref_len + 1)
        pref7 = [0] * (max_pref_len + 1)

        for i in range(max_pref_len):
            d = int(num[i])
            c2, c3, c5, c7 = digit_factors[d]
            pref2[i + 1] = pref2[i] + c2
            pref3[i + 1] = pref3[i] + c3
            pref5[i + 1] = pref5[i] + c5
            pref7[i + 1] = pref7[i] + c7

        # Case 1: Check if num itself is valid (only if num has no zeros)
        if zero_idx == -1:
            need_len, _ = get_needed_len(req2 - pref2[n], req3 - pref3[n], req5 - pref5[n], req7 - pref7[n])
            if need_len == 0:
                return num

        # Case 2: Try replacing digit at index i (i <= max_pref_len) with a strictly larger digit
        # If there's a zero at zero_idx, we must change digit at or before zero_idx
        limit = zero_idx if zero_idx != -1 else n - 1

        for i in range(limit, -1, -1):
            rem2 = req2 - pref2[i]
            rem3 = req3 - pref3[i]
            rem5 = req5 - pref5[i]
            rem7 = req7 - pref7[i]

            rem_len = n - 1 - i

            start_d = int(num[i]) + 1
            for d in range(start_d, 10):
                dc2, dc3, dc5, dc7 = digit_factors[d]
                need_l, need_s = get_needed_len(rem2 - dc2, rem3 - dc3, rem5 - dc5, rem7 - dc7)

                if need_l <= rem_len:
                    padding = '1' * (rem_len - need_l)
                    return num[:i] + str(d) + padding + need_s

        # Case 3: If length n is impossible, generate minimal result of length n + 1 (or required length)
        all_len, all_str = get_needed_len(req2, req3, req5, req7)
        target_len = max(n + 1, all_len)
        return '1' * (target_len - all_len) + all_str