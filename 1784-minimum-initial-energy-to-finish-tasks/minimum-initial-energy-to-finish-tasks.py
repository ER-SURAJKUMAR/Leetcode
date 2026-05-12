class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        # Sort tasks by the difference between minimum and actual (descending)
        # This prioritizes tasks that require much more energy to start than to finish
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        min_initial_energy = 0
        current_energy = 0
        
        for actual, minimum in tasks:
            # If current energy is less than what's needed to start the task
            if current_energy < minimum:
                # Add the deficit to our initial starting energy
                min_initial_energy += (minimum - current_energy)
                # After adding the deficit, our current energy is exactly the 'minimum'
                current_energy = minimum
            
            # Spend the energy required for the task
            current_energy -= actual
            
        return min_initial_energy