# Recursion

# Factorial of 5
# 5! =  5*4*3*2*1 = 120
# 5 * 4!
# 5 * 4 * 3!
# 5 * 4 * 3 * 2!

n = 5
# base condition (where the condition should stop)
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(n))




