class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 07/08/26

        # Iterating through the list
        # When we're looking at 3, we need a 4 to make 7

        # Then when we find 3, we need to return its pos

        # If we save the number needed and the pos
        # We need to be able to query the needed num and return the pos

        # Dict[needed] = pos
        # Dict[target - current] = pos

        # need = target - current
        # If need in d:
        #   return [dict[target], current_pos]

        d = {}

        for i, n in enumerate(nums):
            need = target - n
            if need in d:
                return [d[need], i]
            else:
                d[n] = i