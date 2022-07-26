import xml.etree.ElementTree as ET

def parse_words(document, word_length):
	words = []
	letters = set()
	root = ET.fromstring(document)
	for word in root.findall('.//st/s'):
		if len(word.text) == word_length:
			normalized_word = word.text.lower()
			for letter in normalized_word:
				letters.add(letter)
			words.append(normalized_word)

	return (words, letters)