def check(n):
    if n ==2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

number = int(input("enter a number"))
if number <2:
    print("soory prime number not defined for this range")
for i in range(2,number+1):
    if check(i):
        print(f"prime number: {i}")
        