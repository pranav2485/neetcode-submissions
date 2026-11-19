class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    

        """
        [-1,0,1,2,-1,-4]
        [-4,-1,-1,0,1,2]

        [-2,0,0,2,2]


        """
        res = []
        nums.sort()

        for i, a in enumerate (nums):
            # if value in array at any point > 0 we can break and return res at this 
            # point as array is sorted no need to check other value in array 
            if a > 0:
                break

            # [-4,-1,-1,0,1,2] when we ll pick first -1 we have triplet [-1,0,1]
            # while second -1 will pick up the same triplet so adding a condition
            # that if current value is same as previos we can skip it 
            if i > 0 and a == nums[i-1]:    
                continue


            l, r = i+1, len(nums) -1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                # print('a',a,'nums[l]', nums[l], 'nums[r]', nums[r])
                # print('threeSum', threeSum)
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    # [-2,0,0,2,2] if we do not add this we ll return 
                    # [[-2,0,2],[-2,0,2]] whiile we need [[-2,0,2]]
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            
        return res;        









    
    


    # [-1,0,1,2,-1,-4]
    # -4,-1,-1,0,1,2

    # [[-1,-1,2],[-1,0,1]]