# I made this function after reviewing the code on https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python
def makeTrie(informativeTracks):
    node = dict()
    for track in informativeTracks:
        currentNode = node
        for letter in track:
            currentNode = currentNode.setdefault(letter, {})
        currentNode['_end_'] = '_end_'

def autocomplete(trie, inputString):
    currentNode = trie
    # Navigate down the trie
    for letter in inputString:
        if letter in currentNode:
            currentNode = currentNode[letter]
        else:
            return "No matches found"
    
    stack = [(currentNode, inputString)]
    words = []
    
    # Continue to navigate down, but collect words
    while not stack.empty():
        currentNode, prefix = stack.pop()
        for letter, childNode in currentNode.items():
            if letter == end:
                words.append(prefix)
            else:
                stack.append((childNode, prefix + letter))
    
    return words