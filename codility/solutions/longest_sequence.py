from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Check if it's the start of a sequence.
            # A number is the start of a sequence if the number before it
            # is not in the set.
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

    @staticmethod
    def are_consecutive(a: List[int]) -> bool:
        a = sorted(list(set(a)))  # Use set to handle duplicates
        return all(a[i] - a[i - 1] == 1 for i in range(1, len(a)))
        