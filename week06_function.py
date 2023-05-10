# week06_function.py
#after decorator
import time

#decorator
def time_checker(func): #closure
    def inner(*args):
        s = time.time()
        r = func(*args)
        e = time.time()
        print(f"총 수행시간은 {e - s}초 입니다.")
        return r
    return inner

def factorial_repetition(n):
    """
    factorial function
    :param n: > 0
    :return: n!
    """
    result=1
    for k in range(1,n+1):
        result=result*k
    return result


def factorial_recursion(n):
    """
    factorial function with recursion
    :param n: > 0
    :return: n!
    """
    if n==1:
        return 1
    else:
        return n*factorial_recursion(n-1)

def fibonacci_recursion(n):
    """
    fibonacci number recursion
    :param n: integer value
    :return: fibonacci number
    """
    if n<=1:
        return n
    else:
        return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)
def fibonacci_repetition(n):
    a=[0,1]
    for i in range(2,n+1):
        a.append(a[i-1]+a[i-2])
    return a[n]

if __name__=="__main__":
    number=int(input("정수 입력: "))
    print(factorial_repetition(number))
    print(factorial_recursion(number))
    print(fibonacci_repetition(number))
    print(fibonacci_recursion(number))


