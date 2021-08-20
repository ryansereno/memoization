
def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))


def gT(m,n, memo = {}):
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    else:
        memo[key] = gT(m-1,n, memo) + gT(m,n-1, memo)
    return memo[key]

print(gT(3,3))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(44))

def arraySum(array):
    sum = 0
    for i in array:
        sum = sum + i
    return sum


def canSum(targetSum, numbers, memo = {}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for i in numbers:
        remainder = targetSum - i
        if canSum(remainder, numbers, memo) == True:
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False

print(canSum(705,[5,5,5]))


def howSum(targetSum, numbers, memo = []):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for i in numbers:
        remainder = targetSum - i
        remainderResult = howSum(remainder, numbers, memo)
        if remainderResult != None:
            return remainderResult + [i]
    return None

print('\n' +  'howSum Function:')
print(howSum(1, [4,4,3]))
