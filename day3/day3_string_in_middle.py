str1 = input("enter the string::")
x = input("new string you want to insert in middle::")
str2 = len(str1)//2
for i in range(1,(len(str1)//2)+1):
    if i == str2:
       a = str1[:str2]   
       b = str1[str2:]
       print(a + x + b)