from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

datas = [
    {
        "title": "用 AXIOS 串接API",
        "content": "將任務改成若可以連接得到伺服端，則使用伺服端資料修改。"
    },
    {
        "title": "實作 Flask RESTful API",
        "content": "用 Flask 實作 CRUD"
    },
    {
        "title": "完成 Vue.js 前端頁面",
        "content": "基本 TODO LIST 頁面"
    },
]
@app.route('/')
def home():
    return "<h1>Hello API</h1>"

@app.route('/api/task')
def getTask():
    return jsonify(datas)

if __name__ == '__main__':
    app.run()