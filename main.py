#!/usr/bin/env python3

from chat import conversaton_handler # Import the function that talks with gpt-3.5-turbo
from ohbot import * # Import the modified ohbot library
from recognize import recognize
import sys

def main():
    lang = sys.argv[-1] # Get the language
    try:
        prompt = recognize()
        answer = conversaton_handler(prompt) # Generate the response from the user
        print(answer) # Print the answer for debuging lol
        say(answer, lang) # Make the ohbot talk
    except:
        say("Can you repeat that?", lang)

if __name__ == "__main__":
    main()