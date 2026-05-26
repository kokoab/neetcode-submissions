class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map = {}

        for i in range(len(s)):
            map[s[i]] = 1 + map.get(s[i], 0)
            map[t[i]] = map.get(t[i], 0) - 1

        return all(value == 0 for value in map.values())


