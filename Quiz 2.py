#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 02:11:35 2020

@author: smrahman
"""

# The variable sentence stores a string.
# Write code to determine how many words in sentence start and end with the same letter, including one-letter words.
# Store the result in the variable same_letter_count.

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.

same_letter_count = sum(w[0] == w[-1] for w in sentence.split())

print(same_letter_count)