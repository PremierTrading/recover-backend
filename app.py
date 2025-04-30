from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="ok")

@app.route("/download-backup", methods=["GET"])
def download_backup():
    db_path = os.path.join(BASE_DIR, "src", "trades_live.db")
    try:
        return send_file(db_path, as_attachment=True)
    except Exception as e:
        app.logger.exception("Error in /download-backup")
        return jsonify(error=str(e)), 500

@app.route("/webhook", methods=["POST"])
def tv_webhook():
    data = request.get_json(force=True)
    app.logger.info(f"📢 TV alert received: %s", data)
    # TODO: persist data to your DB here
    return jsonify(status="received"), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
