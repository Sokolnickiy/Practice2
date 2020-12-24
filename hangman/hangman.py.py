from string import ascii_lowercase
import random


def main():
    with open('words.txt') as file:
        words = file.readline().split()
        print(f'Found {len(words)} words in input file')

    word_to_guess = random.choice(words)

    attempt_number = 0
    max_attempts = 20

    all_letters = set(ascii_lowercase)
    used_letters = set()

    for attempt in range(max_attempts):
        possible_letters = all_letters - used_letters

        print(f'Possible letters are:\r\n {" - ".join(possible_letters)}')

        chosen_letter = input(f'You have {max_attempts - attempt_number} attempts left. Please choose one of possible '
                              f'letters\r\n')

        if chosen_letter not in possible_letters:
            print(f'Wrong input, please use only letters from possible letters listed above\r\n')
            continue

        if chosen_letter in word_to_guess:
            print(f'Great job! OTKROITE BUKVU {chosen_letter}\r\n')
            used_letters.add(chosen_letter)

        if chosen_letter not in word_to_guess:
            print(f'Unfortunately letter {chosen_letter} is not present in a secret word')
            used_letters.add(chosen_letter)

        opened_letters_contatenated = "".join([letter for letter in word_to_guess if letter in used_letters])
        print(f'Here is the word after {attempt} attempt: {opened_letters_contatenated}')

        if opened_letters_contatenated == word_to_guess:
            print(f'VI VIIGRALI AAVTOMOBIL@!!!\r\nYour word was: {word_to_guess}')
            break


if __name__ == '__main__':
    main()