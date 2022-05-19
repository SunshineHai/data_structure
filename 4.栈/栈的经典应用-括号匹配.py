class Solution:
    def isValid(self, s: str) -> bool:
        parens = "()[]{}"                           # 字符串中含有的所有 括号类型
        open_parens = "([{"                         # 开括号
        opposite = {")": "(", "]": "[", "}": "{"}   # 闭括号对应的开括号

        st = []                                     # 使用列表模拟栈, (左)开括号入栈
        for pr in s:
            if pr not in parens:
                return False                        # 字符串中含有除括号外的其它字符则返回 False
            elif pr in open_parens:                 # pr 如果为开括号 则压入栈 st 中
                st.append(pr)
            elif st == []:                          # 栈st为空，说明没有 左括号，只有右括号(eg:])，返回 False
                return False
            elif st.pop() != opposite[pr]:          # 右括号 和 左括号不匹配 eg:[[[){) 返回False
                return False
            else:
                pass

        # 检索完之后，如果出现 栈st 还有字符，可能字符串s只有单括号 如[， 返回False
        # if len(st) == 0:
        #     return True
        # else:
        #     return False
        return True if st == [] else False

if __name__ == '__main__':
    solution = Solution()
    res = solution.isValid("(()]}")
    print("res: ", res)