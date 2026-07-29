class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        bracket_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in ["[", "(", "{"]:
                stack.append(char)
            else:
                if len(stack) == 0 or stack[-1] != bracket_map.get(char):
                    return False
                stack.pop()
            
        return len(stack) == 0
