# importing a transformers library for text summarization
from transformers import pipeline

# Create the summarization pipeline
summarize_text = pipeline("summarization")

# Take user input
user_input = input("Please enter a paragraph that you want summarized:\n\n")

# Generate summary with custom parameters
result = summarize_text(
    user_input,
    max_length=30,
    min_length=30,
    do_sample=False
)

# For displaying a summary to the user
print("\n Generated Summary:\n")
print(result[0]['summary_text'])
