from transformers import pipeline

summarizer = pipeline("summarization")

text = input("Enter the text to be summarized:\n\n")

summary = summarizer(text, max_length=30, min_length=30, do_sample=False)

print("\nSummary:\n", summary[0]['summary_text'])