class Solution:    
    def rotateString(self, s, goal):
        #your code goes here
        if len(s) != len(goal):
            return False
        return goal in (s+s)
            