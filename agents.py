import pandas as pd
import random

def random_word_selection(df, syllable):
    options = df[df['sw'] == syllable]
    choice = options.values[random.randrange(0, len(options))][0]
    return choice

def return_dead_end_if_possible(df, syllable):
    all_syllables = set(df['sw']) | set(df['ew'])
    dead_ends = all_syllables - set(df['sw'])
    options = df[(df['sw'] == syllable) & (df['ew'].isin(dead_ends))]
    if len(options) == 0:
        return ""
    return options.values[random.randrange(0, len(options))][0]

def dead_end_else_random(df, syllable):
    dead_end_check = return_dead_end_if_possible(df, syllable)
    if dead_end_check != "":
        return dead_end_check
    return random_word_selection(df, syllable)