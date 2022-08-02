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
    excluded = {}
    letter_count = {}

    for i in range(0, len(guess)):

        if not word[i] in letter_count:
            letter_count[word[i]] = 0
        letter_count[word[i]] = letter_count[word[i]] + 1

        if guess[i] == word[i]:
            choice.append(guess[i])
        else:
            choice.append(set(guess[i]))

            if not guess[i] in word:
                not_found.add(guess[i])
            else:
                if not guess[i] in excluded:
                    excluded[guess[i]] = set(range(0,len(guess)))
                excluded[guess[i]].remove(i)

    for part in choice:
        if isinstance(part, set):
            part.update(not_found)

    choice = [
        '^' + ''.join(sorted(list(part))) if isinstance(part, set) else part
        for part in choice
    ]


    return [choice]
