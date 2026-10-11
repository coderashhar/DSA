class Solution:
    def isomorphicString(self, s : str, t : str) -> bool:
        if (len(s) != len(t)):
            return False
        mp = {}
        rmp = {}
        i = 0
        while i < len(s):
            if s[i] not in mp:
                mp[s[i]] = t[i]
            elif mp[s[i]] != t[i]:
                return False
            if t[i] not in rmp:
                rmp[t[i]] = s[i]
            elif rmp[t[i]] != s[i]:
                return False
            i += 1
        return True