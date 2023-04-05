import openai, os;

openai.api_key_path = ".env"
model_engine = "gpt-3.5-turbo-0301"


def chat_query(prompt):
    completions = openai.ChatCompletion.create(
        model=model_engine,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2048,
        n=1,
        temperature=0.5,
    )

    message = completions.choices[0].message.content
    return message

def conversaton_handler(prompt):
    response = chat_query(prompt)
    return response


from ohbot import *

lang = input("What language do you want to use: ")

while True:
    prompt = input("User: ")
    answer = conversaton_handler(prompt)
    print(answer)
    say(answer, lang)
    wait(2)
