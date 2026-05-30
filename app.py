from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!doctype html>
    <html>
      <head>
        <title>ThunderHouse Core Staging</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </head>
      <body style="font-family: Arial, sans-serif; padding: 40px;">
        <h1>ThunderHouse Core Staging</h1>
        <p>Pipeline proven: GitHub → Coolify → staging.thunderhouseai.com.</p>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "thunderhousecore"
    })
