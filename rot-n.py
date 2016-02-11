# Rot13 Encryption Test
def rotX(inputString,x):
    if x > 26:
        print("Please use numbers between 1-26.")
        exit()
    else:
        pass

    encryptedString = ""
    inputStringList = list(inputString.lower())
    for letter in inputStringList:
        letterNumber = ord(letter) - 96
        if ord(letter) - 96 == -64:
            # print(" ")
            encryptedString += " "
        else:
            if letterNumber + x > 26:
                # print(letter + str((letterNumber + x) - 26))
                encryptedString += str((chr((letterNumber + x) - 26 + 96)))
            else:
                # print(letter + str(letterNumber + x))
                encryptedString += str((chr(letterNumber + x + 96)))

    # print(inputStringList)
    return encryptedString

def decrypt(encryptedString):
    for x in xrange(0,26):
        decryptedString = ""
        encryptedStringList = list(encryptedString.lower())

        for letter in encryptedStringList:
            letterNumber = ord(letter) - 96
            if letterNumber == -64:
                decryptedString += " "
            else:
                if letterNumber - x < 1:
                    string = (letterNumber - x) + 26 + 96
                    # print(string, chr(string))
                    decryptedString += chr(string)
                else:
                    string = letterNumber - x + 96
                    # print(string, chr(string))
                    decryptedString += chr(string)
        if x < 10:
            print("0" + str(x) + ": " + decryptedString)
        else:
            print(str(x) + ": " + decryptedString)

menuChoice = int(raw_input("Options:\n1. Encrypt\n2. Decrypt\n> "))
print("\n----\n")
if menuChoice == 1:
    inputString = raw_input("Enter your message\n> ")
    print("\n----\n")
    rotationValue = int(raw_input("How many rotations?\n> "))
    print("\n----\n")
    print(rotX(inputString,rotationValue))

if menuChoice == 2:
    inputString = raw_input("Enter the encrypted message\n> ")
    decrypt(inputString)
