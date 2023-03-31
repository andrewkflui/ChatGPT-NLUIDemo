import openai
####################
# Setup the OpenAI API for ChatGPT

with open('OPENAI_KEY','r') as f:
    OPENAI_KEY = f.read()

openai.api_key = OPENAI_KEY

with open('CHATGPT_SYS_PROMPT_2','r') as f:
    content = f.read()
    SYSTEM_PROMPT = {'role': 'system', 'content': content}

def call_chatgpt(input):
    messages = [SYSTEM_PROMPT]
    input = f'My command is “{input}".'
    messages.append({"role": "user", "content": input})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    return reply

####################
# Building the GUI using Tkinter
import tkinter as tk
from tkinter import *
  
root = Tk()
root.title('Road Crash Visualization')
root.geometry('400x300')

def update_dropdown(tkvar, value):
    if 'nil' in value:
        error_label.config(text=f'Not sure about the year')
        return False        
    elif 'error' in value:
        error_label.config(text=f'The year is out of the valid range')
        return False
    tkvar.set(value)
    return True

def update_checkbox(tkcomp, value):
    if 'unchecked' in value:
        tkcomp.deselect()
    elif 'checked' in value:
        tkcomp.select()
    else:
        return False
    return True

def update_gui(reply):
    lines = reply.splitlines() 
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue
        strlist = line.split(':')
        if len(strlist) != 2:
            continue
        name, value = strlist[0].strip().lower(), strlist[1].strip().lower()
        #print(f'name = {name}, value = {value}')
        if 'start year' in name:
            #print(f'start year = "{value}"')
            update_dropdown(start_year_clicked, value)
        elif 'end year' in name:
            update_dropdown(end_year_clicked, value)
            #print(f'end year = "{value}"')
        else:
            for i in range(len(CRASH_TYPE)):
                if CRASH_TYPE[i].lower() in name:
                    update_checkbox(crash_type_checkboxes[i], value)
                    break

def submit_press_event():
    content = textbox.get('1.0', END)
    reply = call_chatgpt(content)
    print(f'CHATGPT:\n{reply}')
    update_gui(reply)
  
# Create the GUI components
# The dropdown for the start year and the end year
year_list = [str(x) for x in range(2000, 2024)]
start_year_clicked = StringVar()
start_year_clicked.set(year_list[0])
start_year_option = OptionMenu(root, start_year_clicked, *year_list)
start_year_option.pack()

end_year_list = [str(x) for x in range(2000, 2023)]
end_year_clicked = StringVar()
end_year_clicked.set(end_year_list[-1])
end_year_option = OptionMenu(root, end_year_clicked, *year_list)
end_year_option.pack()

# The checkboxes for the crash types
CRASH_TYPE = ['Multi', 'Single', 'Pedestrian', 'Other']
crash_type_clicked = [tk.IntVar() for i in range(len(CRASH_TYPE))]
crash_type_checkboxes = []
for i in range(len(CRASH_TYPE)):
    crash_type_checkboxes.append(
        tk.Checkbutton(root, text=CRASH_TYPE[i], variable=crash_type_clicked[i], 
                       onvalue=1, offvalue=0,))
    crash_type_checkboxes[-1].pack()

textbox_str = StringVar()
textbox = Text(root, height=6, width=40)
textbox.pack()
button = Button(root, text='Submit', command=submit_press_event).pack()
error_label = Label(root, text='')
error_label.pack()
# Start the GUI loop
root.mainloop()
