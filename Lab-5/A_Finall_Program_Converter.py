from Pvitanya import greet_user
from number_to_word import convert_number_to_word

def main():
    greet_user()
    number = int(input("Будь ласка введіть число, яке вам потрібно перетворити в текст: "))
    word = convert_number_to_word(number)
    print(f"Текст числа {number} є {word}.")
