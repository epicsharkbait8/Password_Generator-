import random
import string
import requests

def random_character():
    choices = string.ascii_letters + string.digits + string.punctuation
    return random.choice(choices)

passwordLength = 12


def generate_strong_password():
    password = ""
    for i in range(passwordLength):
        password = password + random_character()
    print(password)

generate_strong_password()

def fetch_word():
    url = "https://random-word-api.herokuapp.com/word?length=6"

    response = requests.get(url)
    word = response.json()[0]
    return word
#print(fetch_word())

def replaceLetters(word):
    word = word[0].upper() + word[1:]
    if "a" in word:
        word = word.replace("a", "@")
    if "i" in word:
        word = word.replace("i", "!")
    if "c" in word:
        word = word.replace("c", "(")
    if "o" in word:
        word = word.replace("o", "0")
    return word

def generate_weaker_password():
    word1 = fetch_word()
    word2 = fetch_word()
    word1 = replaceLetters(word1)
    word2 = replaceLetters(word2)
    password = word1 + word2
    return password

print(generate_weaker_password())