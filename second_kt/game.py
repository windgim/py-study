import random


words_file = "words.txt"
pictures_path = "hangman/"
max_errors = 7


def load_words():
    with open(words_file, "r", encoding="utf-8") as file:
        words = file.readlines()

    return [word.strip().lower() for word in words if word.strip()]


def choose_word(words):
    return random.choice(words)


def create_hidden_word(word):
    return ["_" for _ in word]


def show_word(hidden_word):
    print(" ".join(hidden_word))


def show_hangman(errors):
    filename = pictures_path + str(errors) + ".txt"

    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())


def get_letter():
    while True:
        letter = input("Введите букву: ").strip().lower()

        if len(letter) == 1 and letter.isalpha():
            return letter

        print("Введите одну букву.")


def update_word(word, hidden_word, letter):
    found = False

    for index in range(len(word)):
        if word[index] == letter:
            hidden_word[index] = letter
            found = True

    return found


def word_guessed(hidden_word):
    return "_" not in hidden_word


def start():
    words = load_words()
    word = choose_word(words)
    hidden_word = create_hidden_word(word)
    errors = 0
    used_letters = []

    print("Игра «Виселица»!")
    print()

    while errors < max_errors and not word_guessed(hidden_word):
        show_word(hidden_word)

        print("Использованные буквы:", " ".join(used_letters))

        letter = get_letter()

        if letter in used_letters:
            print("Эта буква уже использовалась.")
            continue

        used_letters.append(letter)

        if update_word(word, hidden_word, letter):
            print("Верно!")
        else:
            errors += 1
            print("Неверно!")
            show_hangman(errors)

        print()

    show_word(hidden_word)

    if word_guessed(hidden_word):
        print("Поздравляем! Вы угадали слово:", word)
    else:
        print("Вы проиграли!")
        print("Загаданное слово:", word)
