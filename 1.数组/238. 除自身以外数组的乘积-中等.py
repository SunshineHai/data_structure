# https://leetcode.cn/problems/product-of-array-except-self/

'''
    238. 除自身以外数组的乘积
            给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
            题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
            请不要使用除法，且在 O(n) 时间复杂度内完成此题。

        示例 1:
            输入: nums = [1,2,3,4]
            输出: [24,12,8,6]
        示例 2:
            输入: nums = [-1,1,0,-3,3]
            输出: [0,0,9,0,0]
'''


class Solution:
    '''
        要求：时间复杂度 O(n)
        方法一：
        1.从头遍历， 累成除去当前位置元素
        这种方法属于暴力破解，可以解决问题，但是时间复杂度是 O(n^2)
    '''
    def productExceptSelf(self, nums: list):
        n = len(nums)
        answer = []
        for i in range(n):
            sum = 1
            for j in range(n):
                if i == j:
                    continue
                if nums[j] == 0:
                    sum = 0
                    break
                sum *= nums[j]
            answer.append(sum)
        return answer

    def productExceptSelf2(self, nums: list):
        '''
            左右乘积列表法：
                1.遍历 nums[] 数组， 定义 Left/Right 数组，分别存放当前元素左边、右边所有元素的成绩
                2.当 i = 0 时， nums 数组左边没有元素，默认 Left[0] = 1
                3.当 i = len(nums)-1 时， 数组右边没有元素，默认 Right[len(nums-1)] = 1
                4.Left 和 Right 数组 各个元素对应相乘即可得到 每个元素 对应的结果。
            时间复杂度：O(n)
        '''
        n = len(nums)
        answer = []
        left, right = [0]*n, [0]*n
        sum = 1
        # 计算 left
        for i in range(n):
            if i == 0:
                left[i] = 1
            else:
                sum *= nums[i-1]
                left[i] = sum
        sum = 1
        # 计算 right
        for i in range(n-1, -1, -1):
            if i == n-1:
                right[i] = 1
            else:
                sum *= nums[i+1]
                right[i] = sum
        # left 和 right 各个元素相乘即可得到答案
        for i, j in zip(left, right):
            answer.append(i*j)
        return answer

    def productExceptSelf3(self, nums: list):
        '''
            左右乘积列表法：时间复杂度 O(n), 空间复杂度 O(n)   (重点掌握)
                该方法依然和上一个方法一样，目的是使 代码 更加简洁。
        '''
        n = len(nums)
        left, right, answer = [0]*n, [0]*n, [0] * n
        left[0] = 1       # 下标为 0 时， nums[0] 左边没有元素，默认为1.
        # 计算 left
        for i in range(1, n):
            left[i] = nums[i-1] * left[i-1]     # nums的前一个元素 * 前一个计算过的 left
        # 计算 right
        right[n-1] = 1
        for i in range(n-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]   # nums 的后一个元素 * 后一个计算过的 right,以免重复计算
        # left 和 right 各个元素相乘即可得到答案
        for i in range(n):
            answer[i] = left[i] * right[i]
        return answer

    def productExceptSelf4(self, nums: list):
        '''优化：空间复杂度：O(1)
            不定义 left、right数组，answer 数组 存放 left里的内容， 并 使用 R 变量临时存放 right计算的结果，然后 再更新 answer数据
        '''
        n = len(nums)
        # answer 先存放 left 值
        answer = [0] * n
        answer[0] = 1
        for i in range(1, n):
            answer[i] = nums[i-1] * answer[i-1]

        R = 1
        for i in reversed(range(n)):
            # 更新 answer
            answer[i] = answer[i] * R
            R *= nums[i]              # 这是 下一个 的 R
        return answer


nums = [1, 2, 3, 4]
s = Solution()
res = s.productExceptSelf4(nums)
print(res)
n = len(nums)

# for i in range(n-1):
#     print(i)
#
# for i in reversed(range(n-1)):
#     print(i)