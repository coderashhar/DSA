class Solution:    
    def anagramStrings(self, s, t):
        #your code goes here
        if (len(s) != len(t)):
            return False

        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        for char in t:
            count[ord(char) - ord('a')] -= 1
        for i in count:
            if i != 0:
                return False
        return True