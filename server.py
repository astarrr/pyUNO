from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room, send

from uno import generate_cards

app = Flask("UNO")
socketio = SocketIO(app)


@socketio.on('connect', namespace='/chat')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', room=room)


if __name__ == '__main__':
    socketio.run(app, debug=True)

cards = []
deck = []


# @app.route('/')
# def init():
#     cards = generate_cards()
#     return str(len(cards))





