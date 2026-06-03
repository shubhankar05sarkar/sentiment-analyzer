from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

history = []

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        text = request.form["text"]

        analysis = TextBlob(text)

        polarity = analysis.sentiment.polarity
        subjectivity = analysis.sentiment.subjectivity

        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        result = {
            "text": text,
            "sentiment": sentiment,
            "polarity": round(polarity, 2),
            "subjectivity": round(subjectivity, 2)
        }

        history.insert(0, result)

        if len(history) > 5:
            history.pop()

    return render_template(
        "index.html",
        result=result,
        history=history
    )

if __name__ == "__main__":
    app.run(debug=True)