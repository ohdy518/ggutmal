import os
import pandas as pd
from pathlib import Path


def convert_xls_to_csv(input_dir, output_dir):
    """
    Convert all XLS files in input directory to CSV files in output directory.
    
    Args:
        input_dir (str): Path to directory containing XLS files
        output_dir (str): Path to directory where CSV files will be saved
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Find all XLS files in input directory
    xls_files = list(input_path.glob("*.xls")) + list(input_path.glob("*.xlsx"))
    
    if not xls_files:
        print(f"No XLS files found in {input_dir}")
        return
    
    print(f"Found {len(xls_files)} XLS file(s) to convert")
    
    for xls_file in xls_files:
        try:
            # Read XLS file
            df = pd.read_excel(xls_file)
            
            # Create CSV filename
            csv_filename = xls_file.stem + ".csv"
            csv_path = output_path / csv_filename
            
            # Save as CSV
            df.to_csv(csv_path, index=False)
            print(f"Converted: {xls_file.name} -> {csv_filename}")
            
        except Exception as e:
            print(f"Error converting {xls_file.name}: {str(e)}")


if __name__ == "__main__":
    input_directory = "./data/raw/xls"
    output_directory = "./data/raw/csv"
    
    convert_xls_to_csv(input_directory, output_directory)