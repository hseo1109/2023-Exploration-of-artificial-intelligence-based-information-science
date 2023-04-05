# week04_prime_number v1.0
# add function
def is_prime(k) -> bool:
    """
    소수 판정
    :param n: Integer number
    :return: True (if number is prime number) / False (if number is NOT prime number)
    """
    if k<2:
        return False
    else:
        for i in range(2,k):
            if k%i==0:
                return False
    return True

start_number,end_number=map(int,input("Enter starting number and ending number : ").split())
if start_number>end_number
    start_number,end_number=end_number,start_number
for i in range(start_number, end_number+1):
    if is_prime(i):
        print(i,end=' ')