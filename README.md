# ChatGPT-NLUIDemo

# A Demo Natural Language User Interface based on a Prompt-Engineered ChatGPT model
 
This repository contains the demo program described in the following Medium article

* [Prompt Engineering in ChatGPT: building a Natural Language User Interface made easy](https://medium.com/@andrewlui_60044/deploy-a-python-application-on-a-aws-ci-cd-pipeline-part-1-code-repository-1090ff888eaa)

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

### Licences

Copyright (C) 2023 - Andrew Kwok-Fai Lui

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 2 as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, see http://www.gnu.org/licenses/.

 
