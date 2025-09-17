import pandas as pd
import random

def random_word_selection(df, syllable):
    options = df[df['sw'] == syllable]
    choice = options.values[random.randrange(0, len(options))][0]
    return choice

def random_without_worst(df, syllable):
    all_syllables = set(df['sw']) | set(df['ew'])
    dead_ends = all_syllables - set(df['sw'])
    winnable = df[df['ew'].isin(dead_ends)]['sw']
    options = df[(df['sw'] == syllable) & (~df['ew'].isin(winnable))]
    if len(options) == 0:
        return ""
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

def dead_end_else_no_worst(df, syllable): # checks if dead end options are possible, if not choose one's that the bot does not lose.
    dead_end_check = return_dead_end_if_possible(df, syllable)
    if dead_end_check != "":
        return dead_end_check
    r = random_without_worst(df, syllable)
    if r != "":
        print("fb to rws")
        return random_word_selection(df, syllable)
    return r


def debug_static(_df, _syllable):
    return "정지"