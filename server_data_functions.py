import pandas as pd
import agents

DATA_FILE_LOCATION = "./data/prod/prod.csv"
WORDS_COL_NAME = '어휘'
AGENT = agents.dead_end_else_no_worst

# Foundational game status
reject_input = False
game_running = False
player_playing = True # First player is named alpha.

user_wins = False

# Word status
last_syllable = "*"

agent_word = ""

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
    print(last_syllable)
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
    if not word_in_dictionary(word): print("a"); return False
    if not word_starts_with_last_syllable(word): print("b"); return False

    return True

def word_in_dictionary(word: str):
    return word in valid_words

def calculate_dead_ends():
    global dead_ends, df
    all_syllables = set(df['sw']) | set(df['ew'])
    dead_ends = all_syllables - set(df['sw'])

def initialize():
    global game_running, reject_input, player_playing, last_syllable, dead_ends, df, valid_words
    reject_input = False
    player_playing = True  # First player is named alpha.

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
    print("pw")
    global reject_input, game_running, player_playing, agent_word, user_wins
    reject_input = False

    if not word_is_valid(word): print(f">{word}<"); reject_input = True; return

    print(f'-> {word}')

    if is_dead_end(word):
        print("dead end! game over")
        game_running = False
        if player_playing:
            user_wins = True
        else:
            user_wins = False
        return

    drop_word(word)
    calculate_dead_ends()

    player_playing = not player_playing

    if not player_playing:
        agent_word = AGENT(df, last_syllable)
        process_word(agent_word)

def input_manager():
    global player_playing, reject_input
    while game_running:
        # print(alpha_playing)
        while True:
            reject_input = False
            user_input = input(f"Player {'alpha' if player_playing else 'beta'} -- Enter word: ")
            process_word(user_input)

            # Input rejection mechanism
            if not reject_input: break
            print("Input rejected.")
        # print("next!")
        player_playing = not player_playing

if __name__ == "__main__":
    initialize()
    print(process_word("기쁨"))