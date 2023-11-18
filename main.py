import re
import pandas as pd
import os

data_directory = 'data/'

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        v_values = {}
        current_v = None
        for i, line in enumerate(lines):
            if "v=" in line:
                match = re.search(r'v=(.*?)\)', line)
                if match:
                    current_v = match.group(1).strip()
                    if i + 2 < len(lines):
                        description_line = lines[i + 2].strip()
                        values = description_line.split()
                        if values:
                            description = values[-1]
                            v_values[current_v] = [description]

        return v_values

    except Exception as e:
        print(f"Error processing file '{file_path}': {str(e)}")
        return None  # Return None to indicate failure

data_frames = []
file_names = sorted([f for f in os.listdir(data_directory) if f.endswith('.txt')])

for file_name in file_names:
    file_path = os.path.join(data_directory, file_name)
    v_values = process_file(file_path)

    if v_values is None:
        # If processing failed, continue to the next file
        continue

    if not v_values:
        v_values[0] = [0]

    df = pd.DataFrame.from_dict(v_values, orient='index').transpose()
    df.insert(0, '', file_name.replace('.txt', ''))
    data_frames.append(df)
    print(file_name + "  finished")

final_df = pd.concat(data_frames, ignore_index=True)
excel_path = 'output.xlsx'
final_df.to_excel(excel_path, index=False)
excel_path
