"""
Programming in Java: An Interdisciplinary Approach
p. 598 - Problem 4.3.15
"""

def EvaluatePostfix(expression):
    operators = { '+': operator.add 
                , '-': operator.sub 
                , '/': operator.itruediv
                , '*': operator.mul}
    operand_stack = []
    
    expression = expression.strip().split(' ')      # Parse expression
    
    for ch in expression:                           # Iterate through parsed expression
        if ch in operators.keys():                  # If operator is found, pop two and combine
            a, b = operand_stack.pop(), operand_stack.pop()
            c = operators[ch](float(b), float(a))
            operand_stack.append(c)
        else:                                       
            operand_stack.append(ch)                # If operand is found, push on stack
    
    return operand_stack
