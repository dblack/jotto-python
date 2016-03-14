class WordLengthException(Exception):
	def __init__(self):
		Exception.__init__(self, "Jotto words have to have exactly five letters")

def load_dictionary(filename="fives"):
	return [w.strip() for w in open(filename).readlines()]

def matching_letter_count(word1, word2):
	if len(word1) != 5 or len(word2) != 5:
		raise WordLengthException()

	return len([n for n in range(0,5) if word1[n] == word2[n]])
