from flask import Flask
import datetime
import time

# for Readiness Probe 
time.sleep(60)
app = Flask(__name__)

@app.route("/")
def main():
    currentDT = datetime.datetime.now()
    return "ZEZE LOVE current time is " + str(currentDT)

@app.route("/health")
def health():

    return "OK"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
