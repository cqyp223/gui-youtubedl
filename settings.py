#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Łukasz Marcińczak
# Date: 2018-03-30


def read_settings(path):
    try:
        plik = open(path, "r")
        s = plik.read()
        plik.close()
    except IOError:
        return ""
        
    s = s.split(";")
    return s
    
def write_settings(path, text):
    """ Zapisuje ustawienia do pluku <path>.
        Text w postaci listy ustawień [] """
    
    s = text[0]
    for i in range(1, len(text)):
        s = s + ";" + text[i]
    
    plik = open(path, "w")
    plik.write(s)
    plik.close()

