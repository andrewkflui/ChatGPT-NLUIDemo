#
# Copyright (C) 2023 - Andrew Kwok-Fai Lui

# This program is free software; you can redistribute it and/or modify it under the terms 
# of the GNU General Public License version 2 as published by the Free Software Foundation.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
# See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this 
# program; if not, see http://www.gnu.org/licenses/.

import openai

with open('OPENAI_KEY','r') as f:
    OPENAI_KEY = f.read()

openai.api_key = OPENAI_KEY

content = 'write a 200-word essay on climate change'
content = 'set the year range from 2010 to 2016'
messages = [{'role': 'system', 'content': content}]
chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
print(chat.choices[0].message.content)