# Authors: Rylan Andrews and Connor Ambrose

# Credit: PySimpleGUI documentation
# https://docs.pysimplegui.com/en/latest/documentation/what_is_it/fun_as_a_goal/

import PySimpleGUI as sg

import timeit

from load_similarities import *
from autocomplete import *
import Quick_sort
import shell_sort


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
unsortedText = sg.Text(text="Unsorted Songs", size=(65, 1))
sortedText = sg.Text(text="Sorted Songs")

# Fifth Row
unsortedSongs = sg.Multiline(default_text="", size=(70,30))
sortedSongs = sg.Output(size=(70,30))

# Sixth Row
sortTextBox = sg.Text(text="Status:")
sortStatusBar = sg.StatusBar(text="Waiting", enable_events=True)

# Seventh Row
timeTextBox = sg.Text(text="Time for last sort (s):")
timeStatusBar = sg.StatusBar(text="0 s", enable_events=True)

# Layout is organized as a series of rows
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

# Import the dataset and make a trie with it
current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, '..', 'data')
readInData(path = path, numFilesToProcess = 30) # adjust numFilesToProcess to change start-up time
trie = makeTrie(trackPlaylists.keys())

# Event Loop to process "events" and get the "values" of the inputs
while True:
    # Detect events and values
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    # For every input in the text box, update the suggestions box
    if event == "-INPUT-":
        currentInput = values["-INPUT-"]

        # Clear suggestions box
        suggestedSongs.update(value="")     

        # Populate suggestions box
        if len(currentInput) < 6:
            suggestedSongs.update(value = "Please type more characters")
        elif (autocomplete(trie, currentInput) != "No matches found"):
            # Get possible matching songs
            possibleSongList = autocomplete(trie, currentInput)
            printStatement = ""
            # Print to suggestions box
            for song in possibleSongList:
                suggestedSongs.print(song)
        else:
            suggestedSongs.update(value = "No matches found")
        
    # Shell sort selected
    if event == "-ShellSort-":
        currentInput = values["-INPUT-"]
        
        # Compute similarities and catch exceptions
        waitForNewInput = False
        try: 
            similarities = computeSimilarityScores(currentInput, trackPlaylists, playlistsContent)
            
        except KeyError:
            sortStatusBar.update(value="Song not found")
            waitForNewInput = True

        if not waitForNewInput:
            # Populate the unsorted songs
            unsortedSongs.update(value="")
            for name, similarity in similarities.items():
                unsortedSongs.print(name + ": " + str(similarity))
            
            # Track start time
            startTime = timeit.timeit()

            # Call shell sort on data
            similaritiesSorted = shell_sort.shell_sort(list(similarities.items()))

            # Track end time and update elapsed time
            endTime = timeit.timeit()
            elapsedTime = endTime - startTime
            timeStatusBar.update(value=elapsedTime)

            sortStatusBar.update(value="Done")

            # Clear output box
            sortedSongs.update(value="")

            # Iterate through list of songs and print using sortedSongs.print
            for element in similaritiesSorted:
                sortedSongs.print(element[0] + ": " + str(element[1]))

    # Quick sort selected
    if event == "-QuickSort-":
        currentInput = values["-INPUT-"]
        
        # Compute similarities and catch exceptions
        waitForNewInput = False
        try: 
            similarities = computeSimilarityScores(currentInput, trackPlaylists, playlistsContent)
            
        except KeyError:
            sortStatusBar.update(value="Song not found")
            waitForNewInput = True

        if not waitForNewInput:
            # Populate the unsorted songs
            unsortedSongs.update(value="")
            for name, similarity in similarities.items():
                unsortedSongs.print(name + ": " + str(similarity))
            
            # Track start time
            startTime = timeit.timeit()

            # Call shell sort on data
            similaritiesSorted = list(similarities.items())
            Quick_sort.quick_sort(similaritiesSorted, 0, len(similaritiesSorted)-1)

            # Track end time and update elapsed time
            endTime = timeit.timeit()
            elapsedTime = endTime - startTime
            timeStatusBar.update(value=elapsedTime)

            sortStatusBar.update(value="Done")

            # Clear output box
            sortedSongs.update(value="")

            # Iterate through list of songs and print using sortedSongs.print
            for element in similaritiesSorted:
                sortedSongs.print(element[0] + ": " + str(element[1]))          
        
window.close()