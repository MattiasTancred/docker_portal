from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_data():
    data = request.json
    result = process(data)
    return jsonify(result)

def process(data):
    # Process the data and return the result
    # This is just a dummy example
    result = {'processed_data': data}
    return result

@app.route('/run_gui', methods=['POST'])
def run_gui():
    os.system('python3 client.py &')
    return jsonify({"status": "Script launched"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
