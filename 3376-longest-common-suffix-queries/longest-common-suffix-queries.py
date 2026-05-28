class TrieNode:
    def __init__(self):
        self.children = {}
        # Stores the index of the best word in wordsContainer passing through/ending at this node
        self.best_idx = -1 

class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        root = TrieNode()
        
        # Find the global default best index (shortest length, earliest occurrence)
        # This acts as our fallback if there's absolutely no common suffix.
        global_best_idx = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[global_best_idx]):
                global_best_idx = i
                
        root.best_idx = global_best_idx
        
        # Helper function to insert a word in reverse
        def insert(word: str, idx: int):
            curr = root
            # Update root fallback just in case, though handled above
            if curr.best_idx == -1 or len(word) < len(wordsContainer[curr.best_idx]):
                curr.best_idx = idx
                
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                
                # If this node doesn't have a word yet, or the new word is shorter
                if curr.best_idx == -1 or len(word) < len(wordsContainer[curr.best_idx]):
                    curr.best_idx = idx

        # 1. Build the Trie
        for i, word in enumerate(wordsContainer):
            insert(word, i)
            
        # 2. Query the Trie
        ans = []
        for query in wordsQuery:
            curr = root
            best_match = root.best_idx
            
            # Traverse matching characters from right to left
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                    best_match = curr.best_idx
                else:
                    break # Stop when the common suffix breaks
                    
            ans.append(best_match)
            
        return ans