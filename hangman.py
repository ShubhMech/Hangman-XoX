# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 19:35:51 2021

@author: Asus
"""

from words import words
from game_visuals import lives_visual_dict
import random

word = random.choice(words)
if "-" in word or " " in word:
    word = random.choice(words)

print(word)
lives = len(word)
print(f'You have {lives} to begin with.')

letters = set(word)
used_letters = set()
guessed_letters = set()

list1 = []
# print(initial)
for i in range(0, len(word)):
    list1.append("_")

check1 = str(list1).count('_') > 0
check2 = lives >= 0

while check1 and check2:

    word_construt = ''
    for i in list1:
        word_construt += i

    if word_construt == word:
        print(f"You guessed the word '{word}' right, with {lives} lives remaining!!")
        break
    elif lives == 0:
        print("You have run out of lives!!")
        break

    print(list1)
    print("The set of used letters is:", used_letters)
    print("Remaining lives are: ", lives)

    print("The set of correctly guessed letters that you have used so far are:", guessed_letters)

    guessed_letter = input("Guess a letter other than the ones that you have already guessed").lower()
    if guessed_letter in word:
        guessed_letters.add(guessed_letter)
    else:
        lives = lives - 1
        # print(lives_visual_dict[-lives])
    used_letters.add(guessed_letter)
    list2 = []
    [list2.append(guessed_letter) if guessed_letter == letter else list2.append("_") for letter in word]
    # print(list2)

    for j, i in enumerate(list2):
        if i != "_":
            # indice=list2.index(i)
            # print(j)
            list1[j] = i

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")