
p1 = int(input("how much ques p1 has to do:: "))
p2 = int(input("how much ques p2 has to do:: "))

if p1> p2:
    more = p1
else:
    more = p2
ques = int(input("how much ques has to do more:: "))   
days = int(input("In how many days has to do yhese ques:: ")) 

def questions():
    one_did = more*days
    bypass = one_did + ques
    ans = bypass/days
    print("one has to do minimum in a day",ans)
questions()