📊 Flask-Based Customer Review Sentiment Analysis Web Application 🧠📈

A Flask-powered NLP web application that accepts customer reviews via
CSV upload, analyzes sentiment using traditional Natural Language
Processing techniques, and presents clear insights through charts,
metrics, and filters.

This project focuses on interpretable sentiment analysis using NLTK and
TextBlob, strictly avoiding deep learning models, making it lightweight,
fast, and easy to understand.

🧩 What is this Flask Web Application?

This application allows businesses or analysts to understand customer
feedback at scale by:

-   Uploading customer reviews in CSV format
-   Automatically classifying each review as Positive, Neutral, or
    Negative
-   Displaying insights through a dashboard with charts and word
    analysis
-   Allowing users to filter reviews by sentiment and view individual
    review details

🔹 The backend is built using Flask, while the frontend uses HTML, CSS,
and Jinja templates for dynamic rendering.

🚀 Why Use This Application?

🔹 Problem with Manual Review Analysis\
- Time-consuming to read thousands of reviews\
- Difficult to identify overall customer sentiment\
- No clear visualization of feedback trends

🔹 How This Application Helps\
- 🧠 Automatically understands sentiment\
- 📊 Visualizes feedback trends clearly\
- 🔍 Highlights frequently used positive & negative words\
- ⚡ Fast, lightweight, and easy to deploy

🖼️ Application Screenshots\
🔹 Frontend -- CSV Upload Page\
![Frontend Page](images/frontpage.png)

🔹 Dashboard -- Sentiment Insights\
![Dashboard Page](images/dashboard.png)

✨ Key Features

-   📂 CSV Upload -- Upload customer reviews easily\
-   😊 Sentiment Classification -- Positive / Neutral / Negative\
-   📊 Sentiment Distribution Chart -- Visual summary of feedback\
-   🔤 Most Common Positive Words -- Identifies strengths\
-   ⚠️ Most Common Negative Words -- Highlights issues\
-   🔍 Filter by Sentiment -- View reviews category-wise\
-   📝 Individual Review View -- Detailed sentiment & polarity


🧪 Sentiment Classification Logic

Sentiment is calculated using TextBlob polarity score

Classification rules:

-   Positive → polarity \> 0.1\
-   Neutral → polarity between -0.1 and 0.1\
-   Negative → polarity \< -0.1

🧑‍💻 Tech Stack

-   🐍 Python\
-   🌐 Flask (Backend Framework)\
-   🎨 HTML, CSS, Jinja2\
-   🧠 NLTK & TextBlob (Text Processing)\
-   📊 Chart.js (Data Visualization)\
-   📁 Pandas (CSV Handling)

🏗️ Project Structure

    sentiment-analysis-flask/
    │
    ├── app.py
    ├── requirements.txt
    ├── README.md
    ├── sample_reviews.csv
    │
    ├── templates/
    │   ├── index.html
    │   ├── dashboard.html
    │   └── review_details.html
    │
    ├── static/
    │   ├── css/
    │   │   └── style.css
    │   └── images/
    │       ├── frontend.png
    │       └── dashboard.png

⚙️ Installation & Setup

🔹 Step 1: Clone Repository

    git clone https://github.com/your-username/sentiment-analysis-flask.git
    cd sentiment-analysis-flask

🔹 Step 2: Create Virtual Environment

    python -m venv venv
    venv\Scriptsctivate   # Windows

🔹 Step 3: Install Required Libraries

    pip install flask pandas nltk textblob matplotlib

OR using requirements.txt:

    pip install -r requirements.txt

🔹 Step 4: Download NLTK Resources

    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')

🔹 Step 5: Run the Flask Application

    python app.py

🔹 Step 6: Open in Browser

    http://127.0.0.1:5000/

📥 Sample CSV Input Format

    review_id,review_text
    1,The product quality is amazing and delivery was fast
    2,Customer support was okay not great
    3,Very disappointed with the service
    4,Excellent experience will buy again
    5,Worst product ever

