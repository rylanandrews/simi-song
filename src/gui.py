# https://docs.pysimplegui.com/en/latest/documentation/what_is_it/fun_as_a_goal/

import PySimpleGUI as sg

unsortedSongs = "multiple\nsongs\nhere"

layout = [  
    [sg.Text(text="Input a song: "), sg.Input(default_text="", key="-INPUT-")],
    [sg.Multiline(default_text=unsortedSongs, size=(30,30)), sg.Button("Hi!", k="-BUTTON1-"), sg.Output(size=(30,30))]
            ]

# Create the Window
window = sg.Window('Simi-song', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == "-BUTTON1-":
        print("something")

window.close()