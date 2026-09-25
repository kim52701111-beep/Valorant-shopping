from flask import Flask, jsonify, request
import os
import time

app = Flask(__name__)

SHOP_DATA = [
    {
        "name": "프라임 밴달",
        "price": 1775,
        "type": "무기 스킨"
    },
    {
        "name": "RGX 11Z 프로 팬텀",
        "price": 2175,
        "type": "무기 스킨"
    },
    {
        "name": "약탈자 카람빗",
        "price": 4350,
        "type": "근접 무기"
    },
    {
        "name": "스펙트럼 클래식",
        "price": 1775,
        "type": "무기 스킨"
    }
]

SHOP_UPDATED = int(time.time())

@app.route("/")
def home():
    return jsonify({
        "success": True,
        "service": "VALORANT SHOP BOT",
        "version": "1.0.0",
        "status": "online"
    })

@app.route("/health")
def health():
    return jsonify({
        "success": True,
        "status": "online"
    })

@app.route("/shop")
def shop():
    return jsonify({
        "success": True,
        "updated": SHOP_UPDATED,
        "shop": SHOP_DATA
    })

@app.route("/shop/update", methods=["POST"])
def update_shop():
    admin_token = os.environ.get("SHOP_ADMIN_TOKEN")
    request_token = request.headers.get("X-Admin-Token")

    if not admin_token or request_token != admin_token:
        return jsonify({
            "success": False,
            "message": "Unauthorized"
        }), 401

    data = request.get_json(silent=True)

    if not data or "shop" not in data:
        return jsonify({
            "success": False,
            "message": "shop 데이터가 필요합니다."
        }), 400

    if not isinstance(data["shop"], list):
        return jsonify({
            "success": False,
            "message": "shop은 배열이어야 합니다."
        }), 400

    global SHOP_DATA
    global SHOP_UPDATED

    SHOP_DATA = data["shop"]
    SHOP_UPDATED = int(time.time())

    return jsonify({
        "success": True,
        "message": "상점 데이터가 업데이트되었습니다.",
        "updated": SHOP_UPDATED,
        "shop": SHOP_DATA
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
