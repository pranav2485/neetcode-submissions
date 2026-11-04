class Solution:
    """ 
    brute force itterate over using 2 loops 
    time O(n^1)
    space O(1)

    """


    def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range(i+1, len(nums)):
                if (target == nums[i] + nums[j]):
                    return [i,j]
        return []    


    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {} # num -> index 
        for i in range (len(nums)):
            n = nums[i]
            diff = target - n
            if diff in map:
                return [map[diff], i]
            map[n] = i     


        