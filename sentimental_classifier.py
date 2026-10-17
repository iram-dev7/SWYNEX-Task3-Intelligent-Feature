from textblob import TextBlob

def classify_sentiment(review):
    if not review or not review.strip():
        return "Error: Empty input, please enter a review."

    try:
        analysis = TextBlob(review)
        polarity = analysis.sentiment.polarity

        if polarity > 0.1:
            return "Positive"
        elif polarity < -0.1:
            return "Negative"
        else:
            return "Neutral"
    except Exception as e:
        return f"Error: Could not analyze input ({e})"


# ---- Evaluation examples (known cases) ----
evaluation_examples = [
    ("This product is amazing, I love it!", "Positive"),
    ("Terrible quality, broke in two days.", "Negative"),
    ("It's okay, does what it says.", "Neutral"),
    ("Best purchase ever, highly recommend!", "Positive"),
    ("Waste of money, do not buy.", "Negative"),
]

print("=== Evaluation ===")
correct = 0
for review, expected in evaluation_examples:
    result = classify_sentiment(review)
    status = "Correct" if result == expected else "Incorrect"
    if result == expected:
        correct += 1
    print(f"Review: {review}")
    print(f"Expected: {expected} | Got: {result} | {status}\n")

accuracy = (correct / len(evaluation_examples)) * 100
print(f"Accuracy: {accuracy:.1f}%\n")


# ---- Known failure cases (model limitations) ----
failure_cases = [
    "Not bad at all!",            # sarcasm/negation confuses simple models
    "This is sick!",              # slang - "sick" can mean great
    "",                           # empty input (tests error handling)
]

print("=== Failure Cases (Model Limitations) ===")
for review in failure_cases:
    result = classify_sentiment(review)
    print(f"Review: '{review}' -> Result: {result}")
print()


# ---- Simple interactive interface ----
print("=== Try it yourself ===")
print("Type a review to classify it, or type 'exit' to quit.\n")

while True:
    user_input = input("Enter a review: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    result = classify_sentiment(user_input)
    print(f"Sentiment: {result}\n")
    