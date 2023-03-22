#week03_prime_number v0.6
number=int(input("Input number : "))
#count=0
is_prime=True
if number<2:
    is_prime=False
else:
    for i in range(2,number):
        if number%i==0:
            #count=count+1
            is_prime=False
            break #If not prime number, exit the loop as soon as the first divisor is found
if is_prime: #remove comparison
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number.')