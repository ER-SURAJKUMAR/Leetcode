class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        if not costs:
            return 0
        
        max_cost = max(costs)
        # Create a frequency array to store the count of each ice cream cost
        frequency = [0] * (max_cost + 1)
        for cost in costs:
            frequency[cost] += 1
            
        ice_cream_count = 0
        
        # Iterate through each possible cost from 1 to max_cost
        for cost in range(1, max_cost + 1):
            if frequency[cost] == 0:
                continue
                
            # If we can't even afford one ice cream of this cost, we are done
            if coins < cost:
                break
                
            # Calculate how many bars of this cost we can afford
            count_to_buy = min(frequency[cost], coins // cost)
            
            # Update our totals
            ice_cream_count += count_to_buy
            coins -= count_to_buy * cost
            
        return ice_cream_count