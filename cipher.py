alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
    ]   
greet = "WELCOME TO THE PROGRAM: CAESAR CIPHER"
section = "-" * 60
new_section = "=" * 60
choose = True

print("")
print(section)
print(greet)
print(section,"\n")

while choose:
    choose_of_operation = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    if choose_of_operation == "encode" or choose_of_operation == "decode":
        print(section)
        
        if choose_of_operation == "encode":
            word = input("Type your messange: \n").lower()
            if not word.isalpha():
                print("Your input did not contain alphabetic characters, try again..")

            try:
                 shift_number = int(input("\nType the shift number: \n"))
            except:
                print("Your input did not contain alphanumeric characters, try again..")
            
            letters_list = []
            for letter_index in range(0, len(word)):
                chracter = word[letter_index]
                character_index = alphabet.index(chracter)
                result = alphabet[(character_index + shift_number) % len(alphabet)] 
                letters_list.append(result)
            print(new_section)
            print("Encoded message:", "".join(letters_list))
            print(new_section,"\n")
            
            again = input("Type 'yes' if you want to go again, or another sign for 'no':\n").lower()
            if again == "yes":
                    choose
                    print()
            elif again != "yes":
                print("The program turns off.")
                print(section)
                quit()    
            
        elif choose_of_operation == "decode":
            word = input("Type your messange: \n").lower()
            if not word.isalpha():
                print("Your input did not contain alphabetic characters, try again..")

            try:
                shift_number = int(input("\nType the shift number: \n"))
            except:
                print("Your input did not contain alphanumeric characters, try again..")

            letters_list2 = []
            for letter_index2 in range(0, len(word)):
                chracter = word[letter_index2]
                character_index2 = alphabet.index(chracter)
                result = alphabet[(character_index2 - shift_number) % len(alphabet)] 
                letters_list2.append(result)
            print(new_section)
            print("Decoded message:", "".join(letters_list2))
            print(new_section,"\n")

            again = input("Type 'yes' if you want to go again, or another sign for 'no':\n").lower()
            if again == "yes":
                    choose
                    print()
            elif again != "yes":
                print("The program turns off.")
                print(section)
                quit()    

    else:
        print("Invalid input, try again..")
        print(section)
        




