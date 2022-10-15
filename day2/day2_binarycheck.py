num = input("enter the number::")
flag = 0
for i in num:
    if i == "0" or i == "1":
            continue
    else:
            flag += 1
            break
if flag == 1:
       print('not')
else:
        print('binary')