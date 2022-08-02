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

    choice = []
    not_found = set()

    for i in range(0, len(guess)):
        if guess[i] == word[i]:
            choice.append(guess[i])
        else:
            choice.append(set(guess[i]))
            not_found.add(guess[i])

    for part in choice:
        if isinstance(part, set):
            part.update(not_found)

    return [[
        '^' + ''.join(sorted(list(part))) if isinstance(part, set) else part
        for part in choice
    ]]
