class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for st in s:
            if st in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[st] != top_element:
                    return False
            else:
                stack.append(st)
        return not stack
            
        
# Runtime: 36 ms, faster than 30.47% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.8 MB, less than 77.84% of Python3 online submissions for Valid Parentheses.
