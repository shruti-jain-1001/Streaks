a = int(input('enter the number:'))
list1 = []
for i in range(2,a+1):
    if a%i == 0:
        counter = 1
        for j in range(2,int(i//2)+1):
            if i%j == 0:
                counter = 0
        if counter == 1:
              list1.append(i)  

newstr = ""
for i in list1:
    if i == 3:
       newstr += 'pling'
    elif i == 5:
       newstr += 'plang'
    elif i == 7:
         newstr += 'plong'
    else:
          print(a)
print(newstr)