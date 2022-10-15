a = int(input('enter the first number:'))
b = int(input('enter the first number:'))
lcm = 1 

for i in range(1, a if (a>b) else b):
    if a%i == 0 and b%i == 0:
        lcm = lcm * i
        
print(lcm)      
     