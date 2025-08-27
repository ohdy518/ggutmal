import pandas as pd
import os

def concat_csv_files(file_list, output_file):
    """
    Concatenate multiple CSV files into one.
    
    Args:
        file_list (list): List of CSV file paths to concatenate
        output_file (str): Output CSV file path
    """
    if not file_list:
        print("No CSV files provided")
        return
    
    print(f"Concatenating {len(file_list)} CSV files:")
    for file in file_list:
        print(f"  - {file}")
    
    dataframes = []
    for file in file_list:
        if not os.path.exists(file):
            print(f"Warning: File not found: {file}")
            continue
            
        try:
            df = pd.read_csv(file)
            dataframes.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")
    
    if dataframes:
        concatenated_df = pd.concat(dataframes, ignore_index=True)
        concatenated_df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"Successfully concatenated {len(dataframes)} files into {output_file}")
        print(f"Total rows: {len(concatenated_df)}")
    else:
        print("No valid CSV files to concatenate")

if __name__ == "__main__":
    # Example usage
    csv_files = [f"./data/modified/edited/{i+1}.csv" for i in range(15)]
    output_file = "./data/modified/concat/concat_full.csv"
    
    concat_csv_files(csv_files, output_file)