# -*- coding: utf-8 -*-
"""
Longest Common Subsequence (LCS) Similarity Detection for Java Code

Martinez-Gil, J. (2024). Source Code Clone Detection Using Unsupervised Similarity Measures. arXiv preprint arXiv:2401.09885.

@author: Jorge Martinez-Gil
"""

import os
import difflib
import pandas as pd
import re
from datetime import datetime
import sys

# 获取当前脚本的绝对路径
current_script_path = os.path.abspath(__file__)
current_script_dir = os.path.dirname(current_script_path)
# 定义IR-Plag-Dataset文件夹的路径
# dataset_path = os.path.join(os.getcwd(), "IR-Plag-Dataset")

dataset_path = os.path.abspath(os.path.join(current_script_dir, "IR-Plag-Dataset"))
# 定义一组相似性阈值，用于遍历测试不同的阈值
similarity_thresholds = [0.1,0.2, 0.3, 0.6]


# # 初始化用于跟踪最佳结果的变量
# best_threshold = 0
# best_accuracy = 0
#
# # 初始化统计变量
# TP = 0  # 真阳性：抄袭且被识别为抄袭
# FP = 0  # 假阳性：非抄袭但被识别为抄袭
# FN = 0  # 假阴性：抄袭但被识别为非抄袭
#
# # 创建一个列表用于保存所有的文件对和相似度
# similarity_data = []
#
# # 创建一个集合用于检查文件对是否已经处理过
# processed_pairs = set()

# 去除代码中的注释和空白行
def preprocess_code(code):
    # 去除单行注释
    code = re.sub(r'//.*', '', code)
    # 去除多行注释
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    # 去除空白行
    code = '\n'.join([line for line in code.splitlines() if line.strip() != ''])
    return code



# # 遍历每个相似性阈值并计算准确率
# for SIMILARITY_THRESHOLD in similarity_thresholds:
#     # 初始化每个阈值的统计数据
#     total_cases = 0
#     over_threshold_cases_plagiarized = 0
#     cases_plag = 0
#
#     # 遍历数据集中的每个子文件夹
#     for folder_name in os.listdir(dataset_path):
#         # folder_path = os.path.join(dataset_path, folder_name)
#         folder_path = os.path.abspath(os.path.join(dataset_path, folder_name))
#         if os.path.isdir(folder_path):
#             # 找到原始文件夹中的Java文件
#             # original_path = os.path.join(folder_path, 'original')
#             original_path = os.path.abspath(os.path.join(folder_path, 'original'))
#             # java_files1 = [f for f in os.listdir(original_path) if f.endswith('.java')]
#             # python语言的
#             java_files1 = [f for f in os.listdir(original_path) if f.endswith(('.py','.java'))]
#
#             # 遍历每个原始文件，与plagiarized文件夹中的所有文件进行对比
#             for java_file1 in java_files1:
#                 file1_abs_path = os.path.abspath(os.path.join(original_path, java_file1))
#                 with open(file1_abs_path, 'r', encoding='utf-8') as f:
#                     code1 = f.read()
#
#                 # 预处理代码1：去除注释和空白行
#                 code1 = preprocess_code(code1)
#
#                 # 遍历plagiarized文件夹
#                 plagiarized_path = os.path.join(folder_path, 'plagiarized')
#                 if os.path.isdir(plagiarized_path):
#                     # 遍历子文件夹中的所有Java文件
#                     for root, dirs, files in os.walk(plagiarized_path):
#                         for java_file2 in files:
#                             # if java_file2.endswith('.java'):
#                             # python语言的
#                             if java_file2.endswith('.py'):
#                                 # 生成文件对的唯一标识符
#                                 pair_identifier = (java_file1, java_file2)
#
#                                 # 如果已经处理过这个文件对，则跳过
#                                 if pair_identifier in processed_pairs:
#                                     continue
#
#                                 # 标记这个文件对为已处理
#                                 processed_pairs.add(pair_identifier)
#
#                                 with open(os.path.join(root, java_file2), 'r', encoding='utf-8') as f:
#                                     code2 = f.read()
#
#                                 # 预处理代码2：去除注释和空白行
#                                 code2 = preprocess_code(code2)
#
#                                 # 计算两个代码片段的最长公共子序列（LCS）
#                                 lcs = difflib.SequenceMatcher(None, code1, code2).find_longest_match(0, len(code1),
#                                                                                                          0,
#                                                                                                          len(code2)).size
#                                 similarity_ratio = (2 * lcs) / (len(code1) + len(code2))
#
#                                 # 打印出每对文件的相似度
#                                 print(
#                                     f"Comparing {java_file1} with {java_file2} in plagiarized: Similarity = {similarity_ratio:.2f}")
#
#                                 # 将文件对及相似度保存到列表
#                                 similarity_data.append({
#                                     'Code1': java_file1,
#                                     'Code2': java_file2,
#                                     'Similarity': similarity_ratio,
#                                     'Subfolder': 'plagiarized'
#                                 })
#
#                                 # 根据相似性比率更新计数器
#                                 cases_plag += 1
#                                 if similarity_ratio >= SIMILARITY_THRESHOLD:
#                                     over_threshold_cases_plagiarized += 1
#                                 total_cases += 1
#
#                                 # 根据相似性比率更新统计信息（真阳性、假阳性、假阴性）
#                                 if similarity_ratio >= SIMILARITY_THRESHOLD:
#                                     TP += 1  # 真阳性
#                                 else:
#                                     FN += 1  # 假阴性
#                             if java_file2.endswith('.java'):
#                                 # 生成文件对的唯一标识符
#                                 pair_identifier = (java_file1, java_file2)
#
#                                 # 如果已经处理过这个文件对，则跳过
#                                 if pair_identifier in processed_pairs:
#                                     continue
#
#                                 # 标记这个文件对为已处理
#                                 processed_pairs.add(pair_identifier)
#
#                                 file2_abs_path = os.path.abspath(os.path.join(root, java_file2))
#                                 with open(file2_abs_path, 'r', encoding='utf-8') as f:
#                                     code2 = f.read()
#
#                                 # 预处理代码2：去除注释和空白行
#                                 code2 = preprocess_code(code2)
#
#                                 # 计算两个代码片段的最长公共子序列（LCS）
#                                 lcs = difflib.SequenceMatcher(None, code1, code2).find_longest_match(0, len(code1),
#                                                                                                      0,
#                                                                                                      len(code2)).size
#                                 similarity_ratio = (2 * lcs) / (len(code1) + len(code2))
#
#                                 # 打印出每对文件的相似度
#                                 print(
#                                     f"Comparing {java_file1} with {java_file2} in plagiarized: Similarity = {similarity_ratio:.2f}")
#
#                                 # 将文件对及相似度保存到列表
#                                 similarity_data.append({
#                                     'Code1': java_file1,
#                                     'Code2': java_file2,
#                                     'Similarity': similarity_ratio,
#                                     'Subfolder': 'plagiarized'
#                                 })
#
#                                 # 根据相似性比率更新计数器
#                                 cases_plag += 1
#                                 if similarity_ratio >= SIMILARITY_THRESHOLD:
#                                     over_threshold_cases_plagiarized += 1
#                                 total_cases += 1
#
#                                 # 根据相似性比率更新统计信息（真阳性、假阳性、假阴性）
#                                 if similarity_ratio >= SIMILARITY_THRESHOLD:
#                                     TP += 1  # 真阳性
#                                 else:
#                                     FN += 1  # 假阴性
#
#     # 计算当前阈值的准确率
#     if total_cases > 0:
#         accuracy = over_threshold_cases_plagiarized / total_cases
#         if accuracy > best_accuracy:
#             best_accuracy = accuracy
#             best_threshold = SIMILARITY_THRESHOLD
#
#     # 计算精度和召回率
#     if TP + FP > 0:
#         precision = TP / (TP + FP)
#     else:
#         precision = 0
#
#     if TP + FN > 0:
#         recall = TP / (TP + FN)
#     else:
#         recall = 0
#
#     # 计算F-measure
#     if precision + recall > 0:
#         f_measure = 2 * (precision * recall) / (precision + recall)
#     else:
#         f_measure = 0
#
# # 创建带时间戳的Excel文件名
# timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
# excel_filename = f"similarity_results_{timestamp}.xlsx"
#
# # 将数据保存到Excel
# df = pd.DataFrame(similarity_data)
#
# # 删除最后一列（Subfolder列）
# df = df.iloc[:, :-1]
#
# # 新增：去除Code1和Code2顺序相反的重复行
# # 生成排序后的文件对标识
# df['sorted_pair'] = df.apply(lambda x: tuple(sorted([x['Code1'], x['Code2']])), axis=1)
# # 保留每个文件对的第一个出现
# df = df.drop_duplicates(subset='sorted_pair', keep='first')
# # 删除临时列
# df = df.drop(columns=['sorted_pair'])
#
# # 创建结果目录，如果不存在
# # results_directory = os.path.join(os.getcwd(), 'Results')
# results_directory = os.path.join(os.getcwd(), 'Results')
# if not os.path.exists(results_directory):
#     os.makedirs(results_directory)
#
# # 保存到Results目录
# # excel_filepath = os.path.join(results_directory, excel_filename)
# excel_filepath = os.path.abspath(os.path.join(results_directory, excel_filename))
# df.to_excel(excel_filepath, index=False, engine='openpyxl')
#
# # 输出最佳阈值和准确率
# print(
#     f"{os.path.basename(__file__)} - The best threshold is {best_threshold} with an accuracy of {best_accuracy:.2f}, Precision: {precision:.2f}, Recall: {recall:.2f}, F-measure: {f_measure:.2f}")
def main():
    # 初始化用于跟踪最佳结果的变量
    best_threshold = 0
    best_accuracy = 0

    # 初始化统计变量
    TP = 0  # 真阳性：抄袭且被识别为抄袭
    FP = 0  # 假阳性：非抄袭但被识别为抄袭
    FN = 0  # 假阴性：抄袭但被识别为非抄袭

    # 创建一个列表用于保存所有的文件对和相似度
    similarity_data = []

    # 创建一个集合用于检查文件对是否已经处理过
    processed_pairs = set()

    # 遍历每个相似性阈值并计算准确率
    for SIMILARITY_THRESHOLD in similarity_thresholds:
        # 初始化每个阈值的统计数据
        total_cases = 0
        over_threshold_cases_plagiarized = 0
        cases_plag = 0

        # 遍历数据集中的每个子文件夹
        for folder_name in os.listdir(dataset_path):
            folder_path = os.path.abspath(os.path.join(dataset_path, folder_name))
            if os.path.isdir(folder_path):
                # 找到原始文件夹中的Java文件
                original_path = os.path.abspath(os.path.join(folder_path, 'original'))
                java_files1 = [f for f in os.listdir(original_path) if f.endswith(('.py','.java'))]

                # 遍历每个原始文件，与plagiarized文件夹中的所有文件进行对比
                for java_file1 in java_files1:
                    file1_abs_path = os.path.abspath(os.path.join(original_path, java_file1))
                    with open(file1_abs_path, 'r', encoding='utf-8') as f:
                        code1 = f.read()

                    # 预处理代码1：去除注释和空白行
                    code1 = preprocess_code(code1)

                    # 遍历plagiarized文件夹
                    plagiarized_path = os.path.join(folder_path, 'candidate')
                    if os.path.isdir(plagiarized_path):
                        # 遍历子文件夹中的所有Java文件
                        for root, dirs, files in os.walk(plagiarized_path):
                            for java_file2 in files:
                                if java_file2.endswith('.py'):
                                    # 生成文件对的唯一标识符
                                    pair_identifier = (java_file1, java_file2)

                                    # 如果已经处理过这个文件对，则跳过
                                    if pair_identifier in processed_pairs:
                                        continue

                                    # 标记这个文件对为已处理
                                    processed_pairs.add(pair_identifier)

                                    with open(os.path.join(root, java_file2), 'r', encoding='utf-8') as f:
                                        code2 = f.read()

                                    # 预处理代码2：去除注释和空白行
                                    code2 = preprocess_code(code2)

                                    # 计算两个代码片段的最长公共子序列（LCS）
                                    lcs = difflib.SequenceMatcher(None, code1, code2).find_longest_match(0, len(code1),
                                                                                                             0,
                                                                                                             len(code2)).size
                                    similarity_ratio = (2 * lcs) / (len(code1) + len(code2))

                                    # 打印出每对文件的相似度
                                    # print(
                                    #     f"Comparing {java_file1} with {java_file2} in plagiarized: Similarity = {similarity_ratio:.2f}")

                                    # 将文件对及相似度保存到列表
                                    similarity_data.append({
                                        'Code1': java_file1,
                                        'Code2': java_file2,
                                        'Similarity': similarity_ratio,
                                        'Subfolder': 'plagiarized'
                                    })

                                    # 根据相似性比率更新计数器
                                    cases_plag += 1
                                    if similarity_ratio >= SIMILARITY_THRESHOLD:
                                        over_threshold_cases_plagiarized += 1
                                    total_cases += 1

                                    # 根据相似性比率更新统计信息（真阳性、假阳性、假阴性）
                                    if similarity_ratio >= SIMILARITY_THRESHOLD:
                                        TP += 1  # 真阳性
                                    else:
                                        FN += 1  # 假阴性
                                if java_file2.endswith('.java'):
                                    # 生成文件对的唯一标识符
                                    pair_identifier = (java_file1, java_file2)

                                    # 如果已经处理过这个文件对，则跳过
                                    if pair_identifier in processed_pairs:
                                        continue

                                    # 标记这个文件对为已处理
                                    processed_pairs.add(pair_identifier)

                                    file2_abs_path = os.path.abspath(os.path.join(root, java_file2))
                                    with open(file2_abs_path, 'r', encoding='utf-8') as f:
                                        code2 = f.read()

                                    # 预处理代码2：去除注释和空白行
                                    code2 = preprocess_code(code2)

                                    # 计算两个代码片段的最长公共子序列（LCS）
                                    lcs = difflib.SequenceMatcher(None, code1, code2).find_longest_match(0, len(code1),
                                                                                                         0,
                                                                                                         len(code2)).size
                                    similarity_ratio = (2 * lcs) / (len(code1) + len(code2))

                                    # 打印出每对文件的相似度
                                    # print(
                                    #     f"Comparing {java_file1} with {java_file2} in plagiarized: Similarity = {similarity_ratio:.2f}")

                                    # 将文件对及相似度保存到列表
                                    similarity_data.append({
                                        'Code1': java_file1,
                                        'Code2': java_file2,
                                        'Similarity': similarity_ratio,
                                        'Subfolder': 'plagiarized'
                                    })

                                    # 根据相似性比率更新计数器
                                    cases_plag += 1
                                    if similarity_ratio >= SIMILARITY_THRESHOLD:
                                        over_threshold_cases_plagiarized += 1
                                    total_cases += 1

                                    # 根据相似性比率更新统计信息（真阳性、假阳性、假阴性）
                                    if similarity_ratio >= SIMILARITY_THRESHOLD:
                                        TP += 1  # 真阳性
                                    else:
                                        FN += 1  # 假阴性

        # 计算当前阈值的准确率
        if total_cases > 0:
            accuracy = over_threshold_cases_plagiarized / total_cases
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_threshold = SIMILARITY_THRESHOLD

    # 计算精度和召回率
    if TP + FP > 0:
        precision = TP / (TP + FP)
    else:
        precision = 0

    if TP + FN > 0:
        recall = TP / (TP + FN)
    else:
        recall = 0

    # 计算F-measure
    if precision + recall > 0:
        f_measure = 2 * (precision * recall) / (precision + recall)
    else:
        f_measure = 0

    # 创建带时间戳的Excel文件名
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    excel_filename = f"similarity_results_{timestamp}.csv"

    # 将数据保存到Excel
    df = pd.DataFrame(similarity_data)

    # 删除最后一列（Subfolder列）
    df = df.iloc[:, :-1]

    # 新增：去除Code1和Code2顺序相反的重复行
    df['sorted_pair'] = df.apply(lambda x: tuple(sorted([x['Code1'], x['Code2']])), axis=1)
    df = df.drop_duplicates(subset='sorted_pair', keep='first')
    df = df.drop(columns=['sorted_pair'])

    # 创建结果目录，如果不存在
    results_directory = os.path.abspath(os.path.join(os.getcwd(), 'Results'))
    results_directory = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Results'))
    # print(results_directory)
    if not os.path.exists(results_directory):
        os.makedirs(results_directory)

    # 保存到Results目录
    excel_filepath = os.path.abspath(os.path.join(results_directory, excel_filename))
    print("保存语法相似检测结果文件路径是"+excel_filepath)
    print("脚本执行完成")
    df.to_csv(excel_filepath, index=False, encoding='utf-8')
    # df.to_csv(excel_filepath, index=False, encoding='utf-8')

    # 输出最佳阈值和准确率
    # print(
    #     f"{os.path.basename(__file__)} - The best threshold is {best_threshold} with an accuracy of {best_accuracy:.2f}, Precision: {precision:.2f}, Recall: {recall:.2f}, F-measure: {f_measure:.2f}")
if __name__ == "__main__":
    main()
    sys.exit(0)