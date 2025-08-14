import pandas as pd
import os
import glob

# Define column names based on the readme (26 columns total)
cols = ['unit_number', 'time_in_cycles', 'settings1', 'settings2', 'settings3'] + [f'sensor_{i}' for i in range(1, 24)]  # 5 + 21 = 26 columns

# Set the data directory path
data_dir = 'nasa_cmaps/CMaps'

# Process each dataset type (train/test) for all FD datasets
for split in ['train', 'test']:
    for fd in ['FD001', 'FD002', 'FD003', 'FD004']:
        filename = f'{split}_{fd}.txt'
        filepath = os.path.join(data_dir, filename)
        
        if os.path.exists(filepath):
            print(f"Processing {filename}...")
            df = pd.read_csv(filepath, sep='\s+', header=None, names=cols)
            csv_name = filename.replace('.txt', '.csv')
            df.to_csv(csv_name, index=False)
            print(f"Saved {csv_name}")

# Process RUL files
for fd in ['FD001', 'FD002', 'FD003', 'FD004']:
    rul_filename = f'RUL_{fd}.txt'
    rul_filepath = os.path.join(data_dir, rul_filename)
    
    if os.path.exists(rul_filepath):
        print(f"Processing {rul_filename}...")
        # RUL files have different format - just unit numbers and RUL values
        rul_df = pd.read_csv(rul_filepath, sep='\s+', header=None, names=['unit_number', 'RUL'])
        rul_csv_name = rul_filename.replace('.txt', '.csv')
        rul_df.to_csv(rul_csv_name, index=False)
        print(f"Saved {rul_csv_name}")

print("All files processed successfully!")