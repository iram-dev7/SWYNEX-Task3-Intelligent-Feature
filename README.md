# SWYNEX Task 3 - Intelligent Feature

## What this does
An improved sentiment classifier built using the TextBlob Python library. It takes a product review as input and classifies it as Positive, Negative, or Neutral. This version adds evaluation metrics, documented failure cases, error handling, and a live interactive interface.

## How it works
- The script analyzes the polarity score of each review using TextBlob
- Polarity > 0.1 → Positive
- Polarity < -0.1 → Negative
- Otherwise → Neutral

## How to run
1. pip3 install textblob
2. python3 -m textblob.download_corpora
3. python3 sentimental_classifier.py

## Evaluation
The script tests itself against 5 labeled example reviews and prints an accuracy score.
Current accuracy: **80%** (4 out of 5 correctly classified)

## Known Failure Cases (Model Limitations)
This simple model struggles with:
- **Negation/sarcasm**: "Not bad at all!" → incorrectly classified as Positive
- **Slang**: "This is sick!" → incorrectly classified as Negative (slang meaning "great" confuses it)
- **Empty input**: handled gracefully with an error message instead of crashing

## Interactive Mode
After running the script, you can type your own review and get a live sentiment classification. Type 'exit' to quit.

## Example Input/Output
Input: "This product is amazing, I love it!"
Output: Positive

Input: "Terrible quality, broke in two days."
Output: Negative

Input: "It's okay, does what it says."
Output: Neutral (model sometimes misclassifies neutral reviews as Positive — a known limitation)