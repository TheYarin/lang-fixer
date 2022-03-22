#!/usr/bin/python
# -*- coding: utf8 -*-

from replacer import replacer


def test_empty_string():
    assert replacer('') == ''

def test_heb_to_eng():
    assert replacer('אבג') == 'tcd'

def test_eng_to_heb():
    assert replacer('tcd') == 'אבג'

def test_mixed_1():
    assert replacer('tcdאבג') == 'tcdtcd'

def test_mixed_2():
    assert replacer('asdfש') == 'asdfa'

def test_unknown_character_shouldnt_change_anything():
    assert replacer('\n') == '\n'

def test_only_ambiguous_chars_shouldnt_change_anything():
    assert replacer('.,/') == '.,/'

def test_ambiguous_char_at_the_end():
    assert replacer('asdf.') == 'שדגכץ'

def test_ambiguous_char_at_the_start():
    assert replacer('.asdf') == 'ץשדגכ'

def test_text_with_capital_letters():
    assert replacer('Hקךךם Wםרךג!') == 'Hello World!'

def test_edge_case():
    assert replacer("asdf'") == 'שדגכ,'