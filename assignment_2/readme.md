# Documentation and Report: Nepali News Articles Classification Project using Transformer model

## Overview

This project focuses on classifying Nepali news articles using a machine learning and deep learning pipeline. The dataset contains approximately 7,500 Nepali news articles collected from various online news platforms. The dataset has been preprocessed, cleaned, and divided into a balanced training and validation set, allowing for the development and evaluation of text classification models.

## Objectives

- To build and train machine learning models for classifying Nepali news articles.
- To preprocess and encode text data effectively for model input.
- To utilize transformers for advanced natural language processing.

## Dataset

### Description

- **Size:** ~7,500 news articles.
- **Source:** Nepali news websites.
- **Structure:** Pre-divided into training and validation sets.
- **Link:** https://www.kaggle.com/datasets/disisbig/nepali-news-dataset

### Dataset Files

- train.csv: Contains the training data.
- valid.csv: Contains the validation data.
- Test.csv: Contains the test data

## Notebook Workflow

### 1\. Data Loading

The dataset is loaded using the following paths:

```
train_path = 'data/archive (4)/train.csv'

valid_path = 'data/archive (4)/valid.csv'
```

Pandas are used to read these files into data frames for further processing.

### 2\. Data Preprocessing

- **Label Encoding:** **LabelEncoder** from **sklearn** is used to convert textual labels into numerical format suitable for machine learning models:

```
labels = label_encoder.fit_transform(labels)

valid_labels = valid_label_encoder.fit_transform(labels)
````

### 3\. Tokenization

- Tokenization is performed using the **AutoTokenizer** module from the **transformers** library to handle Nepali text efficiently.

### 4\. Architecture

The **CustomTransformerClassifier** is a Transformer-based model for classification with the following architecture:

* **Embedding Layer:** Maps 119,547 tokens into 768-dimensional vectors.

* **Encoder:** A stack of 6 TransformerEncoderLayer blocks, each with:

* **Multi-head Attention (768-dim)**

* **Feedforward Network (FFN):** Linear → ReLU → Linear (768 → 2048 → 768)

* **Layer Normalization** (pre/post-attention and FFN)

* **Dropout (0.1)** after attention and FFN

* **Final Dropout:** 0.3 before the output.

* **Fully Connected Layer:** Projects 768 to 3 output classes.

* **Dropout (0.3)** before classification output.

This model is suitable for text classification with 3 target classes.

## Key Libraries Used

- **Pandas:** For data manipulation and analysis.
- **sklearn:** For preprocessing operations, including label encoding.
- **transformers:** For tokenizing and handling text data.
- **Torch:** For building and training machine learning models.

## Conclusion

This project demonstrates the application of natural language processing techniques for classifying Nepali news articles. With a well-structured dataset and appropriate tools, it can be extended to other NLP tasks like sentiment analysis and text summarization.
