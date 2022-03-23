from flask import Flask, redirect, url_for, render_template
import os, socket

app = Flask(__name__, static_url_path='/static')

def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return "Up"
    except:
        return "Down"
    finally:
        s.close()

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/commands")
def commands():
    return render_template("commands.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)