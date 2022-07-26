from sanulimestari import parse_words

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
	</kotus-sanalista>
	"""
	letters = {'m', 'i', 'k', 'a','s', 'd', 'e' }
	assert (['mika', 'sade'], letters)  == parse_words(doc, 4)
