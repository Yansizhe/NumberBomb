from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# 全局变量存储游戏状态
game_state = {
    "res": 0,
    "count": 0,
    "left": 1,
    "right": 100
}



@app.route("/start", methods=["GET"])
def start():
    game_state["res"] = random.randint(1, 100)
    game_state["count"] = 0
    game_state["left"] = 1
    game_state["right"] = 100
    return jsonify({"message": "游戏开始"})

@app.route("/guess", methods=["POST"])
def guess():
    data = request.json
    number = data["number"]
    res = game_state["res"]
    game_state["count"] += 1
    count = game_state["count"]

    if number < res:
        game_state["left"] = number + 1
        return jsonify({"result": "small", "count": count, "left": game_state["left"], "right": game_state["right"]})
    elif number > res:
        game_state["right"] = number - 1
        return jsonify({"result": "big", "count": count, "left": game_state["left"], "right": game_state["right"]})
    else:
        binary_list = binary_search(res)
        return jsonify({"result": "correct", "count": count, "binary_list": binary_list})

@app.route("/")
def index():
    return render_template("index.html")

def binary_search(target):
    result = []
    l, r = 1, 100
    while True:
        mid = (l + r) // 2
        result.append(mid)
        if mid < target:
            l = mid + 1
        elif mid > target:
            r = mid - 1
        else:
            break
    return result


import threading
import webview


def start_server():
    app.run(debug=False)


if __name__ == "__main__":
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()

    import time

    time.sleep(1)

    window = webview.create_window(
        "数字炸弹游戏",
        "http://127.0.0.1:5000",
        width=800,
        height=600,
        resizable=False
    )


    def on_loaded():
        window.evaluate_js("""
            document.addEventListener('keydown', function(e) {
                if (e.key === 'Enter') {
                    document.getElementById('submit').click();
                }
            });
        """)


    window.events.loaded += on_loaded
    webview.start()