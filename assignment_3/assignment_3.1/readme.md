# RAG Pipeline Utility - README

## Overview

`rag_utils.py` provides core utilities to build a **Retrieval-Augmented Generation (RAG)** pipeline combining:

- **Tavily API** for site-specific content search (acting as a crawler)
- **Sentence Transformers** for embedding textual chunks
- **FAISS** for vector similarity search and indexing
- **Groq (xAI) API** as the Large Language Model (LLM) for answer generation
- **TriviaQA** dataset for evaluation

This module enables ingestion of domain-specific knowledge from websites, retrieval of relevant context, and generation of answers augmented with retrieved content.

---

## Features

- **Crawl and search website content** using Tavily API with domain restrictions
- **Chunk large documents** into smaller text pieces suitable for embedding
- **Generate semantic embeddings** with a pre-trained SentenceTransformer
- **Store and search embeddings** efficiently with FAISS vector store
- **Generate answers** to questions using Groq LLM with retrieved context
- **Evaluate** pipeline performance on TriviaQA benchmark dataset

---

## Setup

### 1. Install dependencies

```bash
pip install requests numpy faiss-cpu sentence-transformers datasets python-dotenv groq
```

---
# 2. Environment variables
Create a .env file in your project root with the following keys:

```
TAVILY_API_KEY=your_tavily_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```
The module uses python-dotenv to load these keys.

## Module Breakdown
### 1. search_tavily(query, site=None, num_results=5)
Searches the web using Tavily API, optionally restricted to a specific domain.

Returns a list of textual contents/snippets.

### 2. chunk_text(text, max_tokens=200)
Splits large text into smaller chunks based on token count limit.

Useful for embedding models with input size constraints.

### 3. build_vector_store(chunks)
Converts text chunks to embeddings using all-MiniLM-L6-v2.

Builds a FAISS index for fast similarity search.

### 4. query_grok(prompt)
Sends the prompt to Groq (xAI) LLM API and returns generated response.

Uses the groq Python client initialized with your API key.

Currently set with system instructions for Python code generation, can be modified.

### 5. retrieve(query, index, chunks)
Encodes query, searches FAISS index for top 3 relevant chunks.

Returns the textual chunks for downstream use.

### 6. generate_answer(query)
Retrieves relevant context for query.

Constructs a prompt combining context and question.

Gets answer from Groq LLM.

### 7. evaluate_rag()
Evaluates pipeline on a sample of TriviaQA validation set.

Computes simple accuracy based on normalized text matching.

### 8. ingest(seed_queries, site)
Performs domain-specific ingestion by searching seed queries via Tavily.

Chunks and indexes retrieved documents into FAISS vector store.

Updates global index and chunk storage.