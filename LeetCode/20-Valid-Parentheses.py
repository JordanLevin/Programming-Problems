class Solution(object):
    def isValid(self, s):
        parens = {')': '(', '}':'{', ']':'['}
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if len(stack) > 0 and stack[len(stack)-1] == parens[i]:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True