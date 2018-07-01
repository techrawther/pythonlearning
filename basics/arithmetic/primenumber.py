#Prime Number is a number that is divisible only by itself
prime_numbers=[]
maxlimit = 100

print("Simple Way of Doing")
for each_number in range(2,maxlimit+1):
    is_prime = True
    for divisor in range(2,each_number):
        if each_number % divisor == 0:
            is_prime = False
            break
    if (is_prime):
        prime_numbers.append(each_number)
print(prime_numbers)
#TODO:1
#Pythonic way of doing
#Following doesnt work
print("Trying Pythonic way")
for each_number in range(2,maxlimit+1):
    is_prime = True
    for divisor in range(2,each_number):
        if each_number % divisor == 0:
            is_prime = False
            break
        
    prime_numers.append(each_number) if (is_prime) else continue

print(prime_numbers)
                         
                         
    
    
