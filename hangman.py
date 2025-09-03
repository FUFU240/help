# import random

# print("Welcome to the hangman game")
# words = ['Poop', 'Girl', 'Manny']

# while True:
#     hang = input("Do you want to play Y/N: ").lower()
    
#     if hang == "y":
#         LIVES = 3
#         if not words:
#             print("You've already played all the words! Goodbye!")
#             break
        
#         oya = random.choice(words)
#         secret_word = oya.lower()
#         words.remove(oya)
        
#         display = ["_"] * len(secret_word)
#         print(" ".join(display))
        
#         another_one = set()

#         while True:
#             print(f"You have {LIVES} lives")
            
#             letter = input("Enter a single letter: ").lower().strip()
            
#             if len(letter) != 1 or not letter.isalpha():
#                 print("Please enter only one letter.")
#                 continue

#             if letter in another_one:
#                 print("You already guessed that letter.")
#                 continue
            
#             another_one.add(letter)

#             if letter in secret_word:
#                 print("Good guess")
#                 for index, char in enumerate(secret_word):
#                     if char == letter:
#                         display[index] = letter
                
#                 print(" ".join(display))
                
#                 if "_" not in display:
#                     print("YOU GOT IT\nYOU WON THE HANGMAN GAME🎉")
#                     print(f"You still have {LIVES} lives left")
#                     break
#             else:
#                 print("nahhh bruh")
#                 LIVES -= 1
                
#                 if LIVES == 0:
#                     print("you are dead")
#                     print(f"The word was: {secret_word.capitalize()}")
#                     break
    
#     elif hang == "n":
#         print("Alright maybe next time")
#         break
    
#     else:
#         print("Choose either (y/n)")

         
                    
# words = {'poop':"A TERM FOR FECES",'Girl':"A FEMALE CHILD OR ADOLESCENT",'PLAYLIST':"A LIST OF AUDIO OR VIDEO FILES"}
      

                        
                    # else:
                    #     LIVES -= 1
                    #     print(f"you have {LIVES} lives left")
                    #     if LIVES == 0:
                    #         print("no more lives")
                    #         quit()
                        
        
                    # elif letter == o[1]:
                    #     display [1] = letter

import random

print("Welcome to the hangman game")
words = ['Poop', 'Girl', 'Manny']
correct_word = 0
while True:
    hang = input("Do you want to play Y/N: ").lower()
    
    if hang == "y":
        LIVES = 3
        # This is the code that checks if the list is empty
        if not words:
            print("You've guessed all the words! Goodbye!")
            break
        
        oya = random.choice(words)
        secret_word = oya.lower()
        words.remove(oya)
        
        display = ["_"] * len(secret_word)
        print(" ".join(display))
        
        another_one = set()

        while True:
            print(f"You have {LIVES} lives")
            
            letter = input("Enter a single letter: ").lower().strip()
            
            if len(letter) != 1 or not letter.isalpha():
                print("Please enter only one letter.")
                continue

            if letter in another_one:
                print("You already guessed that letter.")
                continue
            
            another_one.add(letter)

            if letter in secret_word:
                print("Good guess")
                for index, char in enumerate(secret_word):
                    if char == letter:
                        display[index] = letter
                
                print(" ".join(display))
                
                if "_" not in display:
                    print("YOU GOT IT\nYOU WON THE HANGMAN GAME🎉")
                    print(f"You still have {LIVES} lives left")
                    correct_word += 1
                    break
                if correct_word == 3:
                    print("You have completed the game")
            else:
                print("nahhh bruh")
                LIVES -= 1
                
                if LIVES == 0:
                    print("you are dead")
                    print(f"The word was: {secret_word.capitalize()}")
                    break
           
    
    elif hang == "n":
        print("Alright maybe next time")
        break
    
    else:
        print("Choose either (y/n)")
               
                        
            # else:
            #     print("Invalid input. Please enter only ONE alphabet letter.")

        
        
        # if guess == oya:
        #     print("you guessed the word correctly")

        #     if oya in another_one:
        #         print("That word was already choosen\nLet's pick another one")
