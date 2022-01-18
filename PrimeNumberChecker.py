def prime(number):
    is_prime= True
    for i in range (2, num):
       if num % i ==0:
         is_prime= False
    if is_prime:
       print("Its a prime number")
    else:
       print("Its not a prime number")
num = int(input("Check the number:"))
prime(number = num)


