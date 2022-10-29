import xml.etree.ElementTree as ET
import itertools
import string
from functools import lru_cache, partial
from multiprocessing import Pool
import os

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

    combinations = []
    letters = []
    for letter in excluded:
        k = min(len(guess) - len(excluded[letter]), letter_count[letter])
        combinations.append(itertools.combinations(excluded[letter], k))
        letters.append(letter)

    choices = []
    for comb in itertools.product(*combinations):
        s = 0
        indecies = set()
        for letter_part in comb:
            indecies.update(letter_part)
            s = s + len(letter_part)

        if s == len(indecies):
            choice_copy = choice.copy()
            for letter_index, letter_part in enumerate(comb):
                for index in letter_part:
                    choice_copy[index] = letters[letter_index]

            choices.append(choice_copy)

    return choices

def match(sample, choices):
    for choice in choices:
        is_match = True
        for i in range(0, len(sample)):
            if choice[i][0] == '^':
                if sample[i] in choice[i]:
                    is_match = False
            else:
                if not choice[i] == sample[i]:
                    is_match = False

        if is_match:
            return True

    return False

@lru_cache(maxsize=None)
def get_word_count(filters, words):
    count = 0
    for word in words:

        filters_match = True

        for f in filters:
            if not match(word, f):
                filters_match = False

        if filters_match:
            count = count + 1

    return count

def task(guess, words, previous_guesses):
  
    matching_words = 0
    print(f"start {guess}")
    for sanuli in words:

        filters = [guess_word(guess, sanuli)]
        for previous_guess in previous_guesses:
            filters.append(guess_word(previous_guess, sanuli))

        def tuple2list(a):
            return tuple( tuple2list(x) if isinstance(x, list) else x for x in a) 

        matching_words = matching_words + get_word_count(tuple2list(filters), words)


    print(f"end {guess}")
    return { guess: matching_words }


def get_best_guess(kotus_word_list, word_length, previous_guesses=[]):
    letters = set(string.ascii_lowercase)
    letters.update('ä')
    letters.update('ö')
    words = tuple(parse_words(open(kotus_word_list, encoding='utf-8').read(), word_length, letters))

    results = {}

    with Pool() as pool:
        for result in pool.map(partial(task, words=words, previous_guesses=previous_guesses), words):
            results.update(result)
    

    best_guess = min(results, key=results.get)
    return (best_guess, results[best_guess])