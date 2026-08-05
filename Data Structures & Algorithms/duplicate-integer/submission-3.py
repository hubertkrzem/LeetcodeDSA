class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for num in nums: # O(n)
            if num in nums_dict: # O(1)
                return True
            else: # O(1)
                nums_dict[num] = True
        return False