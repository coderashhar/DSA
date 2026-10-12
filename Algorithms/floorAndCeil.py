class Solution:
    def floorhelper(self, nums, x, low, high, floor) -> int:
        if low > high:
            return floor
        mid = (low + high) // 2
        if nums[mid] <= x :
            floor = max(nums[mid], floor) 
            low = mid + 1
            return self.floorhelper(nums, x, low, high, floor)
        else:
            high = mid - 1
            return self.floorhelper(nums, x, low, high, floor)
        


    def ceilhelper(self, nums, x, low, high, ceil) -> int:
        if low > high:
            return ceil
        mid = (low + high) // 2
        if nums[mid] >= x :
            if ceil != -1:
                ceil = min(nums[mid], ceil) 
            else:
                ceil = max(nums[mid], ceil)
            high = mid - 1
            return self.ceilhelper(nums, x, low, high, ceil)
        else:
            low = mid + 1
            return self.ceilhelper(nums, x, low, high, ceil)

    def getFloorAndCeil(self, nums, x):
        low = 0
        high = len(nums) - 1
        ans = [-1, -1]
        ans[0] = self.floorhelper(nums, x, low, high, ans[0])
        ans[1] = self.ceilhelper(nums, x, low, high, ans[1])
        return ans
    

       
