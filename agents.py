import pandas as pd
import random

def random_word_selection(df, syllable):
    options = df[df['sw'] == syllable]
    choice = options.values[random.randrange(0, len(options))][0]
    return choice