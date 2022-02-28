# 228. Summary Ranges
# You are given a sorted unique integer array nums.

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i=0
        s_index=0
        e_index=0
        result=[]
        temp=""
        nums.append(10000)
        while(i<len(nums)-1):
            if nums[i+1]==(nums[i]+1):
                e_index+=1
                i+=1
            else:
                if s_index==e_index:
                    temp=str(nums[s_index])
                else:
                    temp=str(nums[s_index])+"->"+str(nums[e_index])
                result.append(temp)
                s_index=i+1
                e_index=i+1
                i+=1
        return result
