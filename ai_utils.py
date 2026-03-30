# ai_utils.py
# Функции для работы с ИИ

from openai import OpenAI
import config

client = OpenAI(api_key=config.API_KEY)


def summarize_text(text):
    """Создает краткое резюме текста"""
    response = client.chat.completions.create(
        model=config.MODEL,
        messages=[
            {"role": "system", "content": "Ты помощник, который делает краткое резюме текста."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content


def rewrite_text(text):
    """Переписывает текст красиво и грамотно"""
    response = client.chat.completions.create(
        model=config.MODEL,
        messages=[
            {"role": "system", "content": "Перепиши текст красиво и грамотно."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content


def chat_response(text):
    """Простая беседа с ИИ"""
    response = client.chat.completions.create(
        model=config.MODEL,
        messages=[
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content