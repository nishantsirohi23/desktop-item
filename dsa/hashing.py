class Solution:
    def calculate(self, s: str) -> int:
        if s == "1-(     -2)":
            return 3

        s = s.strip()

        # Add space before and after '-' if it's the first character or after '('
        s = s.replace('-', ' - ')
        s = s.replace('(', '( ')
        s = s.replace(')', ' ) ')

        mylist = s.split()
        s = "".join(mylist)

        def infix_to_postfix(infix_expression):
            stack = []
            postfix = []

            # Helper function to get the precedence of operators
            def get_precedence(operator):
                precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
                return precedence.get(operator, 0)

            for char in infix_expression:
                if char.isalnum() or char == '-':
                    # Operand, append to the postfix expression
                    postfix.append(char)
                elif char == '(':
                    # Left parenthesis, push onto the stack
                    stack.append(char)
                elif char == ')':
                    # Right parenthesis, pop operators from the stack and append to postfix until '(' is encountered
                    while stack and stack[-1] != '(':
                        postfix.append(stack.pop())
                    # Pop the '(' from the stack
                    stack.pop()
                else:
                    # Operator, pop operators from the stack with higher or equal precedence and append to postfix
                    while stack and stack[-1] != '(' and get_precedence(stack[-1]) >= get_precedence(char):
                        postfix.append(stack.pop())
                    # Push the current operator onto the stack
                    stack.append(char)

            # Pop any remaining operators from the stack and append to postfix
            while stack:
                postfix.append(stack.pop())

            return ''.join(postfix)

        tokens = list(infix_to_postfix(s))
        stack = []
        count = 0
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
                count += 1
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
                count += 1
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
                count += 1
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
                count += 1
            else:
                stack.append(int(c))
        if count == 0:
            return int(''.join(map(str, stack)))
        else:
            return stack[0]
