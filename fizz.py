for i in range(1,100):
    if i % 3 == 0:
        if i % 5 == 0:
            print("FixxBuzz")
        else:
            print("Fizz")
    elif i % 5 == 0:
        if i % 3 == 0:
            print("FizzBuzz")
        else:
            print("Buzz")
    elif i % 3 == 0 and i % 5 ==0:
        print("FizzBuzz")
    else:
        print(i)
