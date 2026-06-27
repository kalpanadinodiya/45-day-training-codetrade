# LLM Assignment

## Overview

This project demonstrates the practical implementation of Large Language Model (LLM) applications using the Google Gemini API and OpenRouter API.

The assignment includes:

* Multi LLM Response Comparison
* Prompt Engineering Playground
* Streaming AI Chat Assistant
* Token Usage and Cost Tracker

---

## Technologies Used

* Python
* Google Gemini API
* OpenRouter API
* Pandas
* Requests
* google-genai

---

# Task 1 – Multi LLM Response Comparison

## Objective

Compare responses from two different LLM providers for the same prompt.

## LLM Providers

* Google Gemini
* OpenRouter

## Features

* Send the same prompt to both models
* Measure response time
* Measure response length
* Save comparison results to `results.csv`

## Output

* `results.csv`
* Console output showing responses from both models

---

# Task 2 – Prompt Engineering Playground

## Objective

Compare different prompts for the same text summarization task.

## Use Case

Text Summarization

## Prompts Tested

1. One sentence summary
2. Three bullet points
3. Simple language explanation
4. Summary for a 10-year-old
5. Professional summary

## Features

* Test five different prompts
* Compare Gemini and OpenRouter responses
* Save all responses to `task2_results.csv`
* Identify the best prompt

## Best Prompt

Prompt 5 – Professional Summary

## Reason

It produced the most clear, structured, and informative summary.

---

# Task 3 – Streaming AI Chat Assistant

## Objective

Build an interactive chatbot using Gemini API with streaming responses.

## Features

* Interactive chatbot
* Chat history
* Streaming responses
* Exit command

## Output

Real-time streaming AI chatbot in the terminal.

---

# Task 4 – Token Usage and Cost Tracker

## Objective

Track prompt text, response text, estimated token usage, and estimated API cost.

## Features

* Log prompts and responses
* Estimate token usage
* Estimate API cost
* Save logs to `token_usage_log.csv`
* Generate final usage report

---

# Project Structure

```text
llm_assignment/
│── app.py
│── task2.py
│── task3.py
│── task4.py
│── config.py
│── prompts.csv
│── results.csv
│── task2_results.csv
│── token_usage_log.csv
│── requirements.txt
│── README.md
│── .gitignore
```

---

# How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Task 1:

```bash
python app.py
```

Run Task 2:

```bash
python task2.py
```

Run Task 3:

```bash
python task3.py
```

Run Task 4:

```bash
python task4.py
```

---

# Outputs

* Multi LLM comparison
* Prompt engineering results
* Streaming chatbot
* Token usage report

---

# Author

Kalpana Dinodiya
