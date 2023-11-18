import pandas as pd
import os
import re

def create_switch_classifier(df):
    switch_classifier = {}
    for i in range(len(df)):
        if pd.notna(df.iloc[i, 2]) and pd.notna(df.iloc[i, 4]):
            key_range = (df.iloc[i, 2], df.iloc[i, 4])
            switch_classifier[key_range] = df.iloc[i, 7]
    return switch_classifier

def repcurrent_v = int(match.group(1))
                v_values[current_v] = []  matches = re.finditer(r'\((\d+)\)/abs', line)
    for match in matches:
        index = int(match.group(1))
        for key_range in switch_classifier:
            if key_range[0] <= index <= key_range[1]:
                replacement = f'(v={switch_classifier[key_range]})/abs'
                # 测试用例
                # print(f"匹配项在: {line.strip()}")
                # print(f"替换 {match.group()} 为 {replacement}")
                modified_line = modified_line.replace(match.group(), replacement, 1)
                break  # 找到匹配项后立即跳出循环

        else:
            print(f"序号 {index} 超出范围")

    return modified_line




def process_file(file_path, switch_classifier):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = [replace_index_in_line(line, switch_classifier) for line in lines]

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
    print(f" {file_path} 处理完毕")

# 读取Excel文件
excel_file_path = 'index.xlsx'
df = pd.read_excel(excel_file_path)
df.iloc[:, 2:5] = df.iloc[:, 2:5].apply(pd.to_numeric, errors='coerce')

# 创建 switch 分类器
switch_classifier = create_switch_classifier(df)
# 测试用例。打印 switch_classifier 的内容
# print("Switch_Classifier:")
# for key, value in switch_classifier.items():
#     print(f"Range: {key}, Value: {value}")

# 处理data文件夹下的所有txt文件
data_directory = 'data/'
for filename in os.listdir(data_directory):
    if filename.endswith(".txt"):
        file_path = os.path.join(data_directory, filename)
        process_file(file_path, switch_classifier)
