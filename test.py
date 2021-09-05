
def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
print(fib(5))
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


def howSum(targetSum, numbers, memo = {}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for i in numbers:
        remainder = targetSum - i
        remainderResult = howSum(remainder, numbers, memo)
        if remainderResult != None:
            memo[targetSum] = remainderResult + [i]
            return memo[targetSum]
    memo[targetSum] = None
    return None

print('\n' +  'howSum Function:')
print(howSum(304, [7,7,7]))

def bestSum(targetSum, numbers, memo = {}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortestCombination = None
    for i in numbers:
        remainder = targetSum - i
        remainderCombination = bestSum(remainder, numbers, memo)
        if remainderCombination != None:
            combination = remainderCombination + [i]
            if shortestCombination == None or len(combination) < len(shortestCombination):
                shortestCombination = combination
    memo[targetSum] = shortestCombination
    return shortestCombination


print('\n' +  'besttSum Function:')
print(bestSum(50,[2,3,6]))

def canConstruct(target, wordBank, memo = {}):
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank, memo) == True:
                memo[target] = True
                return True
    memo[target] = False
    return False


print('\n' + 'canConstruct: ')
print(canConstruct('abstractttttttttttt', ['abs', 'str', 'ct', 'tr', 'a', 't','tttt']))

def countConstruct(target, wordBank, memo = {}):
    if target in memo:
        return memo
    if target == '':
        return 1
    count = 0
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            numWaysForRest = countConstruct(suffix, wordBank, memo) == 1
            count += numWaysForRest
    memo[target] = count
    return count

print('\n' + 'countConstruct: ')
print(countConstruct('abcdef', ['abc','def','abd','cdef']))

def allConstruct(target, wordBank):
    if target == '':
       return [[]]
    count = []
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            string = allConstruct(suffix, wordBank)
            for i in string:
                i.insert(0,word)
            count.append(string)
    return count

print("allConstruct: ")
print(allConstruct('abstractttttttttttt', ['abs', 'str', 'ct', 'tr', 'a', 't','c']))
print(allConstruct('abcdefg', ['abc','defg','ab','cdefg']))
print(allConstruct('123456789', ['1234','56789','12','3456789']))

