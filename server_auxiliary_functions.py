import pandas as pd
DATA_FILE_LOCATION = "./data/prod/prod.csv"
WORDS_COL_NAME = '어휘'
WORDS_DEF_NAME = '뜻풀이'

df = pd.read_csv(DATA_FILE_LOCATION)

def define(word: str):
    if len(df[df[WORDS_COL_NAME] == word][WORDS_DEF_NAME]) == 0:
        return ""
    return df[df[WORDS_COL_NAME] == word][WORDS_DEF_NAME].values[0]

if __name__ == '__main__':
    print(define("자동차"))