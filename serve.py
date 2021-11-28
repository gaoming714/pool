from flask import Flask
import json

app = Flask(__name__)

ip_json = {"2miners":{"eth":"51.195.4.174","ctxc":"51.89.96.117"}}


@app.route("/")
def hello_world():
    return ip_json

if __name__ == '__main__':
    # login_wechat()
    app.run(port=8008)