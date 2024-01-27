import random
import hangman_art
import hangman_word

chosen_word = random.choice(hangman_word.word_list)
#Testing code
print(f"Pssst, the solution is {chosen_word}")
lives = 6
display = []
print(hangman_art.logo)
for i in range(len(chosen_word)):
    display.append("_")

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(0,len(chosen_word)):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in a word you lose a life! ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Game Over")  
            print(f"The word was {chosen_word}")
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You won")
    
    print(hangman_art.stages[lives])