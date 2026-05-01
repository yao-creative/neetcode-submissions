class Solution:
    def eval_operator(self, first, second, operator) -> int:
        if operator == '+':
            return first + second
        elif operator == '*':
            return first * second
        elif operator == '-':
            return first - second
        elif operator == '/':
            return int(first / second)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in ['+', '-', '*', '/']:
                second = stack.pop()
                first = stack.pop()
                res = self.eval_operator(first, second, tokens[i])
                stack.append(res)
            else: #number case
                stack.append(int(tokens[i]))
        return stack[0]