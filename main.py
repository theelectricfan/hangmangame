import random
import os
import ascii_arts
import words

word = words.word_list[random.randint(0, len(words.word_list) - 1)]

live = 6

display = []
guessed = []
for ltr in word:
    display.append("_")

print(ascii_arts.logo)

while "_" in display and live > 0:
    flag = False
    print(ascii_arts.stages[live])
    print(' '.join(display))

    letter = input("Guess a letter: ").lower()
    os.system('cls')
    if letter in guessed:
        print("You have already guessed this letter.")
        continue

    for ltr in range(0, len(display)):
        if word[ltr] == letter:
            display[ltr] = letter
            flag = True

    if not flag:
        live -= 1
        print(f"The letter {letter} is not a part of the word. You lose a life.")
    guessed.append(letter)

if live == 0:
    print(ascii_arts.stages[0])
    print("Game over! You lose.")
elif "_" not in display:
    print("Game over! You win.")
else:
    print("Woah! Are you a hacker dude.")
