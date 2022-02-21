from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    frenchtranslation = translator.english_to_french(textToTranslate)
    return frenchtranslation

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    englishtranslation = translator.french_to_english(textToTranslate)
    return englishtranslation

@app.route("/")
def renderIndexPage():
    # render the template
    return render_template("index.html")
    

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8080)
    app.run(debug=True)



