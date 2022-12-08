from flask import Flask, request, jsonify, redirect
from telegram.ext import Updater


app = Flask(__name__)


def send_message(token, chat_id, messag):
    Updater(token=token, use_context=True).bot.send_message(chat_id=chat_id, text=messag)


@app.route("/")
def hello():
    return redirect("/message")


@app.route("/message", methods=['GET'])
def message():
    try:
        chat_id = request.args.get('chat_id')
        message = request.args.get('message')
        token = request.args.get("token")
        send_message(token, chat_id, message)
        return jsonify({'status': 'OK'})
    except Exception as e:
        return jsonify({'status': 'ERROR', 'error': str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999)
