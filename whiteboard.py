# Compute Intersection
# ====================
# Given two arrays, write a function to compute their intersection.
# Example 1:
nums1 = [1,2,2,1]
nums2 = [2,2]
# Output: [2]
# Example 2:
nums3 = [4,9,5]
nums4 = [9,4,9,8,4]
# Output: [9,4]
# Note:
# Each element in the result must be unique.
# The result can be in any order.

def intersection(a,b):
    return list(set(a).intersection(b))

print(intersection(nums3, nums4))
