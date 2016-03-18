class WordLengthException(Exception):
    def __init__(self):
        Exception.__init__(self, "Jotto words have to have exactly five letters")

def matching_letter_count(word1, word2):
    if len(word1) is not 5 or len(word2) is not 5:
        raise WordLengthException()

    return len([True for char1, char2 in zip(word1, word2) if char1 == char2])
