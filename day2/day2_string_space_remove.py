def string_space():
    
    str1 = input("enter the string::")
    list1 = []
    for i in str1:
        if i == " ":
            continue
        else:
           list1.append(i)
    str2 = ''.join(list1)
    return str2
str3 = string_space()
print(str3)