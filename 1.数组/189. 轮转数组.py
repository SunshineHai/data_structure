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
                直接调用 list 中的 方法，执行时间有点长，时间复杂度：O(n), 空间复杂度：O(n)
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

    def rotate3(self, nums: list, k: int):
        ''' 环形替换：
            思路：不定义新数组，在原数组的基础上实现
                1.开始 i = 0, 定义 temp = nums[0], new_index = (i + k) mod n
                2.重复步骤1，遍历 1圈回到 nums[0], 之后 i = 1,继续重复 步骤1
                3.循环 gcd(n, k) 次(证明较麻烦，先记住，或者使用count记录每次遍历的元素个数，count == n时 结束)
            时间复杂度：
            空间复杂度：O(1)
        '''
        def gcd(m, n):
            '''求最大公约数'''
            if m < n:
                m, n = n, m
            while(n != 0):
                r = m%n
                m = n
                n = r
            return m
            pass
        n = len(nums)  # 数组长度
        k = k % n
        cnt = gcd(n, k)
        for i in range(cnt):
            current = i         # 需要新定义一个变量
            temp = nums[current]
            while True:
                new_index = (current + k) % n
                temp, nums[new_index] = nums[new_index], temp
                current = new_index
                if current == i:      # 相当于是do...while循环，先执行一次，再判断
                    break
        return nums

    def rotate4(self, nums, k):
        """环形替换：循环次数使用 cnt 记录 元素个数，cnt == n 时结束循环"""
        n = len(nums)
        current = start = 0
        cnt = 0                 # 记录交换的元素总个数
        while cnt < n:          # 使用 cnt 判断 元素是否交换完
            temp = nums[current]
            while True:
                new_index = (current + k) % n
                temp, nums[new_index] = nums[new_index], temp
                current = new_index
                cnt += 1
                if current == start:
                    current += 1
                    start += 1
                    break
        return nums

    def rotate5(self, nums, k):
        '''数组反转:
            eg:
            nums = [1, 2, 3, 4, 5, 6, 7]; k = 3
            1.全部反转 [7, 6, 5, 4, 3, 2, 1]
            2.reverse(nums, 0, k-1) : [5, 6, 7, 4, 3, 2, 1]
            3.reverse(nums, k, len(nums)): [5, 6, 7, 1, 2, 3, 4]
        '''
        def reverse(nums:list, start:int, end:int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start+1, end-1
            pass
        n = len(nums)
        k %= n
        reverse(nums, 0, n-1)       # 全部反转
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
        pass



s = Solution()
nums = [1,2,3,4,5,6,7]
s.rotate5(nums, 3)
print(nums)

# my_list = []
# my_list.insert(0, 10)
# print(my_list)

