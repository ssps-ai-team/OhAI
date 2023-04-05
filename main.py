#!/usr/bin/env python3

from chat import conversaton_handler
from ohbot import *

lang = "en"

prompt = input("User: ")
answer = conversaton_handler(prompt)
print(answer)
say(answer, lang, soundDelay=0.1)
