import xml.etree.ElementTree as ET

def parse_words(document, word_length):
	words = []
	root = ET.fromstring(document)
	for word in root.findall('.//st/s'):
		if len(word.text) == word_length:
			words.append(word.text)
	return words