import pandas as pd



def modify(input_file, output_file):

    df = pd.read_csv(input_file, encoding='utf-8')

    word = df.columns[0]  # Get the actual column name
    pos = df.columns[5]
    is_external = df.columns[2]

    df[word] = df[word].str.replace(r'\(\d+\)$', '', regex=True)

    # Filter out rows starting or ending with '-'
    mask = ~( (df[word].str.len()==1) | df[word].str.startswith('-') | df[word].str.endswith('-') | ~(df[pos].str.startswith('「명사」')) | df[is_external].str.startswith('외래어'))
    df_cleaned = df[mask].copy()

    # Remove all '-' characters from the column
    df_cleaned[word] = df_cleaned[word].str.replace('-', '')
    df_cleaned[word] = df_cleaned[word].str.replace('^', '')

    df_cleaned = df_cleaned.drop_duplicates(subset=[word], keep='first')

    df_cleaned.to_csv(output_file, index=False, encoding='utf-8-sig')

if __name__ == '__main__':
    for i in range(0, 15):
        j = i+1
        input_file = f'./data/modified/trimmed/{j}.csv'
        output_file = f"./data/modified/edited/{j}.csv"
        modify(input_file, output_file)
        print(f"modified {input_file} to {output_file}")