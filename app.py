from flask import Flask, render_template, request, jsonify
from all_lang import getLLamaresponse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    input_text = data['input_text']
    language = data['language']
    response = getLLamaresponse(input_text, language)
    return jsonify({'code': response})

if __name__ == '__main__':
    app.run(debug=True)
