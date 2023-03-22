#week03_prime_number v0.9
is_prime=True
start_number,end_number=map(int,input("Enter starting number and ending number : ").split())
for i in range(start_number, end_number+1):
    for j in range(2,i):
        if i%j==0:
            is_prime=False
    if is_prime and i!=1:
        print(f"{i} ")
    is_prime=True

