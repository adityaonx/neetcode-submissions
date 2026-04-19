import collections

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the input array in place
        n = len(nums)
        out_ls = []

        for i in range(n - 2):  # Iterate up to n-2 to leave room for start and end
            # Skip duplicate values for 'i'
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start = i + 1
            end = n - 1

            while start < end:
                current_sum = nums[i] + nums[start] + nums[end]

                if current_sum == 0:
                    out_ls.append([nums[i], nums[start], nums[end]])
                    # Skip duplicate values for 'start' and 'end'
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif current_sum < 0:
                    start += 1
                else:  # current_sum > 0
                    end -= 1
        return out_ls