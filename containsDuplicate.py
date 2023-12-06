class Solution(object):
    def containsDuplicate(self, nums):

        seen = set()

        for i in len(nums):
            if i in seen:
                return True
            seen.add(i)
        return False




        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        #
        # return False
# The above has a Time complexity of o(n^2)
