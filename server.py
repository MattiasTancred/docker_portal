from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/run_gui', methods=['POST'])
def run_gui():
    os.system('python3 client.py &')
    return jsonify({"status": "Script launched"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
