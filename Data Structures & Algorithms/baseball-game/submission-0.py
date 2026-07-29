class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                stack.append(sum(stack[-2:]))
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(int(2 * stack[-1]))
            else:
                stack.append(int(op))

        return sum(stack)
