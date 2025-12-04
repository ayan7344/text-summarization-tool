# text-summarization-tool
*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: AYAN AHMAD KHAN 

*INTER ID*: CT06DR1818

*DOMAIN*: ARTIFICIAL INTELLIGENCE

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTOSH
# Text Summarization Tool

## 📌 Introduction

This project was developed as part of my AI internship, where Task 1 focused on creating a **Text Summarization Tool** using a pretrained NLP model. The goal was to transform lengthy paragraphs into short, meaningful summaries. This task helped me understand how modern Transformer-based AI models interpret and compress natural language.

All development work was completed on my **MacBook Air**, and this document highlights the tools, setup, technologies, and workflow I followed throughout the project.

---

## 🧠 Task Objective

The internship task required building a summarizer by:

* Using a pretrained model from **HuggingFace**
* Loading the model through Python code
* Accepting user input through the terminal
* Configuring parameters like `max_length`, `min_length`, and `do_sample`
* Displaying both the original and summarized text
* Running the program locally on a computer
* Following proper and clean coding structure

The purpose was to gain hands-on experience with NLP pipelines and understand how Transformer models work under the hood.

---

## 🛠️ Tools & Libraries

### **Programming Language**

* **Python 3.14** — Widely used in machine learning and AI-based applications.

### **Libraries Used**

* **Transformers (HuggingFace)**
  Makes it easy to load state-of-the-art models with simple commands such as:
  `pipeline("summarization")`

* **SentencePiece**
  Tokenizer commonly used for models like T5 and BART.

* **PyTorch**
  Works as the backend for many Transformer models.

---

## 💻 Development Environment

### **Device**

* **MacBook Air (macOS)** — Entire development and testing were done on macOS.

### **Terminal**

Used for:

* Installing Python packages
* Running scripts
* Debugging

### **Code Editor**

* **Visual Studio Code (VS Code)** — Lightweight and ideal for AI scripting. Files like `text_summarizer.py` were written here.

---

## 🔧 Installation Instructions

### 1. Install pip3 (already included in macOS Python)

### 2. Install required libraries

```bash
pip3 install transformers
pip3 install sentencepiece
```

PyTorch gets automatically installed when running the model, but it can also be installed manually if needed.

---

## 🚀 How the Program Works

1. Import the summarizer:

   ```python
   from transformers import pipeline
   ```
2. Load the pretrained model:

   ```python
   summarizer = pipeline("summarization")
   ```
3. Ask the user for a paragraph:

   ```python
   text = input("Enter your paragraph:\n\n")
   ```
4. Generate the summary:

   ```python
   summary = summarizer(text, max_length=60, min_length=20, do_sample=False)
   ```
5. Print the summarized output.

This creates a simple and user-friendly summarization tool.

---

## 📍 Applications

This summarizer can be useful for:

* Condensing news articles
* Creating short study notes
* Summarizing PDF documents
* Blog or content summarization
* Research paper previews
* Educational tools
* Basic chatbot integration

It runs smoothly even on systems without a GPU.

---

## 🎯 Learning Outcome

From this task, I gained knowledge about:

* Python basics
* How pretrained Transformer models function
* HuggingFace pipelines and tokenization
* How summarization algorithms compress long content
* Installing and managing Python libraries on macOS
* Executing Python scripts using Terminal
* How AI models process text from input to output

This task gave me a strong foundation in NLP and practical AI development on macOS.

---

## ✅ Conclusion

Building this Text Summarization Tool was an excellent introduction to real-world NLP workflows. It showcased how quickly powerful AI capabilities can be implemented using modern frameworks like HuggingFace Transformers.

---

# Alternate README — Text Summarization Tool (Based on Updated Code)

## 📌 Introduction

This README explains the development of a **Text Summarization Tool** created as part of my AI internship. The goal of the task was to build a simple Python-based summarizer using a pretrained Transformer model from HuggingFace. The tool converts long paragraphs into short, meaningful summaries.

This README is based on an updated version of the summarization code, rewritten in a cleaner and more structured format while keeping the core logic the same.

---

## 🧠 Task Overview

For this internship task, I was required to:

* Use a pretrained model from **HuggingFace Transformers**
* Load the summarization pipeline in Python
* Accept paragraph input from the user
* Set summarization parameters like `max_length`, `min_length`, and `do_sample`
* Print the generated summary in the terminal
* Build clean, readable, and professional Python code

The main purpose was to understand how Transformer-based NLP models work and how to integrate them into simple applications.

---

## 🛠 Tools & Technologies Used

### **Programming Language**

* **Python 3.14** — A flexible, widely used language in AI and NLP tasks.

### **Libraries Used**

* **Transformers** — To load NLP models through the `pipeline()` function.
* **SentencePiece** — Tokenizer support for models such as T5 and BART.
* **PyTorch** — Deep learning backend used by the model.

### **Development Environment**

* **Device**: MacBook Air (macOS)
* **Terminal**: Used for installing libraries and running scripts.
* **Code Editor**: Visual Studio Code (VS Code)

---

## 🔧 Installation Steps

Install the required libraries using pip3:

```bash
pip3 install transformers
pip3 install sentencepiece
```

> Note: PyTorch may install automatically when running the script, but it can also be installed manually if needed.

---

## 🚀 Updated Code Explanation

The updated code keeps the same summarization logic but with improved structure and variable names:

```python
from transformers import pipeline

# Create the summarization pipeline
summarize_text = pipeline("summarization")

# Take user input\ nuser_input = input("Please enter a paragraph that you want summarized:\n\n")

# Generate summary with custom parameters
result = summarize_text(
    user_input,
    max_length=30,
    min_length=30,
    do_sample=False
)

# Display summary to the user
print("\n🔍 Generated Summary:\n")
print(result[0]['summary_text'])
```

### ✔ What’s Different in This Version?

* Cleaner code formatting
* Improved naming: `summarize_text`, `user_input`, `result`
* Better user prompt
* Enhanced display formatting
* More readable and structured workflow

---

## 📍 Applications of This Tool

This text summarizer can be used for:

* News article condensation
* Academic notes
* Research summaries
* PDF or document shortening
* Blog and content optimization
* AI assistant integrations
* Writing and editing tools

## 🎯 What I Learned From This Task

Throughout this project, I learned:

* How pretrained NLP models work in HuggingFace
* How to use the `pipeline()` function efficiently
* How summarization algorithms simplify long text
* Basics of Python scripting and terminal usage
* How to manage and install Python libraries on macOS
* How AI models tokenize and generate text outputs

This task strengthened my understanding of core NLP concepts and gave me hands-on experience with practical AI development.

---

## ✅ Final Thoughts

This updated approach to the summarizer code helped me understand clean coding practices while still using powerful AI models. The project demonstrates how easily modern NLP tools can be integrated into simple Python scripts.

---
