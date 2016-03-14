def matching_letter_count(word1, word2):
	letters1 = list(word1)
	letters2 = list(word2)
	count = 0

	for n in range(0,5):
		if letters1[n] == letters2[n]:
			count += 1

	return count
