import sys

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()



def main():
    if len(sys.argv) != 2:
        print("ex1.py \" <s-expression> \"")
        sys.exit(1)

    expression = sys.argv[1]
    print("Received expression")
    tokens = tokenizer(expression)
    result = evaluate(tokens)
    print(f"The result of s-expression is: {result}")


def tokenizer(exp):
    exp = exp.replace("(", " ( ").replace(")", " ) ")
    tokens = exp.split()
    return tokens

def perform_op(x , y, op):
    if(op == '+'):
        return x + y
    elif(op == '-'):
        return x - y
    elif(op == '*'):
        return x * y
    elif(op == '/'):
        return x // y
    else:
        raise ValueError("Invalid operation")
    
        

def evaluate(tokens):
    result = 0
    stack = Stack()
    for i in range(len(tokens)):
        if(tokens[i] != ')'):
            stack.push(tokens[i])
        else:
            operand2 = int(stack.pop())
            operand1 = int(stack.pop())
            operation = stack.pop()
            stack.pop() #removes '('
            result = perform_op(operand1, operand2, operation)
            stack.push(result)
            
    return result        


            

if __name__ == "__main__" :
    main()