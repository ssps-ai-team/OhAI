from chat import conversaton_handler
from ohbot import *

lang = input("What language do you want to use: ")

while True:
    prompt = input("User: ")
    answer = conversaton_handler(prompt)
    print(answer)
    say(answer, lang)
    wait(2)
