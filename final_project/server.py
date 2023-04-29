'''Server'''
from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    '''English to French translation'''
    text = request.args.get('textToTranslate')
    return translator.english_to_french(text)

@app.route("/frenchToEnglish")
def french_to_english():
    '''French to English translation'''
    text = request.args.get('textToTranslate')
    # Write your code here
    return translator.french_to_english(text)

@app.route("/")
def render_index_page():
    '''Index Page'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
