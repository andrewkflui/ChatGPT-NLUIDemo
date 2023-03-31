# A Demo Natural Language User Interface based on a Prompt-Engineered ChatGPT model
 
This repository contains the demo program described in the following Medium article

* [Prompt Engineering in ChatGPT: Prompt Engineering in ChatGPT: adding natural language user input to a GUI easily](https://medium.com/@andrewlui_60044/prompt-engineering-in-chatgpt-building-a-natural-language-user-interface-made-easy-819b80cc98a3)

### Requirments
Tested with these versions but older versions may work.
- Python 3.11
- OpenAI 0.27.2

```
pip install openai
```

### Key Files
- `chatgpt_nlui_demo.py`: The demo application.
- `openai_api.py`: A simple test program for the OpenAI API.
- `OPENAI_KEY`: Store the private OpenAI API key.
- `CHATGPT_SYS_PROMPT_`, `CHATGPT_SYS_PROMPT_2`, `CHATGPT_SYS_PROMPT_3`: Examples of the in-context prompt explained in the article. To try a different prompt, modify the demo application. 
- `EXAMPLE_USER_COMMAND`: Some example user commands for testing.

### The OpenAI API Key

Obtain a new private key from the [OpenAI API Key Page](https://platform.openai.com/account/api-keys). Save the key to the file `OPENAI_KEY`.

Register a new account if you have not got one. 

### Execute the application

```
python chatgpt_nlui_demo.py
```

![image](https://user-images.githubusercontent.com/8808539/229014866-94b0ac1a-7406-41ad-adea-3e8d5eb13c19.png)


### Licences

Copyright (C) 2023 - Andrew Kwok-Fai Lui

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 2 as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, see http://www.gnu.org/licenses/.

 
