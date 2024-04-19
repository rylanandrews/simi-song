# https://docs.pysimplegui.com/en/latest/documentation/what_is_it/fun_as_a_goal/

import PySimpleGUI as sg

import time

unsortedSongs = "multiple\nsongs\nhere"

sortStatusBar = sg.StatusBar(text="Waiting", enable_events=True)
timeStatusBar = sg.StatusBar(text="0 ms", enable_events=True)

layout = [  
    [sg.Text(text="Input a song: "), sg.Input(default_text="", key="-INPUT-"), sg.Button("Shell Sort", k="-ShellSort-"), sg.Button("Quick Sort", k="-QuickSort-")],
    [sg.Text(text="Unsorted Songs", size=(45, 1)), sg.Text(text="Sorted Songs")],
    [sg.Multiline(default_text=unsortedSongs, size=(50,30)), sg.Output(size=(50,30))],
    [sg.Text(text="Status:"), sortStatusBar],
    [sg.Text(text="Time for last operation:"), timeStatusBar],
            ]

# Create the Window
window = sg.Window('Simi-song', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == "-ShellSort-":
        sortStatusBar.update(value="Computing")

        # TODO: assign similarity index
        # TODO: call shell sort on data
        time.sleep(1)

        sortStatusBar.update(value="Done")

        # TODO: display data

    if event == "-QuickSort-":
        sortStatusBar.update(value="Computing")

        # TODO: assign similarity index
        # TODO: call quick sort on data
        time.sleep(1)

        sortStatusBar.update(value="Done")

        # TODO: display data
        

window.close()