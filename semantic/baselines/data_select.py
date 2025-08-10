import pandas as pd
import os
import time

# 定义文件夹路径，其中包含所有Excel文件
folder_path = '../baselines/output'

# 定义输出文件夹路径
output_folder_path = '../Datafiles'

# 确保输出文件夹存在
os.makedirs(output_folder_path, exist_ok=True)

# 获取当前时间戳
timestamp = time.strftime("%Y%m%d_%H%M%S")

# 创建一个空的DataFrame，用于存储所有结果
all_filtered_data = pd.DataFrame()

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        # 读取Excel文件
        file_path = os.path.join(folder_path, filename)
        df = pd.read_excel(file_path)

        # 筛选相似度小于x的行
        filtered_df = df[df.iloc[:, 2] > 0.6]

        # 如果有数据满足条件，则加入到总的DataFrame中
        if not filtered_df.empty:
            # 为数据添加来源文件名列（可选）
            filtered_df['Source_File'] = filename
            # 将筛选的数据追加到总的DataFrame中
            all_filtered_data = pd.concat([all_filtered_data, filtered_df], ignore_index=True)


# 去除表示意思相同的行，即第一列和第二列的互换行
def remove_duplicate_pairs(df):
    seen = set()
    unique_rows = []

    for _, row in df.iterrows():
        # 将第一列和第二列的值以元组形式存储并排序，保证顺序不影响判断
        pair = tuple(sorted([row[0], row[1]]))

        if pair not in seen:
            seen.add(pair)
            unique_rows.append(row)

    return pd.DataFrame(unique_rows)


# 如果有数据满足条件，则去除重复的行并保存到一个新的Excel文件中
if not all_filtered_data.empty:
    # 移除重复的行
    all_filtered_data = remove_duplicate_pairs(all_filtered_data)

    # 保存到文件
    output_filename = f"filtered_data_{timestamp}.xlsx"
    output_file_path = os.path.join(output_folder_path, output_filename)
    all_filtered_data.to_excel(output_file_path, index=False)

print("处理完成")
