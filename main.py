import PySimpleGUI as sg

# Get text corpus from language dicts file
from language_dicts import lang_dict_en, lang_dict_zh_cn, lang_dict_fr, lang_dict_es
lang_dicts = {"en": lang_dict_en, "zh_cn": lang_dict_zh_cn, "fr": lang_dict_fr, "es":lang_dict_es}

# Choose a default language
selected_language = lang_dicts["en"] # language mapping (default to 'en')

# Define and create language selection window
lang_selection_layout = [
    [sg.Text('Select your language')],
    [sg.Radio('English', 'LANG', key='en', default=True)],
    [sg.Radio('简体中文', 'LANG', key='zh_cn')],
    [sg.Radio('Français', 'LANG', key='fr')],
    [sg.Radio('Español', 'LANG', key='es')],
    [sg.Button('Next', size=(10, 1))]
]

lang_selection_window = sg.Window('Select Your Language', lang_selection_layout)  

# Switch language using user's input
event, values = lang_selection_window.read()
for language, selected in values.items():
    # Lets us get selected language
    if selected:
        # Corresponds to language_dicts dictionary at top to store selected language
        selected_language = lang_dicts[language]
lang_selection_window.close()

# Define and create main window
# note: using l[key_name] for all i18n string
layout = [[sg.Text(selected_language["ask_name"])],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button(selected_language["ok"]), sg.Button(selected_language["quit"])]]

window = sg.Window(selected_language["title"], layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == selected_language["quit"]:
        break
    window['-OUTPUT-'].update(selected_language["hello"] + ' ' + values['-INPUT-'] + selected_language["thanks"])

window.close()
