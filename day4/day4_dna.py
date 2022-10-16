a = input("enter the character::").upper()
rnaString =""
for i in a:
    if i == 'G':
        rnaString += "C"
    elif i == "C":
        rnaString += "G"
    elif i =="T":
        rnaString += "A"
    elif i == "A":
        rnaString += "U"
    else:
        break

print(rnaString)