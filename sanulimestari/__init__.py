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