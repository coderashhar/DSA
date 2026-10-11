class Solution:
    def frequencySort(self, s):
        mp = {}
        for i in s:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] += 1

        sorted_chars = sorted(mp, key=lambda x: (-mp[x], x))
        return sorted_chars