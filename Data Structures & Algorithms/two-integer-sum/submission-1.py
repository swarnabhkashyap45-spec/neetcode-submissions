class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate through the numbers, put it in hashmap along with index
        # if (target-current number= number in hashmap, solution found)

        numberIndexMap = {}
        
        for idx, num in enumerate(nums):
            computed = target - num
            if computed in numberIndexMap:
                return [numberIndexMap[computed], idx]
            numberIndexMap[num] = idx
        
        return [-1, -1]

        