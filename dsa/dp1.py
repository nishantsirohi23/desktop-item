s = "k+l-M*n+(o-p)*w/u/v*t+q"
stack  =[]
res  = []
def hasHigherPrecedence(op1, op2):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    return precedence[op1] >= precedence[op2]

def checkAssociativity(stack, operator):
    while stack and stack[-1] in "+-*/" and hasHigherPrecedence(stack[-1], operator):
        # Pop operators from the stack until the condition is met
        stack.pop()
    
    # Push the current operator onto the stack
    stack.append(operator)
for char in s:
       if char =="+" or char =="-" or char =="/" or char =="*" or char==('(') or char==(')'):
            if not stack:
                stack.append(char)
            else:
                while stack and stack[-1] in "+-*/^(" and (char != ')' and hasHigherPrecedence(stack[-1], char)):
                    res.append(stack[-1])
                    stack.pop()

            
                if char != ')':
                    stack.append(char)
                
                     

       else:
            res.append(char)

       print(res,stack,char)


print(res)
                
