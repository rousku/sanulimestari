from sanulimestari import parse_words, guess_word, get_best_guess, match
import pytest
import string


def test_parse_words():

    doc = """<?xml version="1.0" encoding="utf-8"?>
    <!DOCTYPE kotus-sanalista SYSTEM "kotus-sanalista.dtd">
    <!--
        Comment
    -->
    <kotus-sanalista>
    <st><s>ahven</s><t><tn>38</tn></t></st>
    <st><s>MIKA</s><t><tn>38</tn></t></st>
    <st><s>tor</s><t><tn>99</tn></t></st>
    <st><s>sade</s><t><tn>40</tn></t></st>
    <st><s>pito</s><t><tn>40</tn></t></st>
    </kotus-sanalista>
    """
    letters = {'m', 'i', 'k', 'a', 's', 'd', 'e'}
    assert (['mika', 'sade']) == parse_words(doc, 4, letters)


@pytest.mark.parametrize('guess,word,expected',
                         [('b', 'a', [['^b']]), ('a', 'a', [['a']]),
                          ('ac', 'ac', [['a', 'c']]),
                          ('bb', 'ba', [['b', '^b']]),
                          ('ab', 'bb', [['^a', 'b']]),
                          ('aa', 'bb', [['^a', '^a']]),
                          ('ab', 'ce', [['^ab', '^ab']]),
                          ('aa', 'ca', [['^a', 'a']]),
                          ('ab', 'ca', [['^ab', 'a']]),
                          ('abb', 'cad', [['^ab', 'a', '^b'],['^ab', '^b', 'a']]),
                          ('abc', 'cad', [['c', 'a', '^bc'],['c', '^b', 'a'],['^ab', 'c', 'a']]),
                          ('aabb', 'cdae', [['^ab', '^ab', 'a', '^b'], ['^ab', '^ab', '^b', 'a']]),
                          ('abab', 'baba', [['b', 'a', 'b', 'a']])
                          ])
def test_guess_word(guess, word, expected):
    assert expected == guess_word(guess, word)


def test_guess_word_lenghts_dont_match():
    with pytest.raises(
            ValueError,
            match="The 'word' and the 'guess' must have same length!"):
        guess_word('a', 'ab')


@pytest.mark.parametrize('word,filters,expected', [('a', [], False),
                                                    ('a', [['a']], True), 
                                                    ('b', [['a']], False),
                                                    ('ab', [['b', 'b']], False),
                                                    ('ab', [['a', 'a']], False),
                                                    ('ab', [['a', 'b']], True),
                                                    ('a', [['^c']], True),
                                                    ('c', [['^c']], False),
                                                    ('ab', [['a', '^b']], False),
                                                    ('ab', [['a', '^c']], True),
                                                    ('ab', [['^a', 'b']], False), 
                                                    ('ab', [['^c', 'b']], True), 
                                                    ('ab', [['^a', '^b']], False),
                                                    ('ab', [['^c', '^d']], True),
                                                    ('a', [['^bc']], True),
                                                    ('a', [['^ca']], False), 
                                                    ('a', [['b'], ['a']], True),
                                                    ('a', [['a'], ['b']], True),
                                                    ('a', [['b'], ['c']], False),
                                                    ('a', [['a'], ['^c']], True),
                                                    ('abc', [['a', 'e', 'c']], False)])
def test_match(word, filters, expected):
    assert expected == match(word, filters)

def test_parse_kotus_words():
    letters = set(string.ascii_lowercase)
    letters.add('ä')
    letters.add('ö')
    
    words = parse_words(open('.\\kotus-sanalista_v1\\kotus-sanalista_v1.xml', encoding='utf-8').read(), 5, letters)
    assert 3271 == len(words)
    assert 'pöytä' in words

def test_get_best_guess():
    assert ('kasti', 286123) == get_best_guess('.\\kotus-sanalista_v1\\kotus-sanalista_v1.xml', 5)

def test_get_second_best_guess():
    assert ('lopen', 23822) == get_best_guess('.\\kotus-sanalista_v1\\kotus-sanalista_v1.xml', 5, ['kasti'])