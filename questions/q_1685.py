""" QUESTION 1685: Sum of Absolute Differences in a Sorted Array

You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such
that result[i] is equal to the summation of absolute differences between
nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where
0 <= j < nums.length and j != i (0-indexed).

Example 1:

Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
Example 2:

Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]

result[0] = |1-1|_ + |1-4| + |1-6| + |1-8| + |1-10|
result[1] = |4-1| + |4-4|_ + |4-6| + |4-8| + |4-10|
result[2] = |6-1| + |6-4| + |6-6|_ + |6-8| + |6-10|
result[3] = |8-1| + |8-4| + |8-6| + |8-8|_ + |8-10|
result[4] = |10-1| + |10-4| + |10-6| + |10-8| + |10-10|_

Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= nums[i + 1] <= 104
"""


# First approach.
# Memory usage limit and time limit exceeded
def getSumAbsoluteDifferencesApproach1(nums: list[int]) -> list[int]:
    nums_lenght: int = len(nums)
    prev: list[list[int]] = []

    for i in range(nums_lenght):
        prev.append([nums[j] - nums[i] for j in range(i, nums_lenght)])

    return [
        sum(prev[i] + [prev[j][i - j] for j in range(i)])
        for i in range(nums_lenght)
    ]


def getSumAbsoluteDifferences(nums: list[int]) -> list[int]:
    nums_lenght: int = len(nums)

    result = []
    pre_total = 0  # left side sum of the current index
    post_total = sum(nums)  # right side sum of the current index

    for i in range(nums_lenght):
        pre_total = pre_total + (nums[i - 1] if i > 0 else 0)
        post_total = post_total - nums[i]

        # Function explanation
        # result[i] = i*nums[i] - (n - i - 1)*nums[i] + post - pre
        result.append(
            (i * nums[i])
            - ((nums_lenght - i - 1) * nums[i])
            + post_total
            - pre_total
        )

    return result
