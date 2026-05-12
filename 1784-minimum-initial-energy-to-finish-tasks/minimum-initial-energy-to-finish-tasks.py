class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        # Sort tasks by the difference between minimum required and actual spent
        # We want to perform tasks with the largest "buffer" first.
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        total_required = 0
        current_spent = 0
        
        for actual, minimum in tasks:
            # We need to ensure that: 
            # initial_energy - current_spent >= minimum
            # Therefore: initial_energy >= current_spent + minimum
            if total_required < current_spent + minimum:
                total_required = current_spent + minimum
            
            # Update the total energy consumed after finishing the task
            current_spent += actual
            
        return total_required