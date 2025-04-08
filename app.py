from flask import Flask, render_template, request

app = Flask(__name__)

# Danh sách key hợp lệ
VALID_KEYS = ["Code150k", "Key123"]

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/check_key", methods=["POST"])
def check_key():
    key = request.form.get("key")
    if key in VALID_KEYS:
        return "success"
    return "fail"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
