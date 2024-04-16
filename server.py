from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

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


@app.route('/api/task/', methods=['GET'])
def getTask():
    return jsonify(datas)
        
    
@app.route('/api/task/', methods=['POST'])
def postTask():
    item = request.get_json()
    print("[POST]", item)
    datas.insert(0, item)
    print(datas)
    return item


@app.route('/api/task/<ID>/', methods=['PUT'])
def updateTask(ID):
    pass


@app.route('/api/task/<ID>/', methods=['DELETE'])
def deleteTask(ID):
    print("[DELETE]"+ID);
    datas.pop(int(ID))
    return ID

if __name__ == '__main__':
    app.run(debug=True)
