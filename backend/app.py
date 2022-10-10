import os
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import pandas as pd
import main

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__, static_url_path='', 
            static_folder='results',)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['DEBUG'] = True

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.errorhandler(Exception)
def handle_exception(err):
    response = {
      "error": err.description
    }
    if len(err.args) > 0:
        response["message"] = err.args[0]
    return jsonify(response), err.code

@app.route('/', methods=['POST'])
@cross_origin()
def upload_file():
    # checking for file
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file and allowed_file(file.filename):
        print("Saving file")
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) 

    # getting data from form
    print("Getting data from input")
    model_type = request.form.get("model_type")
    cleaning_data_type = request.form.get("cleaning_data_type")
    percent_num = request.form.get("percent_num")
    encoding_type = request.form.get("encoding_type")
    discarded_columns = request.form.get("discarded_columns")
    if discarded_columns == "no-col":
        discarded_columns_array = []
    else :
        discarded_columns_array = discarded_columns.split(',')
    label = request.form.get("label")

    response = main.main(file_path=app.config['UPLOAD_FOLDER']+ '/' + file.filename, label=label, model_type=model_type, cleaning_data_type=cleaning_data_type, percent_num = percent_num,encoding_type=encoding_type, discarded_columns_array=discarded_columns_array)

    # return data
    return response

if __name__ == '__main__':
    app.run()