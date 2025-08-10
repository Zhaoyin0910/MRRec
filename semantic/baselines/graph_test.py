import sys

import torch
from transformers import RobertaTokenizer, RobertaModel
import numpy as np
import os
import pandas as pd
from datetime import datetime

# 获取当前脚本所在的绝对路径
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 加载GraphCodeBERT模型和tokenizer（使用绝对路径）
MODEL_PATH = os.path.join(SCRIPT_DIR, "results/checkpoint-3381")
TOKENIZER_PATH = os.path.join(SCRIPT_DIR, "../microsoft/graphcodebert-base")

tokenizer = RobertaTokenizer.from_pretrained(TOKENIZER_PATH)
model = RobertaModel.from_pretrained(MODEL_PATH)

def generate_embedding(code):
    # Tokenize the code
    inputs = tokenizer(code, return_tensors="pt", padding=True, truncation=True)
    # Generate the model's output
    with torch.no_grad():
        outputs = model(**inputs)
    # Extract the embedding for the [CLS] token
    embedding = outputs.last_hidden_state[:, 0, :]
    # Normalize the embedding
    embedding = torch.nn.functional.normalize(embedding, p=2, dim=1)
    return embedding

def similarity(code1, code2):
    embedding1 = generate_embedding(code1)
    embedding2 = generate_embedding(code2)
    similarity = torch.nn.functional.cosine_similarity(embedding1, embedding2)
    similarity_ratio = similarity.item()
    return similarity_ratio

# 批量计算code1文件夹中的代码和code2文件夹中的代码的相似度
def calculate_similarity_between_folders(code1_folder, code2_folder):
    # 获取code1文件夹中的所有文件
    code1_files = [f for f in os.listdir(code1_folder) if os.path.isfile(os.path.join(code1_folder, f))]
    # 获取code2文件夹中的所有文件
    code2_files = [f for f in os.listdir(code2_folder) if os.path.isfile(os.path.join(code2_folder, f))]

    # 遍历code1文件夹中的所有文件
    for file1 in code1_files:
        code1_path = os.path.join(code1_folder, file1)
        code1 = read_code_from_file(code1_path)

        # 存储每个code1文件和所有code2文件的相似度
        similarity_scores = []

        # 对比每个code1文件与code2文件夹中的所有文件
        for file2 in code2_files:
            code2_path = os.path.join(code2_folder, file2)
            code2 = read_code_from_file(code2_path)

            # 计算相似度
            similarity_score = similarity(code1, code2)

            # 保存相似度及文件名
            similarity_scores.append((file1, file2, similarity_score))

            # 打印相似度结果到控制台
            # print(f"Semantic similarity between {file1} and {file2}: {similarity_score:.4f}")

        # 将相似度结果保存到Excel文件
        df = pd.DataFrame(similarity_scores, columns=["Code1 File", "Code2 File", "Similarity Score"])

        # 获取当前时间戳
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # 生成输出文件的路径，文件名带上code1文件名
        # output_folder = './output'  # 确保output文件夹存在
        output_folder = os.path.join(SCRIPT_DIR, 'output')  # 使用绝对路径
        os.makedirs(output_folder, exist_ok=True)  # 创建output文件夹（如果不存在的话）
        output_filename = f"semantic_similarity_scores_{file1}_{timestamp}.csv"
        output_path = os.path.join(output_folder, output_filename)

        # 保存为Excel文件
        df.to_csv(output_path, index=False)

        # print(f"Results for {file1} saved to {output_path}")
        print("保存语义相似检测结果文件路径是"+output_path)
        print("脚本执行完成")
# 从文件读取代码
def read_code_from_file(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            return file.read()
    except UnicodeDecodeError:
        # 如果 utf-8 失败，则尝试 gbk
        with open(file_path, 'r', encoding='gbk') as file:
            return file.read()
    except Exception as e:
        print(f"发生错误: {e}")
        return None


# # 假设code1和code2文件夹的路径
# code1_folder = '../baselines/original'
# code2_folder = '../baselines/candidate'
#
# # 计算相似度并保存结果
# calculate_similarity_between_folders(code1_folder, code2_folder)
def main():
    # 假设code1和code2文件夹的路径
    # code1_folder = '../baselines/original'
    # code2_folder = '../baselines/candidate'
    code1_folder = os.path.join(SCRIPT_DIR, "../baselines/original")
    code2_folder = os.path.join(SCRIPT_DIR, "../baselines/candidate")
    # 计算相似度并保存结果
    calculate_similarity_between_folders(code1_folder, code2_folder)

if __name__ == "__main__":
    main()
    sys.exit(0)