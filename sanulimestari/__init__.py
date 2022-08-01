import xml.etree.ElementTree as ET

def parse_words(document, word_length, letters):
	words = []
	root = ET.fromstring(document)
	for word in root.findall('.//st/s'):
		if len(word.text) == word_length:
			normalized_word = word.text.lower()
			if not set(normalized_word) - letters:
				words.append(normalized_word)

	return words


def guess_word(guess, word):

	if len(guess) != len(word):
		raise ValueError("The 'word' and the 'guess' must have same length!")

	match = []
	for i in range(0, len(guess)):
		if guess[i] == word[i]:
			match.append('+')
		else:
			match.append('-')

	return (''.join(match), [])