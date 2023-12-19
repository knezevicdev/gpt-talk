import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']


def pitaj_gpt(message, chat_log=None):
    odgovor = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        messages=chat_log or [{"role": "user", "content": message}]
    )

    return odgovor.choices[0].message.content
