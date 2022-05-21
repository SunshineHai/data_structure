# https://leetcode.cn/problems/rotate-array/

class Solution:
    def rotate(self, nums: list, k: int):
        """
            Do not return anything, modify nums in-place instead.
            给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
            eg:
                输入：nums = [-1,-100,3,99], k = 2
                输出：[3,99,-1,-100]
                解释:
                向右轮转 1 步: [99,-1,-100,3]
                向右轮转 2 步: [3,99,-1,-100]
            思路：
                直接调用 list 中的 方法，执行时间有点长
        """
        for i in range(k):
            nums.insert(0, nums.pop())
        pass

    def rotate2(self, nums: list, k: int):
        '''
            思路：使用新数组, 以空间换时间
                1.假如 i 表示 数组的下标， k 表示移动的长度，n是数组的长度,则 移动之后i对应的新的下标为 (i+k)%n
        '''
        n = len(nums)
        new_list = []
        for i, num in enumerate(nums):
            new_index = (i+k) % n
            new_list.insert(new_index, num)

        for i in range(n):
            nums[i] = new_list[i]
        pass


s = Solution()
nums = [1,2,3,4,5,6,7]
s.rotate2(nums, 3)
print(nums)

# my_list = []
# my_list.insert(0, 10)
# print(my_list)
