
str1 = input("enter the string::")
vowels = "aeiou"
numbers = '0123456789'
count = 0
num ,spec , cons = 0,0,0
for i in str1:
    if i in vowels:
        count += 1
    elif i in numbers:
        num += 1
    elif (ord(i)>=33 and ord(i)<=47) or (ord(i)>=58 and ord(i)<=64) or (ord(i)>=91 and ord(i)<=96) or (ord(i)>=123 and ord(i)<=126):
        spec += 1
    else:
        cons += 1
print('str1 have {} vowels ,{} numbers,{} special chr and {} constants'.format(count,num,spec,cons))