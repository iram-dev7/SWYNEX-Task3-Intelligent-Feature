from textblob import TextBlob

def classify_sentiment(review):
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity

    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

sample_reviews = [
    "This product is amazing, I love it!",
    "Terrible quality, broke in two days.",
    "It's okay, does what it says.",
]

for review in sample_reviews:
    result = classify_sentiment(review)
    print(f"Review: {review}")
    print(f"Sentiment: {result}")
    print()