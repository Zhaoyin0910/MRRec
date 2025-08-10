# A Metamorphic Relation Identification Method Based on Program Similarity

## 📄 Overview

This method leverages **program similarity** (syntactic similarity and semantic similarity) to recommend existing Metamorphic Relations (MR) for new programs, thereby reducing the cost of MR identification and improving efficiency.  
- **Syntactic similarity** → Measures code structural similarity based on the Longest Common Subsequence (LCS) algorithm  
- **Semantic similarity** → Measures code functional similarity based on GraphCodeBERT  
- Experiments on the **MetBench** and **LeetCode** datasets demonstrate that syntactic and semantic similarities are complementary in MR identification.

## 📂 Project Structure

### Syntactic Similarity Module

 ```
syntax/                        # Syntactic similarity computation module
├── main.py                    # Entry point for syntactic similarity computation
├── java-sim-lcs-opt.py        # LCS algorithm implementation
├── IR-Plag-Dataset/           # Candidate program samples
├── Results/                   # Results from syntactic similarity computation
└── ...                        # Other auxiliary files and directories
 ```

### Semantic Similarity Module

 ```
semantic/                      # Semantic similarity computation module
├── baselines/                 # Basic scripts and data processing
│   ├── data_select.py         # Data cleaning script
│   ├── graph_test.py          # Entry point for semantic similarity computation
│   └── data/                  # Candidate program samples
├── microsoft/                 # GraphCodeBERT model
└── ...                        # Other auxiliary files and directories
 ```

## 🛠 Environment Requirements

### General
- Python 3.8+
- pip (latest version)

### Syntactic Similarity Module
- Python libraries: os, subprocess, time, threading, difflib, re, datetime, sys, pandas

### Semantic Similarity Module
- torch == 2.0.1
- transformers == 4.31.0 (RobertaTokenizer, RobertaModel)  
- Python libraries: os, time, datetime, pandas, numpy
