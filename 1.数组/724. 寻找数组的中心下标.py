# https://leetcode.cn/problems/find-pivot-index/
class Solution:
    """
        1.从头开始遍历 nums[]
        2.index=0, 左边为0； index=len(nums)-1 右边为0
        3.判断 index左边的所有元素之和 是否等于 右边的所有元素之和
        4.第一次满足条件的则返回 下标，遍历完没有找到，则返回 -1
        eg:
            输入：nums = [1, 7, 3, 6, 5, 6]
            输出：3
            解释：
            中心下标是 3 。
            左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
            右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等
        这种2层循环，时间复杂度是 O(n^2) 效率太低
    """
    def pivotIndex(self, nums: list):
        n = len(nums)
        lsum , rsum = 0, 0
        for i in range(0, n):
            for j in range(0, i):
                lsum += nums[j]
            for j in range(i+1, n):
                rsum += nums[j]
            if lsum == rsum:
                return i
            lsum, rsum = 0, 0
        return -1
    '''
        改进：
            1.记数组的总和为 total
            2.求index 元素 左边的和 lsum
            3.则 index 右边的元素和 : total - lsum - nums[index] 
            4.若 total - lsum - nums[index]  = lsum 即返回下标index . 即 total = 2*lsum + nums[index]
    '''
    def pivotIndex2(self, nums:list):
        n = len(nums)
        total = sum(nums)
        lsum = 0
        for i in range(0, n):
            lsum += nums[i-1] if i > 0 else 0
            if total == 2*lsum + nums[i]:
                return i
        return -1
# 时间复杂度 ： O(n) , 空间复杂度 O(1)


nums = [1, 7, 3, 6, 5, 6]
s = Solution()
res = s.pivotIndex2(nums)
print(res)

