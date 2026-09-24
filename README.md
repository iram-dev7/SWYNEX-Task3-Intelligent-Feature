# SWYNEX Task 2 - Model/API Integration

## What this does
A simple sentiment classifier built using the TextBlob Python library. It takes a product review as text input and classifies it as Positive, Negative, or Neutral based on sentiment polarity.

## How it works
- The script analyzes the polarity score of each review using TextBlob
- Polarity > 0.1 → Positive
- Polarity < -0.1 → Negative
- Otherwise → Neutral

## How to run
1. pip3 install textblob
2. python3 -m textblob.download_corpora
3. python3 sentimental_classifier.py

## Example Input/Output
Input: "This product is amazing, I love it!"
Output: Positive

Input: "Terrible quality, broke in two days."
Output: Negative

Input: "It's okay, does what it says."
Output: Neutral