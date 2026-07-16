from flask import Flask, request, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

infos_recues = []

@app.route('/')
def home():
    return render_template('index.html', infos=infos_recues)

@app.route('/api/info', methods=['POST'])
def recevoir_info():
    data = request.json
    if data:
        data['ip_visiteur'] = request.remote_addr
        data['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        infos_recues.append(data)
        return jsonify({"status": "ok"}), 200
    return jsonify({"status": "error"}), 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
