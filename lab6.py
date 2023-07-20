# Bryce Ramos
def passwordEncoder(password):
    encodedPassword = None
    digitList = []
    for digit in password: # translates each digit of the password
        newDigit = ((int(digit) + 3)% 10)
        digitList.append(str(newDigit))
    encodedPassword = "".join(digitList) # recombines the new digits into a new password
    return encodedPassword

def decode(password):
    decodedPassword = None
    digitList =[]
    for digit in password:
        newDigit = ((int(digit) - 3) % 10)  # Making sure to not go below 0
        digitList.append(str(newDigit))
    decodedPassword = "".join(digitList)
    return decodedPassword


def main():
    programRun = True
    password = None
    encodedPassword = None
    while programRun:
         print("Menu")
         print("-------------")
         print("1. Encode")
         print("2. Decode")
         print("3. Quit")
         menuInput = int(input("Please enter an option: "))
         if menuInput == 1: # encoding passwords
                if password is None:
                    password = str(input("Please enter your password to encode: "))
                    encodedPassword = passwordEncoder(password)
                    print("Your password has been encoded and stored!")
                else:
                    # insert decoder code here
                    print(f"The original password is {password}, and the encoded password is {encodedPassword}")  # why decode a password if you already know the original
         elif menuInput == 2: # decoding passwords
            if password is not None:
                print(f"The encoded password is {encodedPassword}, and the original password is {password}.") # why decode a password if you already know the original
            else: # Decoded code
                encodedPassword = str(input("Please enter your encoded password to decode: "))
                password = decode(encodedPassword)
                print("Your password has been encoded and stored!")
         elif menuInput == 2: # decoding passwords
            if password is not None:
                print(f"The encoded password is {encodedPassword}, and the original password is {password}.") # why decode a password if you already know the original
            else:
                # enter decoded code here
                pass
         elif menuInput == 3: # exiting code
            break
         else: # someone didn't read the menu options
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()