import pandas as pd

def trim_csv(input_file, output_file, columns_to_remove=None, rows_to_remove=None):
    """
    Remove specified columns and rows from a CSV file
    
    Args:
        input_file: Path to input CSV file
        output_file: Path to output CSV file  
        columns_to_remove: List of column names/indices to remove (e.g., ['A', 'B', 'F'] or [0, 1, 5])
        rows_to_remove: List of row indices to remove (e.g., [0] for row 1)
    """
    # Read the CSV file
    df = pd.read_csv(input_file, encoding='utf-8')
    
    # Remove specified rows (if any)
    if rows_to_remove:
        df = df.drop(index=rows_to_remove)
    
    # Remove specified columns (if any)  
    if columns_to_remove:
        df = df.drop(columns=columns_to_remove, errors='ignore')
    
    # Save the trimmed CSV
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"Trimmed CSV saved to: {output_file}")

# Example usage:
if __name__ == "__main__":
    for i in range(0, 15):
        j = i + 1
        trim_csv(
            input_file=f"data/raw/csv/{j}.csv",
            output_file=f"data/modified/trimmed/{j}.csv",
            columns_to_remove=['어원', '활용', '발음', '주표제어', '부표제어', '의미 문형', '공통 문형', '공통 문법', '의미 문법', '용례', '범주', '전문 분야', '속담', '관용어', '관용구', '대역어', '검색용 이형태', '생물 분류군 정보', '멀티미디어', '관련 어휘', '한 걸음 더'],
            # rows_to_remove=[0]  # Row 1 is index 0
        )