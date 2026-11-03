# space O(N)
# time O(N)
class Solution:
    # solution - 1 brute for 2 for loop space O(1) time O(n^2)
    
    # solution -2 sorting and then compare number and number next to it time O(nlogn) space 0(1) or 0(n) depends on sorting algo
    # solution - 3 
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen. add(num)
        return False

    # solution - 4
    def hasDuplicate1(self, nums: List[int]) -> bool:
        # set (nums) < len (nums) return true else false
        return len (set(nums)) < len(nums)

        
