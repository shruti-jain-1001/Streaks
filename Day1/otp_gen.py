import random

b = ""
def otpgen():
    global b
    for i in range(0,6):
      b = b + str(random.randint(0, 9))
    return b
o = otpgen()
print("otp  is ",o)