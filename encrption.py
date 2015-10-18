import random
splitArray = []

def takeInput():

    rawText = raw_input("Type something to be encrypted: \n")
    password = raw_input("Please type a numerical password: \n")
    encrypt(rawText, int(password))

def encrypt(rawText, password):
    for c in rawText:
        divide(c, password)


def divide(charToDivide, password):
    asciiValue = ord(charToDivide)
    a = 0
    b = 0
    c = 0
    passa = 0
    passb = 0
    passc = 0
    a = random.randrange(a, asciiValue)
    b = random.randrange(b, asciiValue - a)
    c = asciiValue - (a+b)
    passa = random.randrange(passa, password)
    passb = random.randrange(passb, password-passa)
    passc = password - (passa+passb)
    if isinstance(password, str):   
        print "Please enter a number"
        takeInput()
    else:
        a += passa  
        b += passb
        c += passc      
    splitArray.append(str(a))
    splitArray.append(str(b))
    splitArray.append(str(c))

takeInput()
f = open("myEncryptorTest", 'w')
arrayDelimiterString = "."
encryptedString = arrayDelimiterString.join(splitArray)
encryptedString = "." + encryptedString
f.write(encryptedString)
f.close
