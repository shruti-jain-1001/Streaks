def fibonacci():
    a = 0
    b = 1
    counter = 0
    nth = int(input("enter the nth term::"))
    print(a)
    print(b)
    while(counter<nth):
        c = a + b
        print(c)
        a = b
        b = c
        counter += 1   
fibonacci()
