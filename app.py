import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))

def index():
    if request.method == "POST":
        product = request.form["animal"]
        response = openai.Completion.create(
                            model="text-davinci-003",
                            prompt="Write a creative ad of 20 words approximately for the following product to run on a augmented reality based advertisement platform which advertises retail products(7eleven):\n\nProduct:" + product,
                            temperature=1,
                            max_tokens=100,
                            top_p=1.0,
                            frequency_penalty=0.0,
                            presence_penalty=0.0
                            )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)



