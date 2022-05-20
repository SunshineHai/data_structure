# https://leetcode.cn/problems/max-consecutive-ones/

class Solution:
    '''
        给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
        eg：
        输入：nums = [1,1,0,1,1,1]
        输出：3
        解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
        思路：

    '''
    def findMaxConsecutiveOnes(self, nums: list):
        maxCnt = cnt = 0
        
        for i in nums:
            if i == 1:
                cnt += 1
            else:
                maxCnt = max(maxCnt, cnt)
                cnt = 0
        maxCnt = max(maxCnt, cnt)   # 最后出现连续的 1 且长度最大时
        return maxCnt


nums = [0, 0, 0, 0]
s = Solution()
res = s.findMaxConsecutiveOnes(nums)
print(res)


