import random
import hangman_words
import hangman_art

print(hangman_art.logo)
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
lives = 6
placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}!")
        continue

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"****************************\n"
              f"'{guess}' is not in the word")
        lives -= 1

        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************\n"
                  f"The word was: {chosen_word}\n")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
