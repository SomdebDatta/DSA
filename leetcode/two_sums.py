from typing import List


# def two_sums(nums1: list, nums2: list, m, n):
def two_sums(nums1: List[int], m: int, nums2: List[int], n: int):
    end = m + n - 1
    nums1end = m - 1
    nums2end = n - 1
    while nums2end >= 0:
        if nums1end < 0:
            nums1[end] = nums2[nums2end]
            nums2end -= 1
            end -= 1
            continue
        if nums1[nums1end] > nums2[nums2end]:
            nums1[end] = nums1[nums1end]
            nums1end -= 1
        else:
            nums1[end] = nums2[nums2end]
            nums2end -= 1
        end -= 1
    print(nums1)


two_sums([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
two_sums([2, 0], 1, [1], 1)
two_sums([5, 6, 7, 0, 0, 0, 0], 3, [1, 2, 3, 4], 4)
two_sums([0], 0, [1], 1)
two_sums([1], 1, [], 0)
