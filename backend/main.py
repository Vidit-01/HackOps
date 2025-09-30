from flask import Flask,request,jsonify
import pandas
from flask_cors import CORS
from keyword_generator import KeyWordGenerator
from PyPDF2 import PdfReader


app = Flask(__name__)
CORS(app)
keyword = KeyWordGenerator()

@app.route("/reccomend",methods=["POST"])
def recommend():
    #recommend code
    pdf_file = request.files['file']
    if pdf_file:
        reader = PdfReader(pdf_file)
        all_text = "".join(page.extract_text() or "" for page in reader.pages)
        keywords = keyword.run(all_text)
        return jsonify({"keywords":keywords})
    # keywords = keyword.run(pdf_file
    return jsonify({"journals":["IEEE","AMM","DJSCE"]})


if __name__ == "__main__":
    app.run()