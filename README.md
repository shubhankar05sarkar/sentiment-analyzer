# Sentiment Analyzer 

A web-based Sentiment Analysis Dashboard developed using Flask and TextBlob that analyzes user-entered text and classifies it as Positive, Negative, or Neutral. The application also provides polarity and subjectivity scores to help users understand the emotional tone and nature of the text.

---

## Project Overview

This project uses Natural Language Processing (NLP) techniques through the TextBlob library to perform sentiment analysis on textual data. Users can enter any text through a simple web interface, and the application instantly analyzes the sentiment and displays meaningful insights.

The project was developed using Python and Flask and features a responsive and user-friendly interface built with HTML, CSS, and Bootstrap.

---

## Features

- Analyze user-entered text in real time
- Classify sentiment as:
  - Positive
  - Negative
  - Neutral
- Display polarity score
- Display subjectivity score
- Maintain recent analysis history during the session
- Responsive and modern user interface

---

## Technologies Used

- Python
- Flask
- TextBlob
- HTML5
- CSS3
- Bootstrap 5

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Sentiment-Analyzer-Flask.git
cd Sentiment-Analyzer-Flask
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Download TextBlob Corpora

```bash
python -m textblob.download_corpora
```

### 6. Run the Application

```bash
python app.py
```

### 7. Open in Browser

```text
http://127.0.0.1:5000
```

---

## Understanding the Output

### Sentiment Classification

The application classifies text into three categories:

| Sentiment | Meaning |
|------------|----------|
| Positive | The text expresses a favorable opinion or emotion |
| Neutral | The text does not express a strong positive or negative sentiment |
| Negative | The text expresses an unfavorable opinion or emotion |

### Polarity Score

Polarity measures the sentiment of the text on a scale from -1 to +1.

- -1 indicates highly negative sentiment
- 0 indicates neutral sentiment
- +1 indicates highly positive sentiment

### Subjectivity Score

Subjectivity measures how opinion-based the text is on a scale from 0 to 1.

- 0 indicates factual content
- 1 indicates highly opinionated content

---

## **Author**

Created with ❤️ by **Shubhankar Sarkar**.  
[GitHub Profile](https://github.com/shubhankar05sarkar)
