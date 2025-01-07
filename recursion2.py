# recursion
# callstack

#   example

#mam - she wanrs total now of rows in class room
# Debug and see in pycharm to understand call stack
# frames are created in stack to hold and process the data
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(1)
print(2)
print(3)
print(4)
print(5)
print(factorial(5))