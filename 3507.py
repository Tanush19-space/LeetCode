class Solution:
    def minimumPairRemoval(self, nums):
        def is_non_decreasing(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True

        operations = 0

        while not is_non_decreasing(nums):

            # Find leftmost adjacent pair with minimum sum
            min_sum = float('inf')
            idx = 0

            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]

                if pair_sum < min_sum:
                    min_sum = pair_sum
                    idx = i

            # Merge the pair
            nums[idx] = nums[idx] + nums[idx + 1]
            nums.pop(idx + 1)

            operations += 1

        return operations