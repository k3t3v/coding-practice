from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
    

# Sample call
sol = Solution()
print(sol.hasDuplicate([1, 2, 3, 3]))  # Output: True
print(sol.hasDuplicate([1, 2, 3, 4]))  # Output: False