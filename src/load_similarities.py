import os
import json
from collections import defaultdict

numPlaylistsProcessed = 0
trackPlaylists = defaultdict(list) # Solution from https://stackoverflow.com/questions/11509721/how-do-i-initialize-a-dictionary-of-empty-lists-in-python
tracksInfo = dict()
playlistsContent = dict()
informativeNameToURIs = dict()

def readInData(path, numFilesToProcess = 100):
    """Goes through each file in the provided path and fetchs their contents to be put in the dictionaries
    input:
        path: a string that leads to the folder with data files
        numFilesToProcess: an integer count of how many files should be read in
    """
    numFilesProcessed = 0
    files = os.listdir(path)
    for file in files:
        if file.startswith("mpd.slice.") and file.endswith(".json"):
            fullPath = os.path.join(path, file)
            f = open(fullPath)
            stringContents = f.read()
            filesDict = json.loads(stringContents)
            f.close()
            
            for playlist in filesDict["playlists"]:
                processData(playlist)
            
            numFilesProcessed += 1
                
            if numFilesProcessed >= numFilesToProcess:
                return
            
def processData(playlist):
        """Takes in a playlist dictionary and stores tracks in each playlist and the playlist containing each track
        Input:
            playlist: a dictionary containing the playlist name, tracks within, and information on those tracks
        """
        playlistID = playlist["pid"]
        tracks = []
    
        for track in playlist["tracks"]:
            # Skip loop if the track lacks information
            if track["track_uri"] == "" or track["track_name"] == "" \
                or track["artist_name"] == "" or track["album_name"] == "":
                continue

            track_uri = track["track_uri"]
            tracks.append(track_uri) # Make a list of tracks in that playlist
            trackPlaylists[track_uri].append(playlistID) # Add the playlist to each track
            
            # Store the track information
            trackInfo = dict()
            trackInfo["track_name"] = track["track_name"]
            trackInfo["artist_name"] = track["artist_name"]
            trackInfo["album_name"] = track["album_name"]
            tracksInfo[track_uri] = trackInfo

            # Store the IDs by track
            name = track["track_name"] + " by " + track["artist_name"]
            tracksInfo[track_uri]["condensed_name"] = name
            informativeNameToURIs[name] = track_uri
        
        playlistsContent[playlistID] = tracks  

def computeSimilarityScores(trackID, trackPlaylists, playlistsContent):
    """Computes a similarity score defined by the number of tracks in each playlist and adds this score to each song
    Inputs:
        trackID: a string of the unique Spotify track ID
        trackPlaylists: a dictionary with trackID keys and a list of playlists containing that ID as values
        playlistsContent: a dictionary with unique playlist ID as keys and songs in that playlist as values
    Output:
        A dictionary of unique trackIDs (as strings) and a similarity score (as a float) to the specified track as values 
    """
    trackSimilarity = defaultdict(float)
    
    playlists_to_consider = trackPlaylists[trackID]
    for playlist in playlists_to_consider:
        similarityScore = 1 / (1 + len(playlistsContent[playlist])/500)
        
        for track in playlistsContent[playlist]:
            trackSimilarity[track] += similarityScore
            
    del trackSimilarity[trackID]
    
    return trackSimilarity

# Miscellaneous Functions
def getTrackName(trackID, tracksInfo):
    return tracksInfo[trackID]["track_name"]

def getArtistName(trackID, tracksInfo):
    return tracksInfo[trackID]["artist_name"]

def getAlbumName(trackID, tracksInfo):
    return tracksInfo[trackID]["album_name"]

def getCondensedName(trackID, tracksInfo):
    return tracksInfo[trackID]["condensed_name"]

def getTrackURI(trackInfo, infoToTracks):
    return infoToTracks[trackInfo]

# Actual code
# current_dir = os.path.dirname(os.path.abspath(__file__))
# path = os.path.join(current_dir, '..', 'data')
# readInData(path = path)

### EXAMPLE
# testTrack = "spotify:track:3cVWNLd0uEHkc2tnBoE3Ay"
# print(f'The test track is {getCondensedName(testTrack, tracksInfo)} with URI {getTrackURI(getCondensedName(testTrack, tracksInfo), informativeNameToURIs)}.')
# similarityScores = computeSimilarityScores(trackID = testTrack, trackPlaylists = trackPlaylists, playlistsContent = playlistsContent)
# similarityScores = similarityScores.items() # Converting to a list of tuples