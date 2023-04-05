import openai

openai.api_key_path = ".env"
model_engine = "gpt-3.5-turbo-0301"


def chat_query(prompt):
    completions = openai.ChatCompletion.create(
        model=model_engine,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50,
        n=1,
        temperature=0.5,
    )

    message = completions.choices[0].message.content
    return message

def conversaton_handler(prompt):
    response = chat_query(prompt)
    return response
