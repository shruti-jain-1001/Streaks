a = int(input('enter the number:'))
list1 = []
sum = 0
for i in range(2,a+1):
    if a%i == 0:
        counter = 1
        for j in range(2,int(i//2)+1):
            if i%j == 0:
                counter = 0
        if counter == 1:
              list1.append(i)  
              sum += 1
print(list1)
print('{} have {} factors'.format(a,sum)) 
