from flask import Flask, jsonify

app = flask.Flask(__name__)

songJson = [
    {
        "albumId":1,
        "id": 1,
        "songName":"songName1",
        "downloadLink": "https://link1",
        "imageLink": "https://imgLink1"
    },
    {
        "albumId":1,
        "id": 2,
        "songName":"songName1",
        "downloadLink": "https://link2",
        "imageLink": "https://imgLink2"
    },
    {
        "albumId":1,
        "id": 3,
        "songName":"songName1",
        "downloadLink": "https://link3",
        "imageLink": "https://imgLink3"
    },
    {
        "albumId":1,
        "id": 4,
        "songName":"songName1",
        "downloadLink": "https://link4",
        "imageLink": "https://imgLink4"
    },
    {
        "albumId":1,
        "id": 5,
        "songName":"songName1",
        "downloadLink": "https://link5",
        "imageLink": "https://imgLink5"
    },
    {
        "albumId":1,
        "id": 6,
        "songName":"songName1",
        "downloadLink": "https://link6",
        "imageLink": "https://imgLink6"
    },
    {
        "albumId":1,
        "id": 7,
        "songName":"songName1",
        "downloadLink": "https://link7",
        "imageLink": "https://imgLink7"
    },
    {
        "albumId":1,
        "id": 8,
        "songName":"songName1",
        "downloadLink": "https://link8",
        "imageLink": "https://imgLink8"
    },
    {
        "albumId":1,
        "id": 9,
        "songName":"songName1",
        "downloadLink": "https://link9",
        "imageLink": "https://imgLink9"
    },
    {
        "albumId":1,
        "id": 10,
        "songName":"songName1",
        "downloadLink": "https://link10",
        "imageLink": "https://imgLink10"
    }
]

@app.route('/hello')
def hello_world():
    return 'Hello, Welcome to our hand made API'

@app.route('/sName')
def songName():
    return jsonify(songJson)

if __name__ =="__main__":
    app.run(debug = True)