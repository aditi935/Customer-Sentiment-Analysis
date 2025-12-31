from flask import Flask, render_template, request
import pandas as pd
from utils.sentiment import analyze_sentiment
from utils.text_processing import most_common_words
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    df = pd.read_csv(file)

    if 'review_text' not in df.columns:
        return "CSV must contain 'review_text' column"

    df['sentiment'] = df['review_text'].apply(analyze_sentiment)

    sentiment_counts = df['sentiment'].value_counts()

    plt.figure(figsize=(7, 7))
    
    # Define custom colors: green for Positive, yellow for Neutral, red for Negative
    colors = []
    for label in sentiment_counts.index:
        if label == 'Positive':
            colors.append('#10B981')  # Green
        elif label == 'Neutral':
            colors.append('#FBBF24')  # Yellow
        elif label == 'Negative':
            colors.append('#EF4444')  # Red
    
    plt.pie(
        sentiment_counts.values,
        labels=sentiment_counts.index,
        colors=colors,  # Add colors parameter
        autopct='%1.1f%%',
        startangle=140
    )
    
    plt.axis('equal')

    if not os.path.exists("static"):
        os.makedirs("static")

    plt.savefig("static/sentiment_chart.png", bbox_inches="tight")
    plt.close()

    positive_reviews = df[df['sentiment'] == 'Positive']['review_text']
    negative_reviews = df[df['sentiment'] == 'Negative']['review_text']
    neutral_reviews = df[df['sentiment'] == 'Neutral']['review_text']

    common_positive = most_common_words(positive_reviews)
    common_negative = most_common_words(negative_reviews)
    common_neutral = most_common_words(neutral_reviews)

    return render_template(
        'dashboard.html',
        tables=df.to_dict(orient='records'),
        sentiment_counts=sentiment_counts,
        common_positive=common_positive,
        common_negative=common_negative,
        common_neutral=common_neutral  
    )

if __name__ == '__main__':
    app.run(debug=True)