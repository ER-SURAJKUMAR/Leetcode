from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        
        freq = [0] * (n + 1)
        for factor, _ in items:
            freq[factor] += 1
            
        multiples_count = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f] > 0:
                for m in range(f, n + 1, f):
                    multiples_count[f] += freq[m]
                    
        items.sort(key=lambda x: x[1])
        
        min_price = items[0][1]
        total_items = 0
        rem_budget = budget
        
        for factor, price in items:
            if price >= 2 * min_price:
                break
                
            max_free = multiples_count[factor] - 1
            if max_free <= 0:
                continue
                
            can_buy = min(max_free, rem_budget // price)
            total_items += can_buy * 2
            rem_budget -= can_buy * price
            
            if can_buy < max_free:
                break
                
        total_items += rem_budget // min_price
        
        return total_items