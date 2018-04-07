def infix_list():
    print('===============================')
    print('infix to postfix')
    print('use +, -, *, /, ^, (, )')
    print('===============================')

    infix = list(input('please enter infix: '))
    infix.append('q')
    return infix

def compare(stack, infix):
    infix_priority = ['q', ')', '+', '-', '*', '/', '^', ' ', '(']
    stack_priority = ['q', '(', '+', '-', '*', '/', '^', ' ']
    index_i = infix_priority.index(infix)
    index_s = stack_priority.index(stack)

    if int(index_i/2) < int(index_s/2):
        return 1
    else:
        return 0

def infix_to_postfix():
    infix = infix_list()
    stack = [''] * len(infix)
    stack[0] = 'q'
    top = 0

    print('postfix: ', end ='')

    for i in range(len(infix)):
        if infix[i] == ')':
            while stack[top] != '(':
                print('%c' %stack[top], end ='')
                top -= 1
            top -= 1

        elif infix[i] == 'q':
            while stack[top] != 'q':
                print('%c' %stack[top], end = '')
                top -= 1
                
        elif infix[i] == '(' or infix[i] == '^' or \
             infix[i] == '*' or infix[i] == '/' or \
             infix[i] == '+' or infix[i] == '-':
            while compare(stack[top], infix[i]) == 1:
               print('%c' %stack[top], end = '')
               top -= 1
            top += 1
            stack[top] = infix[i]

        else:
            print('%c' %infix[i], end = '')

                    

infix_to_postfix()
