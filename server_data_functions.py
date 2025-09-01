import pandas as pd

DATA_FILE_LOCATION = "./data/prod/prod.csv"
WORDS_COL_NAME = '어휘'

df = pd.read_csv(DATA_FILE_LOCATION)
valid_words = set(df[WORDS_COL_NAME])

def word_is_valid(word: str):
    return word in valid_words

if __name__ == "__main__":
    print(word_is_valid("한국어"))