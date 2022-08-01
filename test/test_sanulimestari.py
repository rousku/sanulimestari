from sanulimestari import parse_words, guess_word
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
    letters = {'m', 'i', 'k', 'a','s', 'd', 'e' }
    assert (['mika', 'sade'])  == parse_words(doc, 4, letters)

@pytest.mark.parametrize('guess,word,expected', [('b', 'a', ('-', [])),
                                                 ('a', 'a', ('+', [])),
                                                 ('aa', 'aa', ('++', [])),
                                                 ('bb', 'ba', ('+-', [])),
                                                 ('ab', 'bb', ('-+', [])),
                                                 ('aa', 'bb', ('--', [])),
                                                 ('abb', 'cad', ('---', []))])
def test_guess_word(guess, word, expected):
    assert expected == guess_word(guess, word)

def test_guess_word_lenghts_dont_match():
    with pytest.raises(ValueError, match="The 'word' and the 'guess' must have same length!"):
        guess_word('a', 'ab')