from sanulimestari import parse_words, guess_word, first_guess
import pytest


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
                          ('abc', 'cad', [['c', 'a', '^bc'],['c', '^b', 'a'],['^ab', 'c', 'a']])
                          ])
def test_guess_word(guess, word, expected):
    assert expected == guess_word(guess, word)


def test_guess_word_lenghts_dont_match():
    with pytest.raises(
            ValueError,
            match="The 'word' and the 'guess' must have same length!"):
        guess_word('a', 'ab')


def test_first_guess():
    assert ('oieta', 4730143) == first_guess('.\\kotus-sanalista_v1\\kotus-sanalista_v1.xml', 5)
