from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "VALORANT SHOP BOT"

@app.route("/shop")
def shop():
    return jsonify({
        "success": True,
        "shop": [
            {
                "name": "프라임 밴달",
                "price": 1775
            },
            {
                "name": "RGX 11Z 프로 팬텀",
                "price": 2175
            },
            {
                "name": "약탈자 카람빗",
                "price": 4350
            },
            {
                "name": "스펙트럼 클래식",
                "price": 1775
            }
        ]
    })

if __name__ == "__main__":
    app.run()
