class WordLengthException(Exception):
    def __init__(self):
        Exception.__init__(self, "Jotto words have to have exactly five letters")

def matching_letter_count(word1, word2):
    if len(word1) != 5 or len(word2) != 5:
        raise WordLengthException()

    return len([t for t in zip(word1, word2) if t[0] == t[1]])
