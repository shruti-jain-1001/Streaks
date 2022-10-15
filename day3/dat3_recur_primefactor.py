def primeFactors(num):
    for i in range(2,num+1):
        if num%i == 0:
            list1.append(i)
            num = num // i
            break
    if num > 1:
            primeFactors(num)
            
    return list1
    
    
list1 =[]
num = int(input("enter your number ::> "))
listfinal = primeFactors(num)
print(listfinal)