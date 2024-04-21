# https://docs.pysimplegui.com/en/latest/documentation/what_is_it/fun_as_a_goal/

import PySimpleGUI as sg

import time
import timeit

## Preparing GUI

# First Row
songInputText = sg.Text(text="Input a song: ")
songInput = sg.Input(default_text="", key="-INPUT-", enable_events=True)
shellSortButton = sg.Button("Shell Sort", k="-ShellSort-")
quickSortButton = sg.Button("Quick Sort", k="-QuickSort-")

# Second Row
suggestionsTextBox = sg.Text(text="Suggestions")

# Third Row
suggestedSongs = sg.Multiline(size=(45, 5))

# Fourth Row
unsortedText = sg.Text(text="Unsorted Songs", size=(45, 1))
sortedText = sg.Text(text="Sorted Songs")

# Fifth Row
unsortedSongs = sg.Multiline(default_text="multiple\nsongs\nhere", size=(50,30))
sortedSongs = sg.Output(size=(50,30))

# Sixth Row
sortTextBox = sg.Text(text="Status:")
sortStatusBar = sg.StatusBar(text="Waiting", enable_events=True)

# Seventh Row
timeTextBox = sg.Text(text="Time for last sort (s):")
timeStatusBar = sg.StatusBar(text="0 s", enable_events=True)


layout = [  
    [songInputText, songInput, shellSortButton, quickSortButton],
    [suggestionsTextBox],
    [suggestedSongs],
    [unsortedText, sortedText],
    [unsortedSongs, sortedSongs],
    [sortTextBox, sortStatusBar],
    [timeTextBox, timeStatusBar],
            ]

# Create the Window
window = sg.Window('Simi-song', layout)

## Program Running

## Data Import

# TODO: Import dataset

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == "-INPUT-":
        currentInput = values["-INPUT-"]

        # Clear suggestions box
        suggestedSongs.update(value="")     

        # Add suggestions from an array by iterating through array and printing to box
        suggestedSongs.print(currentInput)

        # TODO: populate suggestions box


    if event == "-ShellSort-":
        currentInput = values["-INPUT-"]
        # TODO: Implement song not found error
        

        # TODO: assign similarity index

        # Track start time
        startTime = timeit.timeit()

        # TODO: call shell sort on data

        # Track end time and update elapsed time
        endTime = timeit.timeit()
        elapsedTime = endTime - startTime
        timeStatusBar.update(value=elapsedTime)

        sortStatusBar.update(value="Done")

        # Clear output box
        sortedSongs.update(value="")

        # TODO: display data
        # Iterate through list of songs and print using sortedSongs.print
        sortedSongs.print("Sorted")
        sortedSongs.print("sorted")

    if event == "-QuickSort-":
        currentInput = values["-INPUT-"]
        # TODO: Implement song not found error

        # TODO: assign similarity index

        # Track start time
        startTime = timeit.timeit()

        # TODO: call quick sort on data

        # Track end time and update elapsed time
        endTime = timeit.timeit()
        elapsedTime = endTime - startTime
        timeStatusBar.update(value=elapsedTime)

        sortStatusBar.update(value="Done")

        # Clear output box
        sortedSongs.update(value="")

        # TODO: display data
        # Iterate through list of songs and print using sortedSongs.print
        sortedSongs.print("Sorted")
        sortedSongs.print("sorted")
        

window.close()