from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Create a hash map to hold our groups
        groups = defaultdict(list)
        
        # 1. Iterate using highly-optimized C internals (List Comprehension)
        # 2. 'sorted(w)' returns a list of characters, tuple() makes it hashable
        # 3. Zip preserves the link to the original word
        for sorted_tuple, original_word in ((tuple(sorted(w)), w) for w in strs):
            groups[sorted_tuple].append(original_word)
            
        # Return just the grouped lists
        return list(groups.values())