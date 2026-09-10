# Sentiment-Enhanced Summarization

**Abstractive text summarization** improved by injecting sentiment signals into the model's attention — higher-quality summaries for opinion-heavy text.

## Overview
This project implements a sentiment-aware abstractive summarization model that enhances summary quality for opinion-heavy documents by explicitly incorporating sentiment signals into the attention mechanism.

## Challenge
- **Injecting sentiment signals without degrading summary fluency**: Balancing sentiment preservation with grammatical coherence and factual accuracy

## Stack
- `PyTorch`
- `NLP`
- `Attention`

## Approach
1. **Sentiment encoding**: Pre-trained sentiment classifier extracts sentiment vectors from source text
2. **Attention injection**: Sentiment vectors injected into the decoder's cross-attention layers
3. **Training**: End-to-end training on opinion-heavy datasets (product reviews, editorials)
4. **Evaluation**: ROUGE scores + human evaluation for sentiment preservation

## Results
See [Final Project Paper](Final_Project_Piotr_Parkitny.pdf) for architecture details, quantitative results, and qualitative examples.

## Artifacts
- `Final_Project_Piotr_Parkitny.pdf` — Full paper
- `pics/img1.png` — Architecture diagram
- `pics/img2.png` — Qualitative examples