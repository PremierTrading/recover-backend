
from flask import Flask, send_file
app = Flask(__name__)

@app.route("/download-backup")
def download_backup():
    return send_file("/mnt/data/full_backup.zip", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

