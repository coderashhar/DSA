class Solution:
    def countStudents(self, nums, pages) -> int:
        n = len(nums) 
        students = 1
        pagesStudent = 0
        for i in range(n):
            if pagesStudent + nums[i] <= pages:
                pagesStudent += nums[i]
            else:
                students += 1
                pagesStudent = nums[i]
        return students

    def findPages(self, nums, m):
        n = len(nums)
        if m > n:
            return -1
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high) // 2
            students = self.countStudents(nums, mid)
            if students > m:
                low = mid + 1
            else:
                high = mid - 1
        return low


                