# Time:  O(n)
# Space: O(1)

# Given an array of integers where 1 <= a[i] <= n (n = size of array),
# some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime?
# You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]


class Solution(object):

    def findDisappearedNumbers2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1, len(nums) + 1)) - set(nums))



if __name__ == '__main__':
    s = Solution()
    r = s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
    print r
