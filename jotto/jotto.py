class WordLengthException(Exception):
	def __init__(self):
		Exception.__init__(self, "Jotto words have to have exactly five letters")


def matching_letter_count(word1, word2):
	letters1 = list(word1)
	letters2 = list(word2)

	if len(letters1) != 5 or len(letters2) != 5:
		raise WordLengthException()

	return len([n for n in range(0,5) if letters1[n] == letters2[n]])
