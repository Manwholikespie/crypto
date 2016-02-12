# Rot13 Encryption Test

# for finding the correct decryption scenario
from enchant.checker import SpellChecker
import pandas as pd

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
    stringList = []
    errorsList = []
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
        stringList.append(decryptedString)
        errorsList.append(testAccuracy(decryptedString))
        if x < 10:
            print("0" + str(x) + ": " + decryptedString)
        else:
            print(str(x) + ": " + decryptedString)
        # if testAccuracy(decryptedString) == 0:
        #     print("Decrypted!")
        #     break
    stringSeries = pd.Series(stringList)
    errorsSeries = pd.Series(errorsList)
    d = {
        'message' : stringSeries,
        'errors' : errorsSeries
    }
    df = pd.DataFrame(d)
    df = df.sort_values(by='errors', ascending=True)
    df = df[:5]
    print("\nTop 5 Possibilities:")
    print(df)

def testAccuracy(inputString):
    errors = 0
    chkr = SpellChecker("en_US")
    chkr.set_text(inputString)
    for err in chkr:
        errors += 1
    return errors

###########################   MAIN FUNCTION  ###################################
menuChoice = int(raw_input("Options:\n1. Encrypt\n2. Decrypt\n> "))
print("\n----\n")
if menuChoice == 1:
    inputString = raw_input("Enter your message\n> ")
    print("\n----\n")
    rotationValue = int(raw_input("How many rotations?\n> "))
    print("\n----\n")
    print(rotX(inputString,rotationValue))

if menuChoice == 2:
    # setting up pyEnchant for finding the correct rotation sequence
    inputString = raw_input("Enter the encrypted message\n> ")
    print("\nDecrypting...\n")
    decrypt(inputString)
##########################  END MAIN FUNCTION  #################################
