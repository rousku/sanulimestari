import xml.etree.ElementTree as ET

def parse_words(document, word_length):
	words = []
	letters = set()
	root = ET.fromstring(document)
	for word in root.findall('.//st/s'):
		if len(word.text) == word_length:
			for letter in word.text:
				letters.add(letter)
			words.append(word.text)

	return (words, letters)