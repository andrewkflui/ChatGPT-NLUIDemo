import openai

with open('OPENAI_KEY','r') as f:
    OPENAI_KEY = f.read()

openai.api_key = OPENAI_KEY

content = 'write a 200-word essay on climate change'
content = 'set the year range from 2010 to 2016'
messages = [{'role': 'system', 'content': content}]
chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
print(chat.choices[0].message.content)