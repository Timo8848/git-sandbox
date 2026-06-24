"""二分查找：边界条件多，适合演示'改同一行制造冲突'和写多个测试。"""

from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """在升序数组 nums 中查找 target，返回下标；找不到返回 -1。

    使用左闭右闭区间 [lo, hi]。
    """
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
