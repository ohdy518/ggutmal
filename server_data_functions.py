import pandas as pd

DATA_FILE_LOCATION = "./data/prod/prod.csv"
WORDS_COL_NAME = '어휘'

# Foundational game status
reject_input = False
game_running = False
alpha_playing = True # First player is named alpha.

# Word status
last_syllable = "*"

dead_ends = set()

df = pd.read_csv(DATA_FILE_LOCATION)
valid_words = set(df[WORDS_COL_NAME])

def drop_word(word: str):
    global df, valid_words
    df = df[df[WORDS_COL_NAME] != word]
    valid_words = set(df[WORDS_COL_NAME])

def set_last_syllable(word: str):
    global last_syllable
    last_syllable = df['ew'][df[WORDS_COL_NAME] == word].values[0]

def word_starts_with_last_syllable(word: str) -> bool:
    global last_syllable
    if last_syllable == "*":
        set_last_syllable(word)
        return True
    if last_syllable == df['sw'][df[WORDS_COL_NAME] == word].values[0]:
        set_last_syllable(word)
        return True
    return False

def is_dead_end(word: str):
    if df['ew'][df[WORDS_COL_NAME] == word].values[0] in dead_ends:
        return True
    return False

def word_is_valid(word: str) -> bool:
    if not word_in_dictionary(word): return False
    if not word_starts_with_last_syllable(word): return False

    return True

def word_in_dictionary(word: str):
    return word in valid_words

def calculate_dead_ends():
    global dead_ends, df
    all_syllables = set(df['sw']) | set(df['ew'])
    dead_ends = all_syllables - set(df['sw'])

def initialize():
    global game_running, reject_input, alpha_playing, last_syllable, dead_ends, df, valid_words
    reject_input = False
    alpha_playing = True  # First player is named alpha.

    # Word status
    last_syllable = "*"

    dead_ends = set()

    df = pd.read_csv(DATA_FILE_LOCATION)
    valid_words = set(df[WORDS_COL_NAME])

    game_running = True
    calculate_dead_ends()
    # print(dead_ends)
    # input_manager()

def process_word(word: str):
    global reject_input, game_running
    reject_input = False
    if not word_is_valid(word): reject_input = True; return

    print('->')

    if is_dead_end(word):
        print("dead end! game over")
        game_running = False

    drop_word(word)
    calculate_dead_ends()

def input_manager():
    global alpha_playing, reject_input
    while game_running:
        # print(alpha_playing)
        while True:
            reject_input = False
            user_input = input(f"Player {'alpha' if alpha_playing else 'beta'} -- Enter word: ")
            process_word(user_input)

            # Input rejection mechanism
            if not reject_input: break
            print("Input rejected.")
        # print("next!")
        alpha_playing = not alpha_playing

if __name__ == "__main__":
    initialize()