# https://www.reddit.com/r/dailyprogrammer/comments/5llkbj/2017012_challenge_298_easy_too_many_parentheses/
# [298] [Easy] [Too many parenthesis]

# ((a((bc)(de)))f)
# (((zbcd)(((e)fg))))
# ab((c))

# ((a((bc)(de)))f)  
# ((zbcd)((e)fg))
# ab(c)

def sol(exp):
    if (exp == "()"): return ""
    for i in range(0,len(exp)-1):
        if (exp[i] == ')'):
            ind = matching(exp, i)
            if (exp[ind+1:i] == ''):
                return sol(exp[:ind]+exp[i+1:])
            if ((exp[i+1] == ')') and exp[ind-1] == '('):
                return sol(exp[:ind-1] + exp[ind:i+1] + exp[i+2:])
    return exp
                
def matching(exp,ind):
    """
    Given an expression and a parenthesis, it returns
    the mathching index
    """
    stack = []
    if exp[ind] != ')':
        print ("Not a )")
        return None
    for i in range(0,ind):
        if (exp[i] == '('):
            stack.append(i)
        elif (exp[i] == ')'):
            stack.pop()
    return stack[-1]
            
sol("()")
