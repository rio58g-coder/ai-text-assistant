from openai import OpenAI
import config

client = OpenAI(api_key=config.API_KEY)


def summarize_text(text):
    response = client.chat.completions.create(
        model=config.MODEL,
        messages=[
            {"role": "system", "content": "Ты помощник, который делает краткое резюме текста."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content


def rewrite_text(text):
    response = client.chat.completions.create(
        model=config.MODEL,
        messages=[
            {"role": "system", "content": "Перепиши текст красиво и грамотно."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content


def chat_response(text):
    response = client.chat.completions.create(
        model=config.MODEL,
        messages=[
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content