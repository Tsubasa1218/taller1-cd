from flask import Flask
from datetime import datetime
import yfinance_test

app = Flask(__name__)

@app.route("/")
def hello_world():
    return yfinance_test.test().to_html()

if __name__ == "__main__":
    print(f"{datetime.now()}")
    app.run(host="0.0.0.0")

