# CODTECH Internship - Task 4
# Sentiment Analysis using NLP
# Done using Notepad + Python

from textblob import TextBlob

# Sample textual data (reviews/tweets)
texts = [
    "I love this product. It is amazing!",
    "This is the worst experience I have ever had.",
    "The service was okay, not great but not bad.",
    "Absolutely fantastic! Highly recommended.",
    "I am very disappointed with the quality."
]

print("SENTIMENT ANALYSIS RESULTS\n")

# Analyze sentiment
for text in texts:
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    print("Text:", text)
    print("Polarity:", polarity)
    print("Sentiment:", sentiment)
    print("-" * 50)
